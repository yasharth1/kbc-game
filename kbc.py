# Welcome, here are the guideline if you need them again
# lifeline - to use lifeline
# Either run "pip install -r requirements.txt" or install the packages separately
import threading
import pyttsx3 # pip install pyttsx3
import winsound
from queue import Queue
from num2words import num2words # pip install num2words 
import time
from datetime import date
import matplotlib.pyplot as plt # pip install matplotlib
import cv2 as cv # pip install opencv-python
fiftyUsed = False
flipUsed = False
apUsed = False
ateUsed = False
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
winsound.PlaySound("sounds/KBC.wav", winsound.SND_FILENAME)
print("Hello and welcome to Kaun Banega Crorepati!")
time.sleep(2)
print("There are 15 questions ranging from Rs 1000 to Rs 1 Crore")
time.sleep(2)
print("There are two stages, 1st at Rs 10000 and 2nd at Rs 320000")
time.sleep(2)
print("There are 4 lifelines-")
time.sleep(1.5)
print("1)50-50 2)Ask the expert 3)Audience poll 4)Flip the question")
time.sleep(3.5)
print("Type 'lifeline' if you want to use a lifeline")
time.sleep(2)
print("You can quit by typing 'quit' if you are not sure of the answer")
time.sleep(2.5)
print("The first 5 questions have a time limit of 45 seconds,")
time.sleep(1.5)
print("While the next 5 questions have a time limit of 60 seconds!")
time.sleep(2)
print("Before starting the game, we would like to know your name")
time.sleep(1.5)
global name
name = input("Please enter your name! ")
print("Thanks for entering!")
time.sleep(1.5)
print("So let's start the game!")
time.sleep(2)
def cheque(amt):
  time.sleep(2)
  print(f"Here's your cheque for Rs {amt}!")
  time.sleep(1.5)
  img = cv.imread('cheque.jpg')
  word = num2words(amt, lang='en_IN') + " only"
  year = date.today().year - 2000
  cv.putText(img, str(date.today().day) + "/" + str(date.today().month), (776, 67), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv.LINE_AA)
  cv.putText(img, "/" + str(year), (828, 67), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv.LINE_AA)
  cv.putText(img, word, (161, 165), cv.FONT_HERSHEY_SIMPLEX, 1.2, (70, 70, 70), 0, cv.LINE_AA)
  cv.putText(img, name, (88, 125), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 1, cv.LINE_AA)
  cv.putText(img, str(amt), (776, 211), cv.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 0), 1, cv.LINE_AA)
  cv.imshow("Your cheque", img)
  cv.waitKey(0)
  cv.destroyAllWindows()
def speak(audio):
  engine.say(audio)
  engine.runAndWait()
def time_up(rightOp, lostAmt, time_limit):
  winsound.PlaySound("sounds/4000.wav", winsound.SND_FILENAME)
  print(f"\n{time_limit} seconds have elapsed! Your time is over!!")
  time.sleep(1)
  print(f"The correct answer is {rightOp}! You fall back to Rs {lostAmt}!")
  time.sleep(5)
  print("You played really well! Thank you for playing!")
  time.sleep(1.5)
  print("We will take your leave now!")
  winsound.PlaySound("sounds/closing.wav", winsound.SND_FILENAME)
  exit()
global answer
answer = None
def inputtime(rightOp, lostAmt, time_limit):
  def input_thread():
    input_queue.put(input("Enter your answer"))
  input_queue = Queue()
  input_thread = threading.Thread(target=input_thread)
  input_thread.daemon = True
  input_thread.start()
  input_thread.join(time_limit)
  if input_thread.is_alive():
    time_up(rightOp, lostAmt, time_limit)
  else:
    return input_queue.get()
def quit(winAmt, lostAmt, quitAmt, rightAns, firstOp, secondOp, rightOp, time_limit, qno):
  winsound.PlaySound("sounds/ping.wav", winsound.SND_FILENAME)
  if qno == 6:
    print("I will not let you quit at this point! You will not lose anything even if you get the question wrong!")
    time.sleep(2)
    inputtime(rightOp, 0, 45)
    check_ans(answer, 20000, 10000, 10000, rightAns, firstOp, secondOp, rightOp, 45, 6)
  elif qno == 11:
    print("I will not let you quit at this point! You will not lose anything even if you get the question wrong!")
    time.sleep(2)
    winsound.PlaySound("sounds/640000ques.wav", winsound.SND_LOOP + winsound.SND_ASYNC)
    quit_input = input("Enter Your answer ").lower()
    check_ans(quit_input, 640000, 320000, 320000, rightAns, firstOp, secondOp, rightOp, 45, 11)
  else:
    confirm = input("Are you sure you want to quit?(y/n) ").lower()
    if confirm == "y":
      print(f"Thank you for playing! You won Rs {quitAmt}!")
      time.sleep(2)
      print(f"The correct answer is {rightOp}")
      cheque(quitAmt)
      time.sleep(2)
      print("We will take your leave now!")
      winsound.PlaySound("sounds/closing.wav", winsound.SND_FILENAME)
      exit()
    elif confirm == "n":
      if quitAmt > 320000:
        print("Okay, let's continue the game!")
        time.sleep(2)
        winsound.PlaySound("sounds/" + str(winAmt) + "ques.wav", winsound.SND_LOOP + winsound.SND_ASYNC)
        quit_input = input("Enter your answer ").lower()
        check_ans(quit_input, winAmt, lostAmt, quitAmt, rightAns, firstOp, secondOp, rightOp, time_limit, qno)
      elif quitAmt < 320000:
        print("Okay, let's continue the game!")
        time.sleep(2)
        inputtime(rightOp, 0, time_limit)
        check_ans(answer, winAmt, lostAmt, quitAmt, rightAns, firstOp, secondOp, rightOp, time_limit, qno)
def wrong(correctAns, winAmt, lostAmt, qno):
  if qno > 5:
    print(f"Wrong answer! The correct answer is {correctAns}! You fall back to Rs {lostAmt}")
    winsound.PlaySound("sounds/" + str(winAmt) + "lose.wav", winsound.SND_FILENAME)
    print("Thank you for playing the game! You played really well!")
    cheque(lostAmt)
    time.sleep(1.5)
    print("We will now take your leave")
    winsound.PlaySound("sounds/closing.wav", winsound.SND_FILENAME)
    print(":-)")
    exit()
  else:
    print(f"Wrong answer! The correct answer is {correctAns}! You fall back to Rs {lostAmt}")
    winsound.PlaySound("sounds/4000.wav", winsound.SND_FILENAME)
    print("Thank you for playing the game! You played really well, but unfortunately, you gave a wrong answer!")
    time.sleep(2)
    print("We will take your leave now!")
    winsound.PlaySound("sounds/closing.wav", winsound.SND_FILENAME)
    exit()
def ask_the_expert(lostAmt, winAmt, quitAmt, rightAns, firstOp, secondOp, rightOp, time_limit, qno):
  global ateUsed
  ateUsed = True
  print("Hello, This is your expert Mister Know it all")
  speak("Hello, This is your expert Mister Know it all")
  print("I am here to help you")
  speak("I am here to help you")
  print("Let me see this question once.")
  speak("Let me see this question once.")
  time.sleep(2)
  print("Thinking...")
  time.sleep(2)
  print("Analyzing the brain database...")
  time.sleep(3)
  print("Okay, I have found the answer!")
  time.sleep(3)
  print(f"I believe answer of this question should be {rightOp}")
  speak(f"I believe answer of this question should be {rightOp}")
  if qno < 11:
    winsound.PlaySound("sounds/timer.wav", winsound.SND_LOOP + winsound.SND_ASYNC)
    inputtime(rightOp, lostAmt, time_limit)
    check_ans(answer, winAmt, lostAmt, quitAmt, rightAns, firstOp, secondOp, rightOp, time_limit, qno)
  else:
    winsound.PlaySound("sounds/" + str(winAmt) + "ques.wav", winsound.SND_LOOP + winsound.SND_ASYNC)
    user_input = input("Enter your answer ").lower()
    check_ans(user_input, winAmt, lostAmt, quitAmt, rightAns, firstOp, secondOp, rightOp, time_limit, qno)
def flip(winAmt, lostAmt, quitAmt, rightOp, rightAns, time_limit, qno):
  global flipUsed
  flipUsed = True
  print("Activating Flip the Question Lifeline...")
  time.sleep(2)
  print("Before proceeding, we would like you to guess the answer")
  time.sleep(1)
  flip_input = input("Guess an answer ").lower()
  time.sleep(1.5)
  if flip_input == rightAns:
      print("Your answer would have been correct!")
      time.sleep(1)
      print("Now flipping the question...")
  else:
    print("Your answer would have been wrong! Thank God you took a lifeline! Correct answer is " + rightOp)
    time.sleep(2)
    print("Now flipping the question...")
  time.sleep(1.5)
  if qno <= 5:
    winsound.PlaySound("sounds/1st.wav", winsound.SND_FILENAME)
    print("Fill in the blank in this hindi proverb which means to run away- '______ Dabaakar Bhaagna'")
    winsound.PlaySound("sounds/timer.wav", winsound.SND_LOOP + winsound.SND_ASYNC)
    inputtime("a)दुम", 0, 45)
    check_ans(answer, winAmt, lostAmt, quitAmt, "a", "a)दुम", "c)हाथ", "a)दुम", time_limit, qno)
  elif qno > 5 and qno <= 10:
    winsound.PlaySound("sounds/question.wav", winsound.SND_FILENAME)
    print("To which group of sportspersons is the Dronacharya Award given?")
    time.sleep(2)
    print("a)Players b)Support Staff c)Administrators d)Coaches")
    winsound.PlaySound("sounds/timer.wav", winsound.SND_LOOP + winsound.SND_ASYNC)
    inputtime("a)Coaches", 10000, 60)
    check_ans(answer, winAmt, lostAmt, quitAmt, "d", "d)Support Staff", "d)Coaches", "d)Coaches", time_limit, qno)
  elif qno > 10:
    winsound.PlaySound("sounds/" + str(winAmt) + "play.wav", winsound.SND_FILENAME)
    print("When the Lucknow pact was adopted in 1916 Mohammad Ali Jinnah represented the Muslim League, who represented the Indian National Congress?")
    time.sleep(1.5)
    print("a)Mahatma Gandhi b)Lokmanya Tilak c)Motilal Nehru d)Sardar Vallabhbhai Patel")
    winsound.PlaySound("sounds/" + str(winAmt) + "ques.wav", winsound.SND_LOOP + winsound.SND_ASYNC)
    flip_3 = input("Enter your answer ").lower()
    check_ans(flip_3, winAmt, lostAmt, quitAmt, "b", "a)Mahatma Gandhi", "b)Lokmanya Tilak", "b)Lokmanya Tilak", time_limit, qno)
def fifty_fifty(lostAmt, winAmt, quitAmt, firstOp, secondOp, rightOp, rightAns, time_limit, qno):
  global fiftyUsed
  fiftyUsed = True
  if qno < 11:
    time.sleep(2)
    winsound.PlaySound("sounds/fifty2.wav", winsound.SND_FILENAME)
    print(f"Two options are left {firstOp} and {secondOp}")
    winsound.PlaySound("sounds/timer.wav", winsound.SND_LOOP + winsound.SND_ASYNC)
    inputtime(rightOp, lostAmt, time_limit)
    check_ans(answer, winAmt, lostAmt, quitAmt, rightAns, firstOp, secondOp, rightOp, time_limit, qno)
  else:
    time.sleep(2)
    winsound.PlaySound("sounds/fifty2.wav", winsound.SND_FILENAME)
    print(f"Two options are left {firstOp} and {secondOp}")
    winsound.PlaySound("sounds/" + str(winAmt) + "ques.wav", winsound.SND_LOOP + winsound.SND_ASYNC)
    if qno == 15:
      fifteenth()
    else: 
      userAns = input("Enter your answer! ").lower()
      check_ans(userAns, winAmt, lostAmt, quitAmt, rightAns, firstOp, secondOp, rightOp, time_limit, qno)
def audience_poll(lostAmt, winAmt, quitAmt, firstOp, secondOp, rightOp, rightAns, time_limit, qno, a_percent, b_percent, c_percent, d_percent):
  global apUsed
  apUsed = True
  print("Activating audience poll lifeline...")
  time.sleep(1)
  print("Giving the audience voting meters...")
  time.sleep(2)
  print("Voting...")
  winsound.PlaySound("sounds/audience.wav", winsound.SND_FILENAME)
  options = ["A", "B", "C", "D"]
  percent = [a_percent, b_percent, c_percent, d_percent]
  plt.bar(options, percent, color='maroon', width=0.4)
  plt.show()
  if qno < 11:
    inputtime(rightOp, lostAmt, time_limit)
    check_ans(answer, winAmt, lostAmt, quitAmt, rightAns, firstOp, secondOp, rightOp, time_limit, qno)
  else:
    winsound.PlaySound("sounds/" + str(winAmt) + "ques.wav", winsound.SND_LOOP + winsound.SND_ASYNC)
    ap_input = input("Enter Your answer ").lower()
    check_ans(ap_input, winAmt, lostAmt, quitAmt, rightAns, firstOp, secondOp, rightOp, time_limit, qno)
def useLifeline(ll_input, lostAmt, winAmt, quitAmt, rightAns, firstOp, secondOp, rightOp, time_limit, qno):
  winsound.PlaySound("sounds/ping.wav", winsound.SND_FILENAME)
  if ll_input == "lifeline":
    if fiftyUsed == True and apUsed == True and ateUsed == True and flipUsed == True:
      if qno > 10:
        print("You have used all the lifelines. Please choose another option")
        winsound.PlaySound("sounds/" + str(winAmt) + "ques.wav", winsound.SND_LOOP + winsound.SND_ASYNC)
        all_lfl_used = input("You can either quit or try to answer ").lower()
        check_ans(all_lfl_used, winAmt, lostAmt, quitAmt, rightAns, firstOp, secondOp, rightOp, time_limit, qno)
      else:
        print("You have used all the lifelines. You can either quit or try to answer")
        time.sleep(2.5)
        inputtime(rightOp, lostAmt, time_limit)
        check_ans(answer, winAmt, lostAmt, quitAmt, rightAns, firstOp, secondOp, rightOp, time_limit, qno)
    else:
      global lifeline
      lifeline = input("What lifeline do you want to use? Type 'ff' for 50-50, 'flip' for flip the question, 'ate' for ask the expert and 'ap' for audience poll ").lower()
      if lifeline == "ff":
        if fiftyUsed == True:
          print("You have already used the 50-50 lifeline")
          useLifeline(ll_input, lostAmt, winAmt, quitAmt, rightAns, firstOp, secondOp, rightOp, time_limit, qno)
        elif fiftyUsed == False:
          fifty_fifty(lostAmt, winAmt, quitAmt, firstOp, secondOp, rightOp, rightAns, time_limit, qno)
      elif lifeline == "flip":
        if flipUsed == True:
          print("You have already used this lifeline")
          useLifeline(ll_input, lostAmt, winAmt, quitAmt, rightAns, firstOp, secondOp, rightOp, time_limit, qno)
        elif flipUsed == False:
          flip(winAmt, lostAmt, quitAmt, rightOp, rightAns, time_limit, qno)
      elif lifeline == "ap":
        if apUsed:
          print("You have already used the Audience poll Lifeline")
          useLifeline(ll_input, lostAmt, winAmt, quitAmt, rightAns, firstOp, secondOp, rightOp, time_limit, qno)
        elif apUsed == False:
          if rightAns == "a":
            audience_poll(lostAmt, winAmt, quitAmt, firstOp, secondOp, rightOp, rightAns, time_limit, qno, 52, 36, 5, 7)
          elif rightAns == "b":
            audience_poll(lostAmt, winAmt, quitAmt, firstOp, secondOp, rightOp, rightAns, time_limit, qno, 12, 45, 23, 20)
          elif rightAns == "c":
            audience_poll(lostAmt, winAmt, quitAmt, firstOp, secondOp, rightOp, rightAns, time_limit, qno, 10, 24, 47, 19)
          elif rightAns == "d":
            audience_poll(lostAmt, winAmt, quitAmt, firstOp, secondOp, rightOp, rightAns, time_limit, qno, 19, 21, 22, 38)
      elif lifeline == "ate":
        if ateUsed:
          print("You have already used this lifeline!")
          useLifeline(ll_input, lostAmt, winAmt, quitAmt, rightAns, firstOp, secondOp, rightOp, time_limit, qno)
        elif ateUsed == False:
          ask_the_expert(lostAmt, winAmt, quitAmt, rightAns, firstOp, secondOp, rightOp, time_limit, qno)
      else:
        hello = input("Invalid input! Do you really want to use a lifeline?(y/n) ").lower()
        if hello == "y":
            useLifeline(ll_input, lostAmt, winAmt, quitAmt, rightAns, firstOp, secondOp, rightOp, time_limit, qno)
        else:
          if qno < 11:
            winsound.PlaySound("sounds/timer.wav", winsound.SND_LOOP + winsound.SND_ASYNC)
            inputtime(rightOp, lostAmt, time_limit)
            check_ans(answer, winAmt, lostAmt, quitAmt, rightAns, firstOp, secondOp, rightOp, time_limit, qno)
          else:
            winsound.PlaySound("sounds/" + str(winAmt) + "ques.wav", winsound.SND_LOOP + winsound.SND_ASYNC)
            lfl_input = input("Enter Your answer ").lower()
            check_ans(lfl_input, winAmt, lostAmt, quitAmt, rightAns, firstOp, secondOp, rightOp, time_limit, qno)
def useLifeline_2(lostAmt, winAmt, quitAmt, rightAns, firstOp, secondOp, rightOp, time_limit, qno):
  print("You can only use the 50-50 lifeline! All other lifelines are disbanded!")
  time.sleep(2.5)
  if fiftyUsed == True:
    print("You have already used the 50-50 lifeline! You will have to either answer or quit!")
    fifteenth()
  elif fiftyUsed == False:
    hello = input("Do you want to use the 50-50 lifeline (y/n)?").lower()
    if hello == "y":
      fifty_fifty(lostAmt, winAmt, quitAmt, firstOp, secondOp, rightOp, rightAns, time_limit, qno)
    else:
      winsound.PlaySound("sounds/10000000ques.wav", winsound.SND_LOOP + winsound.SND_ASYNC)
      hello2 = input("Okay! Please enter your answer or quit! ").lower()
      check_ans(hello2, winAmt, lostAmt, quitAmt, rightAns, firstOp, secondOp, rightOp, time_limit, qno)
def check_ans(input, winAmt, lostAmt, quitAmt, rightAns, firstOp, secondOp, rightOp, time_limit, qno):
  if qno > 5 and qno != 5 and qno != 15:
    if input == rightAns or input == rightAns.upper():
      winsound.PlaySound("sounds/" + str(winAmt) + "final.wav", winsound.SND_FILENAME)
      print(f"Correct Answer! You win Rs {winAmt}")
      winsound.PlaySound("sounds/" + str(winAmt) + "win" + ".wav", winsound.SND_FILENAME)
    elif input == "quit":
      quit(winAmt, lostAmt, quitAmt, rightAns, firstOp, secondOp, rightOp, time_limit, qno)
    elif input == "lifeline":
      useLifeline(input, lostAmt, winAmt, quitAmt, rightAns, firstOp, secondOp, rightOp, time_limit, qno)
    else:
      winsound.PlaySound("sounds/" + str(winAmt) + "final.wav", winsound.SND_FILENAME)
      wrong(rightOp, winAmt, lostAmt, qno)
  elif qno < 5:
    if input == rightAns:
      winsound.PlaySound("sounds/correct-answer_1.wav", winsound.SND_FILENAME)
      time.sleep(1.5)
      print(f"Correct Answer! You win Rs {winAmt}")
      time.sleep(2)
    elif input == "quit":
      quit(winAmt, lostAmt, quitAmt, rightAns, firstOp, secondOp, rightOp, time_limit, qno)
    elif input == "lifeline":
      useLifeline(input, lostAmt, winAmt, quitAmt, rightAns, firstOp, secondOp, rightOp, time_limit, qno)
    else:
      wrong(rightOp, winAmt, lostAmt, qno)
  elif qno == 5:
      if input == rightAns:
        winsound.PlaySound("sounds/locknew_1.wav", winsound.SND_FILENAME)
        print(f"Correct Answer! You win Rs {winAmt}")
        winsound.PlaySound("sounds/stage1correct.wav", winsound.SND_FILENAME)
      elif input == "quit":
        quit(winAmt, lostAmt, quitAmt, rightAns, firstOp, secondOp, rightOp, time_limit, qno)
      elif input == "lifeline":
        useLifeline(input, lostAmt, winAmt, quitAmt, rightAns, firstOp, secondOp, rightOp, time_limit, qno)
      else:
        winsound.PlaySound("sounds/" + str(winAmt) + "final.wav", winsound.SND_FILENAME)
        wrong(rightOp, winAmt, lostAmt, qno)
  elif qno == 10:
      if input == rightAns or input == rightAns.upper():
        winsound.PlaySound("sounds/320000final.wav", winsound.SND_FILENAME)
        print(f"Correct Answer! You win Rs {winAmt}")
        winsound.PlaySound("sounds/320000win.wav", winsound.SND_FILENAME)
      elif input == "quit":
        quit(winAmt, lostAmt, quitAmt, rightAns, firstOp, secondOp, rightOp, time_limit, qno)
      elif input == "lifeline":
        useLifeline(input, lostAmt, winAmt, quitAmt, rightAns, firstOp, secondOp, rightOp, time_limit, qno)
      else:
        winsound.PlaySound("sounds/" + str(winAmt) + "final.wav", winsound.SND_FILENAME)
        wrong(rightOp, winAmt, lostAmt, qno)
  elif qno == 15:
      if input == rightAns:
        winsound.PlaySound("sounds/10000000final.wav", winsound.SND_FILENAME)
        print(f"Correct Answer! You win Rs {winAmt}")
        time.sleep(1)
        winsound.PlaySound("sounds/10000000win.wav", winsound.SND_FILENAME)
        print("Excellent! You have become a crorepati!")
        time.sleep(2)
        print("Congratulations! You have won the bumper prize! Very Well played! I am intrigued by your knowledge!")
        cheque(winAmt)
        time.sleep(2)
        print("Thank you for playing!")
        winsound.PlaySound("sounds/closing.wav", winsound.SND_FILENAME)
      elif input == "quit":
        winsound.PlaySound("sounds/ping.wav", winsound.SND_FILENAME)
        print("Wise decision! It is only safe to quit at this point if you aren't sure!")
        time.sleep(1.5)
        print(f"Thank you for playing! You win Rs {quitAmt}")
        time.sleep(1.5)
        print(f"The correct answer is {rightOp}")
        cheque(quitAmt)
        time.sleep(2)
        print("We will take your leave now!")
        winsound.PlaySound("sounds/closing.wav", winsound.SND_FILENAME)
      elif input == "lifeline":
        useLifeline_2(lostAmt, winAmt, quitAmt, rightAns, firstOp, secondOp, rightOp, time_limit, qno)
      else:
        winsound.PlaySound("sounds/" + str(winAmt) + "final.wav", winsound.SND_FILENAME)
        print("Oh no! That's the wrong answer! You fall back to Rs 3,20,000!")
        winsound.PlaySound("sounds/10000000lose.wav", winsound.SND_FILENAME)
        time.sleep(2)
        print("You should have quit if you were not sure! I feel sad for you :-(")
        cheque(lostAmt)
        time.sleep(1)
        print("Nevertheless, you played really well! Thank you for playing!")
        winsound.PlaySound("sounds/closing.wav", winsound.SND_FILENAME)
        exit()
def first():
  winsound.PlaySound("sounds/1st.wav", winsound.SND_ASYNC + winsound.SND_LOOP)
  print("The 1st question for Rs 1000")
  time.sleep(1.5)
  print("On your screen!!")
  time.sleep(2)
  print("Who is the current President of India?")
  time.sleep(2)
  print("a)Narendra Modi b)Ram Nath Kovind c)Venkaiah Naidu d)Pranab Mukherjee")
  answer = inputtime("b)Ram Nath Kovind", 0, 5)
  check_ans(answer, 1000, 0, 0, "b", "b)Ram Nath Kovind", "c)Venkaiah Naidu", "b)Ram Nath Kovind", 45, 1)
first()
def second():
  winsound.PlaySound("sounds/1st.wav", winsound.SND_ASYNC + winsound.SND_LOOP)
  print("The 2nd question for Rs 2000")
  time.sleep(1.5)
  print("On your screen!!")
  time.sleep(2)
  print("What is the main ingredient in Lassi?")
  time.sleep(2)
  print("a)Dahi (curd) b)Milk c)Dal (Pulses) d)Cheese")
  answer = inputtime("a)Dahi(Curd)", 0, 45)
  check_ans(answer, 2000, 0, 1000, "a", "a)Dahi (curd)", "b)Milk", "a)Dahi (curd)", 45, 2)
second()
def third():
  winsound.PlaySound("sounds/1st.wav", winsound.SND_ASYNC + winsound.SND_LOOP)
  print("The 3rd question for Rs 3000")
  time.sleep(1.5)
  print("On your screen!")
  time.sleep(2)
  print("Where is the Motera stadium, which is the largest stadium, situated?")
  time.sleep(2)
  print("a)Delhi b)Mohali c)Ahmedabad d)Chennai")
  answer = inputtime("c)Ahmedabad", 0, 45)
  check_ans(answer, 3000, 0, 2000, "c", "c)Ahmedabad", "d)Chennai", "c)Ahmedabad", 45, 3)
third()
def fourth():
  winsound.PlaySound("sounds/1st.wav", winsound.SND_ASYNC + winsound.SND_LOOP)
  print("The 4th question for Rs 5000")
  time.sleep(1.5)
  print("On your screen!")
  time.sleep(2)
  print("Which of these films was the first Indian movie with sound and music?")
  time.sleep(2)
  print("a)Raja Harishchandra b)Alam Ara c)Shaheed d)Shree 420")
  answer = inputtime("b)Alam Ara", 0, 45)
  check_ans(answer, 5000, 0, 3000, "b", "a)Raja Harishchandra", "b)Alam Ara", "b)Alam Ara", 45, 4)
fourth()
def option5():
  time.sleep(1.5)
  print("a)Sardar Patel b)Maulana Abul Kalam c)Veer Savarkar d)Jawaharlal Nehru")
  winsound.PlaySound("sounds/timer.wav", winsound.SND_LOOP + winsound.SND_ASYNC)
  answer = inputtime("d)Jawaharlal Nehru", 0, 45)
  check_ans(answer, 10000, 0, 3000, "d", "a)Sardar Patel", "d)Jawaharlal Nehru", "d)Jawaharlal Nehru", 45, 5)
def fifth():
  winsound.PlaySound("sounds/1st.wav", winsound.SND_ASYNC + winsound.SND_LOOP)
  print("The 5th question for Rs 10,000")
  time.sleep(1.5)
  print("On your screen!!")
  time.sleep(2)
  print("Identify the renowned freedom fighter and politician in this audio clip")
  time.sleep(2)
  winsound.PlaySound("sounds/trystwithdestiny.wav", winsound.SND_FILENAME)
  repeat = input("Do you want to hear the audio again?(y/n) ").lower()
  if repeat == "y" or repeat == "Y":
    print("Playing audio...")
    winsound.PlaySound("sounds/trystwithdestiny.wav", winsound.SND_FILENAME)
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
  print("Which Enterprise is constructing the new Parliament building in India?")
  winsound.PlaySound("sounds/20000play.wav", winsound.SND_FILENAME)
  print("a)Adani Group b)Tata projects c)Larsen and Toubro d)GMR Projects")
  winsound.PlaySound("sounds/timer.wav", winsound.SND_LOOP + winsound.SND_ASYNC)
  inputtime("b)Tata Projects", 10000, 60)
  check_ans(answer, 20000, 10000, 10000, "b", "a)Adani Group", "b)Tata Projects", "b)Tata Projects", 60, 6)
sixth()
def seventh():
  time.sleep(2)
  print("The 8th question for Rs 80,000")
  time.sleep(1)
  print("On your screen!!")
  winsound.PlaySound("sounds/80000play.wav", winsound.SND_FILENAME)
  time.sleep(0.25)
  print("Who was the first person to get the Param Vir Chakra, the highest gallantry award of India?")
  time.sleep(1)
  print("a)Sam Manekshaw b)Somnath Sharma c)K.M. Cariappa d)Mohammed Usman")
  winsound.PlaySound("sounds/timer.wav", winsound.SND_LOOP + winsound.SND_ASYNC)
  inputtime("b)Somnath Sharma", 10000, 60)
  check_ans(answer, 80000, 10000, 40000, "b", "b)Somnath Sharma", "c)K.M. Cariappa", "b)Somnath Sharma", 60, 7)
seventh()
def eighth():
  time.sleep(2)
  print("The 9th question for Rs 1,60,000")
  time.sleep(1)
  print("On your screen!!")
  winsound.PlaySound("sounds/160000play.wav", winsound.SND_FILENAME)
  time.sleep(0.25)
  print("Which salty lake located at the lowest point of Earth has such high density  that makes it impossible for people to sink?")
  time.sleep(1)
  print("a)Dead sea b)Lake Baikal c)Caspian Sea d)Vembanad Lake")
  winsound.PlaySound("sounds/timer.wav", winsound.SND_LOOP + winsound.SND_ASYNC)
  inputtime("a)Dead Sea", 10000, 60)
  check_ans(answer, 160000, 10000, 80000, "a", "a)Dead Sea", "c)Caspian Sea", "a)Dead Sea", 60, 8)
eighth()
def ninth():
  time.sleep(2)
  print("The 10th question for Rs 3,20,000")
  time.sleep(1)
  print("On your screen!!")
  winsound.PlaySound("sounds/320000play.wav", winsound.SND_FILENAME)
  time.sleep(0.25)
  print("Roger Penrose was awarded the Nobel Prize in Physics for his work in which of the following fields?")
  time.sleep(1)
  print("a)Black Holes b)Quantum Theory c)Electronics d)Structure of atoms")
  winsound.PlaySound("sounds/timer.wav", winsound.SND_LOOP + winsound.SND_ASYNC)
  inputtime("a)Black Holes", 10000, 60)
  check_ans(answer, 320000, 10000, 160000, "a", "a)Black Holes", "b)Quantum Theory", "a)Black Holes", 60, 9)
ninth()
def tenth():
  time.sleep(2)
  print("The 7th question for Rs 40,000")
  time.sleep(1)
  print("On your screen!!")
  winsound.PlaySound("sounds/40000play.wav", winsound.SND_FILENAME)
  time.sleep(1)
  print("The person shown in this picture attacked which country, a decision that was made due to his country's policy of containing communism")
  time.sleep(3)
  image = cv.imread("lbj.jpg")
  cv.imshow("Press any key to exit", image)
  cv.waitKey(0)
  cv.destroyAllWindows()
  print("a)Korea b)Lebanon c)Vietnam d)Cuba")
  winsound.PlaySound("sounds/timer.wav", winsound.SND_LOOP + winsound.SND_ASYNC)
  inputtime("c)Vietnam", 10000, 60)
  check_ans(answer, 40000, 10000, 20000, "a", "c)Vietnam", "d)Cuba", "c)Vietnam", 60, 10)
tenth()
print("Congratulations, You have successfully passed the 2nd stage! Now you will take at least Rs 3,20,000 from here")
time.sleep(3.5)
print("Now there is no time limit on the questions, You can take as much time as you want!")
time.sleep(2.5)
print("The questions are slowly going to get difficult, so play wisely and quit if you feel so!")
time.sleep(2)
print("Good Luck!")
time.sleep(1)
def eleventh():
  time.sleep(2)
  print("The 11th question for Rs 6,40,000")
  time.sleep(1)
  print("On your screen!!")
  winsound.PlaySound("sounds/640000play.wav", winsound.SND_FILENAME)
  time.sleep(0.25)
  print("What was the name of the rover which was sent along with Chandrayaan-2 to the moon?")
  time.sleep(1)
  winsound.PlaySound("sounds/640000ques.wav", winsound.SND_LOOP + winsound.SND_ASYNC)
  print("a)Vigyan b)Abhigyaan c)Pragyan d)Vikram")
  input11 = input("Enter your Answer ").lower()
  check_ans(input11, 640000, 320000, 320000, "c", "b)Abhigyaan", "c)Pragyan", "c)Pragyan", None, 11)
eleventh()
def twelfth():
  time.sleep(2)
  print("The 12th question for Rs 12,50,000")
  time.sleep(1)
  print("On your screen!!")
  winsound.PlaySound("sounds/1250000play.wav", winsound.SND_FILENAME)
  time.sleep(0.25)
  print("According to Hindu Mythology, who was burned by Lord Shiva's gaze when he tried to disturb his tapasya (meditation)?")
  time.sleep(1)
  print("a)Ganesha b)Indra c)Kama d)Vayu")
  winsound.PlaySound("sounds/1250000ques.wav", winsound.SND_LOOP + winsound.SND_ASYNC)
  input12 = input("Enter your Answer ").lower()
  check_ans(input12, 1250000, 320000, 640000, "c", "b)Indra", "c)Kama", "c)Kama", None, 12)
twelfth()
def thirteenth():
  time.sleep(2)
  print("The 13th question for Rs 25,00,000")
  time.sleep(1)
  print("On your screen!!")
  winsound.PlaySound("sounds/2500000play.wav", winsound.SND_FILENAME)
  time.sleep(0.25)
  print("When was the Ashes first played?")
  time.sleep(1)
  print("a)1923 b)1850 c)1872 d)1885")
  winsound.PlaySound("sounds/1250000ques.wav", winsound.SND_LOOP + winsound.SND_ASYNC)
  input13 = input("Enter your Answer ").lower()
  check_ans(input13, 2500000, 320000, 1250000, "c", "c)1872", "d)1885", "c)1872", None, 13)
thirteenth()
def fourteenth():
  time.sleep(2)
  print("The 14th question for Rs 50,00,000")
  time.sleep(1)
  print("On your screen!!")
  winsound.PlaySound("sounds/5000000play.wav", winsound.SND_FILENAME)
  time.sleep(0.25)
  print("Which of these former presidents of Indiarferferre")
  time.sleep(1)
  print("a)Indian Insitute of Science b)IIT Kharagpur c)Jawaharlal Nehru University D)NIT Trichy")
  winsound.PlaySound("sounds/5000000ques.wav", winsound.SND_LOOP + winsound.SND_ASYNC)
  input14 = input("Enter your Answer ").lower()
  check_ans(input14, 5000000, 320000, 2500000, "b", "b)IIT Kharagpur", "c)Jawaharlal Nehru University", "b)IIT Kharagpur", None, 14)
fourteenth()
print("You are playing excellent! Now get ready for the last question of the game!")
time.sleep(3.5)
print("The 15th question for Rs 1,00,00,000")
time.sleep(1)
print("On your screen!!")
winsound.PlaySound("sounds/10000000play.wav", winsound.SND_FILENAME)
time.sleep(0.25)
print("Which case was heard by the largest ever constitution bench of 13 Supreme Court judges?")
time.sleep(1)
print("a)Golaknath case b)Ashok Kumar case c)Shah Bano case d)Kesavananda Bharati Case.")
def fifteenth():
  winsound.PlaySound("sounds/10000000ques.wav", winsound.SND_LOOP + winsound.SND_ASYNC)
  input15 = input("Enter your Answer ").lower()
  confirm = input("Are you sure?(y/n) ").lower()
  if confirm == "y":
    check_ans(input15, 10000000, 320000, 5000000, "d", "c)Shah Bano case", "d)Kesavananda Bharati Case", "d)Kesavananda Bharati Case", None, 15)
  else:
    fifteenth()
fifteenth()