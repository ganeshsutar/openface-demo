import cv2
import openface

bgrImg = cv2.imread('test.jpg')
rgbImg = cv2.cvtColor(bgrImg, cv2.COLOR_BGR2RGB)

align = openface.AlignDlib('shape_predictor_68_face_landmarks.dat')
net = openface.TorchNeuralNet()

bb = align.getLargestFaceBoundingBox(rgbImg)
alignedFace = align.align(96, rgbImg, bb, landmarkIndices=openface.AlignDlib.OUTER_EYES_AND_NOSE)
rep = net.forward(alignedFace)

print rep
