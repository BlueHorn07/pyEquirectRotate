import numpy as np
import cv2

from equirectRotate import EquirectRotate, pointRotate

if __name__ == '__main__':
  print("=== rotate equirectangular image ===")

  # open source image
  src_path = "../demo/equirectangular_earth.png"
  src_image = cv2.imread(src_path)

  h, w, c = src_image.shape

  # rotate source image
  equirectRot1 = EquirectRotate(h, w, (-30, 26, 57))
  rotated_image = equirectRot1.rotate(src_image)
  cv2.imshow("rotated image", rotated_image)
  cv2.waitKey()
  cv2.destroyAllWindows()

  # wrong inverse rotation
  equirectRot2 = EquirectRotate(h, w, (30, -26, -57))
  rotated_image2 = equirectRot2.rotate(rotated_image)
  cv2.imshow("not restored image", rotated_image2)
  cv2.waitKey()
  cv2.destroyAllWindows()

  # correct inverse rotation
  equirectRot1.setInverse(True)
  invRotated_image = equirectRot1.rotate(rotated_image)
  cv2.imshow("correctly restored image", invRotated_image)
  cv2.waitKey()
  cv2.destroyAllWindows()

  print("=== rotate index pixel in equirectangular ===")
  rotated_point = pointRotate(480, 960, 240, 480, (90, 0, 0))
  print(rotated_point)







