__author__ = 'christalley'

from PIL import Image as pilImage
from random import randint
from imageio import imread, mimwrite
import sys
from images2gif import writeGif

def processImage(infile):
    frames=[]
    try:
        im = pilImage.open(infile)
    except IOError:
        print "Cant load", infile
        sys.exit(1)
    i = 0.0
    mypalette = im.getpalette()
    print mypalette
    myFaceOrig = pilImage.open('./myFace.gif')
    myFace = pilImage.new("RGBA", myFaceOrig.size)
    myFace.paste(myFaceOrig)
    source = myFace.split()
    A=3
    B=2
    G=1
    R=0
    print "++++++++++++"
    print source[A]
    print "++++++++++++++++"
    mask = source[B].point(lambda i: True and 255)
    out  = source[R].point(lambda i: 255)
    source[R].paste(out, None, mask)
    myFace = pilImage.merge(myFace.mode,source)
    frameNames = []
    locations = [(1,0),(6,1),(11,2),(15,3),(19,5),(22,7),(25,9),(27,13),(29,16),(30,19),(31,22),(31,24),(31,28),(30,32),(29,35),(27,39),(26,40)]

    try:
        while 1:
            dy, dx = locations[int(i)]
            i+=1.0
            mypalette = im.getpalette()
            im.putpalette(mypalette)
            new_im = pilImage.new("RGBA", im.size)
            new_im.paste(im)
            location = (int(new_im.width*(0.59-float(dx)/330)), int(new_im.height*(0.22-float(dy)/450)))
            new_im.paste(myFace.rotate((i-10)*2+float(randint(0,3))/2),location)
            frameNames.append('foo'+str(i)+'.jpg')
            new_im.save(frameNames[-1])
            im.seek(im.tell() + 1)
    except EOFError:
        frames = []
        for name in frameNames:
            print name
            frames.append(imread(name))
        mimwrite("./dancingChris.gif", frames)
        pass # end of sequence

processImage('testDrake.gif')

















