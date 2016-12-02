#! /usr/bin/python
import cv2
import openface
from os import path
import logging

align = openface.AlignDlib('shape_predictor_68_face_landmarks.dat')
net = openface.TorchNeuralNet()

def process(filename, output_dir):
    logging.debug('Process file %s', filename)
    bgrImg = cv2.imread(filename)
    rgbImg = cv2.cvtColor(bgrImg, cv2.COLOR_BGR2RGB)

    logging.debug('Detecting face')

    # TODO: Change to get all the faces
    bb = align.getLargestFaceBoundingBox(rgbImg)
    alignedFace = align.align(96, rgbImg, bb, landmarkIndices=openface.AlignDlib.OUTER_EYES_AND_NOSE)
    rep = net.forward(alignedFace)

    logging.debug('Got the representation')
    logging.debug('Sending output')

    if output_dir == None:
        print rep
    else:
        base_filename = path.basename(filename).split('.')[0]
        logging.debug('Output to file %s', base_filename)
        out_filename = path.join(output_dir, base_filename)
        with open(out_filename, 'w') as json_out:
            json_out.write(str(rep))

if __name__ == "__main__":
    print process(filename)
