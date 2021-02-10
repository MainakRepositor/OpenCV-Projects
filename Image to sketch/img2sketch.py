import cv2
import numpy 
img = cv2.imread('C:/Users/maina/Desktop/rid.jpg')
gi = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
inv_gr_img = 255 - gi
bi = cv2.GaussianBlur(inv_gr_img, (21,21), 0)
inv_bl = 255 - bi
pencil_sk = cv2.divide(gi, inv_bl, scale = 256.0)
pencil = pencil_sk-45
cv2.imshow('Actual Image',img)

cv2.imshow('Pencil Sketch',pencil)


cv2.waitKey(0)
cv2.destroyAllWindows()

# to use it in a loop
k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('image.png',img)
    cv2.destroyAllWindows()