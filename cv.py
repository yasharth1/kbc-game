import cv2 as cv
from num2words import num2words
import matplotlib.pyplot as plt
from datetime import date
img = cv.imread('cheque.jpg')   #Load the image file into memory
year = date.today().year - 2000
word = num2words(1250000, lang='en_IN') + " only"
cv.putText(img, str(date.today().day) + "/" + str(date.today().month), (776, 67), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv.LINE_AA)
cv.putText(img, "/" + str(year), (828, 67), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv.LINE_AA)
cv.putText(img, word, (161, 165), cv.FONT_HERSHEY_SIMPLEX, 1.2, (70, 70, 70), 0, cv.LINE_AA)
cv.putText(img, "Navneet Kumar", (88, 125), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 1, cv.LINE_AA)
cv.putText(img, "1,00,00,000", (776, 211), cv.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 0), 1, cv.LINE_AA)
cv.imshow("Your cheque", img)
cv.waitKey(0)
cv.destroyAllWindows()
img = plt.imread('cheque.jpg')
plt.imshow(img)
plt.axis('on')
plt.show()