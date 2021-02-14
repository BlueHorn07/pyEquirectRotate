import cv2

from equirectRotate import EquirectRotate, pointRotate

if __name__ == '__main__':
  print("=== rotate equirectangular image ===")

  # open source image
  src_path = "../demo/equirectangular_earth.png"
  src_image = cv2.imread(src_path)

  h, w, c = src_image.shape

  # rotate (90, 0, 0)
  equirectRot1 = EquirectRotate(h, w, (90, 0, 0))
  rotated_image = equirectRot1.rotate(src_image)
  cv2.imshow("rotated_90_0_0", rotated_image)
  cv2.imwrite("rotated_90_0_0.png", rotated_image)
  cv2.waitKey()
  cv2.destroyAllWindows()

  # rotate (0, 90, 0)
  equirectRot2 = EquirectRotate(h, w, (0, 90, 0))
  rotated_image2 = equirectRot2.rotate(src_image)
  cv2.imshow("rotated_0_90_0", rotated_image2)
  cv2.imwrite("rotated_0_90_0.png", rotated_image2)
  cv2.waitKey()
  cv2.destroyAllWindows()

  # rotate (0, 0, 90)
  equirectRot3 = EquirectRotate(h, w, (0, 0, 90))
  rotated_image3 = equirectRot3.rotate(src_image)
  cv2.imshow("rotated_0_0_90", rotated_image3)
  cv2.imwrite("rotated_0_0_90.png", rotated_image3)
  cv2.waitKey()
  cv2.destroyAllWindows()


