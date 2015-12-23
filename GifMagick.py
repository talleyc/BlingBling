__author__ = 'christalley'

import os
from wand.image import Image

from wand.drawing import Drawing
from imageio import imread, mimwrite
from random import randint
def placeImage(gif_name, image_name, locations, save_location):
  frame_names = []
  with Image(filename=gif_name) as gif:
    gif_new = gif.clone()
    with Image(filename=image_name) as image_orig:
      new_frames = []
      i=0
      for frame_orig in gif_new.sequence:
        frame = frame_orig.clone()
        x,y = locations[i]
        with Drawing() as draw:
          image = image_orig.clone()
          image.rotate(-1*((i-4)+float(randint(0,6))/2))
          draw.composite(operator='src_over', left=x, top=y,
            width=image.width, height=image.height, image=image)
          draw(frame)
          new_name = save_location.split('.')
          new_name[0]+=str(i)
          frame_names.append('.'.join(new_name))
          frame.save(filename=frame_names[-1])
        i += 1
      with gif.clone() as output:
        output.sequence=new_frames
        output.save(filename=save_location)
  frames = []
  for name in frame_names:
    frames.append(imread(name))
  mimwrite(save_location,frames)



locations = [[282, 60],
             [280, 58],
             [278, 58],
             [276, 56],
             [272, 55],
             [270, 51],
             [265, 50],
             [258, 48],
             [252, 46],
             [247, 46],
             [239, 45],
             [232, 45],
             [227, 46],
             [223, 46],
             [217, 46],
             [215, 46],
             [207, 46]]
placeImage('testDrake.gif','myFace.gif', locations, 'dancingChris.gif')


"""
  Split a gif by its frames
"""
def splitGif(gif_path, save_directory=None):
  if not save_directory:
    save_directory = getMasterDirectoryForGif(gif_path)
  #make directory for this gif
  if not os.path.exists(save_directory):
    os.makedirs(save_directory)
  frame_directory = getFrameDirectoryForGif(gif_path)
  if not os.path.exists(frame_directory):
    os.makedirs(frame_directory)
  with Image(filename=gif_path) as gif:
    i=0
    for frame_orig in gif.sequence:
      frame = frame_orig.clone()
      save_location = getGifFrameLocation(gif_path, i)
      frame.save(filename=save_location)
      i += 1
    gif.save(filename=getGifCopyLocation(gif_path))

def getResultsDirectoryForGif(gif_path):
    return getMasterDirectoryForGif(gif_path) + '/Results/'

def getGifFrameLocation(gif_path, frame_index):
    return getFrameDirectoryForGif(gif_path)+'frame'+str(frame_index)+'.jpeg'

def getGifCopyLocation(gif_path):
    return getMasterDirectoryForGif(gif_path)+getGifName(gif_path)+'.gif'

def getGifName(gif_path):
    return gif_path.split('/')[-1].split('.')[0]

def getFrameDirectoryForGif(gif_path):
    return getMasterDirectoryForGif(gif_path) + 'Frames/'

def getMasterDirectoryForGif(gif_path):
  dir = '/'.join(gif_path.split('/')[:-1]) + '/'
  gif_name = gif_path.split('/')[-1]
  return dir + gif_name.split('.')[0]+'/'


#splitGif('./testDrake.gif')
