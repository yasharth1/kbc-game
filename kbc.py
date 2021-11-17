import pyttsx3 # pip install pyttsx3
import winsound # pip install winsound
import time 
from inputimeout import inputimeout, TimeoutOccurred # pip install inputimeout
import matplotlib.pyplot as plt # pip install matplotlib
def check_ans():
  print('jej')
def first():
  rightAns1 = "b)Ram Nath Kovind"
  print("The 1st question for Rs 1000")
  time.sleep(1)
  print("On your screen!!")
  print("Who is the current President of India?")
  winsound.PlaySound("sounds/1st.wav", winsound.SND_FILENAME)
  print("a)Narendra Modi b)Ram Nath Kovind c)Venkaiah Naidu d)Pranab Mukherjee")
  try:
    winsound.PlaySound("sounds/timer.wav", winsound.SND_LOOP + winsound.SND_ASYNC)
    input1 = inputimeout('Enter your answer', timeout=45).lower()
    check_ans(input1, 1000, 0, 0, "b", "b)Ram Nath Kovind", "c)Venkaiah Naidu", "b)Ram Nath Kovind", 45, 1)
  except TimeoutOccurred:
    print("Time over!!")
    winsound.PlaySound("sounds/4000.wav", winsound.SND_FILENAME)
    print("Right answer is a)Dahi (curd). You win Rs 0")
    exit()
first()
def second():
  time.sleep(2)
  print("The 2nd question for Rs 2000")
  time.sleep(1)
  print("On your screen!!")
  time.sleep(0.25)
  print("What is the main ingredient in Lassi?")
  winsound.PlaySound("sounds/1st.wav", winsound.SND_FILENAME)
  print("a)Dahi (curd) b)Milk c)Dal (Pulses) d)Cheese")
  try:
    winsound.PlaySound("sounds/timer.wav", winsound.SND_LOOP + winsound.SND_ASYNC)
    input2 = inputimeout(prompt="Enter your answer", timeout=45).lower()
    check_ans(input2, 2000, 0, 1000, "a", "a)Dahi (curd)", "b)Milk", "a)Dahi (curd)", 45, 2)
  except TimeoutOccurred:
    print("Time over!!")
    winsound.PlaySound("sounds/4000.wav", winsound.SND_FILENAME)
    print("Right answer is a)Dahi (curd). You win Rs 0")
    exit()
second()
def third():
  print("The 3rd question for Rs 3000")
  time.sleep(1)
  print("On your screen!")
  time.sleep(0.25)
  print("Where is the Motera stadium, which is the largest stadium, situated?")
  winsound.PlaySound("sounds/1st.wav", winsound.SND_FILENAME)
  print("a)Delhi b)Mohali c)Ahmedabad d)Chennai")
  try:
    winsound.PlaySound("sounds/timer.wav", winsound.SND_LOOP + winsound.SND_ASYNC)
    input3 = inputimeout(prompt="Enter your answer", timeout=45).lower()
    check_ans(input3, 3000, 0, 2000, "c", "c)Ahmedabad", "d)Chennai", "c)Ahmedabad", 45, 3)
  except TimeoutOccurred:
    print("Time over!!")
    winsound.PlaySound("sounds/4000.wav", winsound.SND_FILENAME)
    print("Right answer is c)Ahmedabad. You win Rs 0")
    exit()
third()
def fourth():
  time.sleep(2)
  print("The 4th question for Rs 5000")
  time.sleep(1)
  print("On your screen!")
  time.sleep(0.25)
  print("Which of these films was the first Indian movie with sound and music?")
  winsound.PlaySound("sounds/1st.wav", winsound.SND_FILENAME)
  print("a)Raja Harishchandra b)Alam Ara c)Shaheed d)Shree 420")
  try:
    winsound.PlaySound("sounds/timer.wav", winsound.SND_LOOP + winsound.SND_ASYNC)
    input3 = inputimeout(prompt="Enter your Answer", timeout=45).lower()
    check_ans(input3, 5000, 0, 3000, "b", "a)Raja Harishchandra", "b)Alam Ara", "b)Alam Ara", 45, 4)
  except TimeoutOccurred:
    print("Time over!!")
    winsound.PlaySound("sounds/4000.wav", winsound.SND_FILENAME)
    print("Right answer is b)Alam Ara. You win Rs 0")
    exit()
fourth()
def audio1():
  winsound.PlaySound("sounds/trystwithdestiny.wav", winsound.SND_FILENAME)
def option5():
    try:
      time.sleep(1)
      print("a)Sardar Patel b)Maulana Abul Kalam c)Veer Savarkar d)Jawaharlal Nehru")
      winsound.PlaySound("sounds/timer.wav", winsound.SND_LOOP + winsound.SND_ASYNC)
      input5 = inputimeout(prompt="Enter your Answer", timeout=45).lower()
      check_ans(input5, 10000, 0, 3000, "d", "c)Veer Savarkar", "d)Jawaharlal Nehru", "d)Jawaharlal Nehru", 45, 5)
    except TimeoutOccurred:
      print("Time over!!")
      winsound.PlaySound("sounds/4000.wav", winsound.SND_FILENAME)
      print("Right answer is d)Jawaharlal Nehru. You win Rs 0")
      exit()
def fifth():
  time.sleep(2)
  print("The 5th question for Rs 10,000")
  time.sleep(1)
  print("On your screen!!")
  time.sleep(0.25)
  print("Identify the renowned freedom fighter and politician in this audio clip")
  winsound.PlaySound("sounds/1st.wav", winsound.SND_FILENAME)
  time.sleep(1)
  winsound.PlaySound("sounds/trystwithdestiny.wav", winsound.SND_FILENAME)
  repeat = input("Do you want to hear the audio again (Y/n)?").lower()
  if repeat == "y" or repeat == "Y":
    print("Playing audio...")
    audio1()
    option5()
  else: 
    option5()
fifth()
print("Congratulations, you have passed the first stage! Now you will take at least Rs 10000 from here!")
time.sleep(2)
print("Now you will get 60 seconds to answer the questions")
def sixth():
  time.sleep(2)
  print("The 6th question for Rs 20,000")
  time.sleep(1)
  print("On your screen!!")
  time.sleep(0.25)
  print("Which of these films was the first Indian movie with sound and music?")
  winsound.PlaySound("sounds/20000play.wav", winsound.SND_FILENAME)
  print("a)Raja Harishchandra b)Alam Ara c)Shaheed d)Shree 420")
  try:
    winsound.PlaySound("sounds/timer.wav", winsound.SND_LOOP + winsound.SND_ASYNC)
    input6 = inputimeout(prompt="Enter your Answer", timeout=45).lower()
    check_ans(input6, 20000, 10000, 10000, "b", "a)Raja Harishchandra", "b)Alam Ara", "b)Alam Ara", 45, 6)
  except TimeoutOccurred:
    print("Time over!!")
    winsound.PlaySound("sounds/20000lose.wav", winsound.SND_FILENAME)
    print("Right answer is b)Alam Ara. You win Rs 0")
    exit()