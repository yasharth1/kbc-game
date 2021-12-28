import cv2 as cv
from num2words import num2words
import matplotlib.pyplot as plt
img = cv.imread('cheque.jpg')   #Load the image file into memory
word = num2words(1250000, lang='en_IN') + " only"
cv.putText(img, word, (54, 50), cv.FONT_HERSHEY_SIMPLEX, 0.3, (0,0,0), 0, cv.LINE_AA)
cv.putText(img, "Navneet Kumar", (100, 25), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv.LINE_AA)
cv.putText(img, "1,00,00,000", (260, 57), cv.FONT_HERSHEY_SIMPLEX, 0.2, (0, 0, 0), 1, cv.LINE_AA)
cv.imshow("Your cheque", img)
cv.waitKey(0)
cv.destroyAllWindows()
