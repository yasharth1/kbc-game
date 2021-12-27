import cv2 as cv
import matplotlib.pyplot as plt
img = cv.imread('cheque.jpg')   #Load the image file into memory
cv.putText(img, "Navneet Kumar", (100, 25), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv.LINE_AA)
cv.putText(img, "1,00,00,000", (260, 57), cv.FONT_HERSHEY_SIMPLEX, 0.2, (0, 0, 0), 1, cv.LINE_AA)
cv.imshow("Your cheque", img)
cv.waitKey(0)
cv.destroyAllWindows()
"""img = cv.imread('cheque.jpg')   #Load the image file into memory
plt.imshow(img)
plt.title('Cheque')
plt.axis('on')
plt.show()"""
