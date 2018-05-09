import cv2
import os
import imageio
from PIL import Image
import time

file_name = 'video-1524189756.mp4'

time_start = time.time()
def mp4_to_frames(vidcap):
    success, image = vidcap.read()
    count = 0   
    while success:
        yield cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        success, image = vidcap.read()
        count += 1

vidcap = cv2.VideoCapture(file_name)
fps = vidcap.get(cv2.CAP_PROP_FPS)
print('Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}'.format(fps))

frames = mp4_to_frames(vidcap)

with imageio.get_writer(os.path.join('output','output.GIF'), mode='I', subrectangles=True, fps = fps) as writer:
    for frame in frames:
        writer.append_data(frame)

with Image.open(os.path.join('output','output.GIF')) as im:
    # im.info['loop']= 0
    print('Output info: {}\n{}'.format(im.info, im.size))
time_end = time.time()
print('Time taken: {}'.format(time_end - time_start))
