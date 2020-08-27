# import sys
#
# from cv2 import cv2
#
# from main import show_frame, clear_file
#
#
# def capture_face(file_name):
#     # Lock
#     write_ok = False
#
#     cap = cv2.VideoCapture(0)
#     sz = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
#           int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
#     fps = 30
#     fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
#
#     vout = cv2.VideoWriter()
#     vout.open(f'{file_name}.mp4', fourcc, fps, sz, True)
#
#     while True:
#         ret, frame = cap.read()
#         show_frame(frame)
#
#         if cv2.waitKey(1) == ord("w"):
#             if not write_ok:
#                 print('Start Recording...')
#                 write_ok = True
#             else:
#                 print('End Recording...')
#                 clear_file(cap, vout)
#                 sys.exit()
#
#         if write_ok:
#             vout.write(frame)