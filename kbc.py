# Welcome, here are the guidelines if you need them again
# lifeline - to use lifeline
# quit - to quit the game
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
# Game begins
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
print("\nIf you feel the correct answer is option 'a', then just input 'a' when prompted (Not case-sensitive)")
time.sleep(3.5)
print("Before starting the game, we would like to know your name")
time.sleep(1.5)
global name
name = input("Please enter your name! ")
# global variable for storing the answer
global answer
answer = None
print("Thanks for entering!")
time.sleep(1.5)
print("So let's start the game!")
time.sleep(2)
# The functions to carry out various stuff
def cheque(amt):
  # displaying the cheque
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
  # controls output if time limit elapses in a particular question
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
def inputtime(rightOp, lostAmt, time_limit):
  # Controls the input for the first 10 questions
  def input_thread():
    input_queue.put(input("Enter your answer ").lower())
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
  # Controls the output if a person chooses to quit
  winsound.PlaySound("sounds/ping.wav", winsound.SND_FILENAME)
  if qno == 6:
    print("I will not let you quit at this point! You will not lose anything even if you get the question wrong!")
    time.sleep(2)
    answer = inputtime(rightOp, 0, 45)
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
        answer = inputtime(rightOp, 0, time_limit)
        check_ans(answer, winAmt, lostAmt, quitAmt, rightAns, firstOp, secondOp, rightOp, time_limit, qno)
def wrong(correctAns, winAmt, lostAmt, qno):
  # Output if answer is wrong
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
  # Code for Ask the expert lifeline
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
    answer = inputtime(rightOp, lostAmt, time_limit)
    check_ans(answer, winAmt, lostAmt, quitAmt, rightAns, firstOp, secondOp, rightOp, time_limit, qno)
  else:
    winsound.PlaySound("sounds/" + str(winAmt) + "ques.wav", winsound.SND_LOOP + winsound.SND_ASYNC)
    user_input = input("Enter your answer ").lower()
    check_ans(user_input, winAmt, lostAmt, quitAmt, rightAns, firstOp, secondOp, rightOp, time_limit, qno)
def flip(winAmt, lostAmt, quitAmt, rightOp, rightAns, time_limit, qno):
  # Code for flip the question lifeline
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
    answer = inputtime("a)दुम", 0, 45)
    check_ans(answer, winAmt, lostAmt, quitAmt, "a", "a)दुम", "c)हाथ", "a)दुम", time_limit, qno)
  elif qno > 5 and qno <= 10:
    winsound.PlaySound("sounds/question.wav", winsound.SND_FILENAME)
    print("To which group of sportspersons is the Dronacharya Award given?")
    time.sleep(2)
    print("a)Players b)Support Staff c)Administrators d)Coaches")
    winsound.PlaySound("sounds/timer.wav", winsound.SND_LOOP + winsound.SND_ASYNC)
    answer = inputtime("a)Coaches", 10000, 60)
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
  # Code for 50-50 lifeline
  global fiftyUsed
  fiftyUsed = True
  if qno < 11:
    time.sleep(2)
    winsound.PlaySound("sounds/fifty2.wav", winsound.SND_FILENAME)
    print(f"Two options are left {firstOp} and {secondOp}")
    winsound.PlaySound("sounds/timer.wav", winsound.SND_LOOP + winsound.SND_ASYNC)
    answer = inputtime(rightOp, lostAmt, time_limit)
    check_ans(answer, winAmt, lostAmt, quitAmt, rightAns, firstOp, secondOp, rightOp, time_limit, qno)
  else:
    time.sleep(2)
    winsound.PlaySound("sounds/fifty2.wav", winsound.SND_FILENAME)
    print(f"Two options are left {firstOp} and {secondOp}")
    winsound.PlaySound("sounds/" + str(winAmt) + "ques.wav", winsound.SND_LOOP + winsound.SND_ASYNC) 
    userAns = input("Enter your answer! ").lower()
    check_ans(userAns, winAmt, lostAmt, quitAmt, rightAns, firstOp, secondOp, rightOp, time_limit, qno)
def audience_poll(lostAmt, winAmt, quitAmt, firstOp, secondOp, rightOp, rightAns, time_limit, qno, a_percent, b_percent, c_percent, d_percent):
  # Code for audience poll lifeline
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
    answer = inputtime(rightOp, lostAmt, time_limit)
    check_ans(answer, winAmt, lostAmt, quitAmt, rightAns, firstOp, secondOp, rightOp, time_limit, qno)
  else:
    winsound.PlaySound("sounds/" + str(winAmt) + "ques.wav", winsound.SND_LOOP + winsound.SND_ASYNC)
    ap_input = input("Enter Your answer ").lower()
    check_ans(ap_input, winAmt, lostAmt, quitAmt, rightAns, firstOp, secondOp, rightOp, time_limit, qno)
def useLifeline(ll_input, lostAmt, winAmt, quitAmt, rightAns, firstOp, secondOp, rightOp, time_limit, qno):
  # Long code that controls the output if a person takes help of a lifeline
  winsound.PlaySound("sounds/ping.wav", winsound.SND_FILENAME)
  if fiftyUsed == True and apUsed == True and ateUsed == True and flipUsed == True:
    if qno > 10:
      print("You have used all the lifelines. Please choose another option")
      winsound.PlaySound("sounds/" + str(winAmt) + "ques.wav", winsound.SND_LOOP + winsound.SND_ASYNC)
      all_lfl_used = input("You can either quit or try to answer ").lower()
      check_ans(all_lfl_used, winAmt, lostAmt, quitAmt, rightAns, firstOp, secondOp, rightOp, time_limit, qno)
    else:
      print("You have used all the lifelines. You can either quit or try to answer")
      time.sleep(2.5)
      answer = inputtime(rightOp, lostAmt, time_limit)
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
          answer = inputtime(rightOp, lostAmt, time_limit)
          check_ans(answer, winAmt, lostAmt, quitAmt, rightAns, firstOp, secondOp, rightOp, time_limit, qno)
        else:
          winsound.PlaySound("sounds/" + str(winAmt) + "ques.wav", winsound.SND_LOOP + winsound.SND_ASYNC)
          lfl_input = input("Enter Your answer ").lower()
          check_ans(lfl_input, winAmt, lostAmt, quitAmt, rightAns, firstOp, secondOp, rightOp, time_limit, qno)
def check_ans(user_input, winAmt, lostAmt, quitAmt, rightAns, firstOp, secondOp, rightOp, time_limit, qno):
  # Checks the user input
  if qno > 5 and qno != 5 and qno != 15:
    if user_input == rightAns or user_input == rightAns.upper():
      winsound.PlaySound("sounds/" + str(winAmt) + "final.wav", winsound.SND_FILENAME)
      print(f"Correct Answer! You win Rs {winAmt}")
      winsound.PlaySound("sounds/" + str(winAmt) + "win" + ".wav", winsound.SND_FILENAME)
    elif user_input == "quit":
      quit(winAmt, lostAmt, quitAmt, rightAns, firstOp, secondOp, rightOp, time_limit, qno)
    elif user_input == "lifeline":
      useLifeline(user_input, lostAmt, winAmt, quitAmt, rightAns, firstOp, secondOp, rightOp, time_limit, qno)
    else:
      winsound.PlaySound("sounds/" + str(winAmt) + "final.wav", winsound.SND_FILENAME)
      wrong(rightOp, winAmt, lostAmt, qno)
  elif qno < 5:
    if user_input == rightAns:
      winsound.PlaySound("sounds/correct-answer_1.wav", winsound.SND_FILENAME)
      time.sleep(1.5)
      print(f"Correct Answer! You win Rs {winAmt}")
      time.sleep(2)
    elif user_input == "quit":
      quit(winAmt, lostAmt, quitAmt, rightAns, firstOp, secondOp, rightOp, time_limit, qno)
    elif user_input == "lifeline":
      useLifeline(user_input, lostAmt, winAmt, quitAmt, rightAns, firstOp, secondOp, rightOp, time_limit, qno)
    else:
      wrong(rightOp, winAmt, lostAmt, qno)
  elif qno == 5:
      if user_input == rightAns:
        winsound.PlaySound("sounds/locknew_1.wav", winsound.SND_FILENAME)
        print(f"Correct Answer! You win Rs {winAmt}")
        winsound.PlaySound("sounds/stage1correct.wav", winsound.SND_FILENAME)
        print("Congratulations, you have passed the first stage! Now you will take at least Rs 10000 from here!")
        time.sleep(2)
        print("Now you will get 60 seconds to answer the questions")
      elif user_input == "quit":
        quit(winAmt, lostAmt, quitAmt, rightAns, firstOp, secondOp, rightOp, time_limit, qno)
      elif user_input == "lifeline":
        useLifeline(user_input, lostAmt, winAmt, quitAmt, rightAns, firstOp, secondOp, rightOp, time_limit, qno)
      else:
        winsound.PlaySound("sounds/" + str(winAmt) + "final.wav", winsound.SND_FILENAME)
        wrong(rightOp, winAmt, lostAmt, qno)
  elif qno == 10:
      if user_input == rightAns or user_input == rightAns.upper():
        winsound.PlaySound("sounds/320000final.wav", winsound.SND_FILENAME)
        print(f"Correct Answer! You win Rs {winAmt}")
        winsound.PlaySound("sounds/320000win.wav", winsound.SND_FILENAME)
        print("Congratulations, You have successfully passed the 2nd stage! Now you will take at least Rs 3,20,000 from here")
        time.sleep(3.5)
        print("Now there is no time limit on the questions, You can take as much time as you want!")
        time.sleep(2.5)
        print("The questions are slowly going to get difficult, so play wisely and quit if you feel so!")
        time.sleep(2)
        print("Good Luck!")
        time.sleep(1)
      elif user_input == "quit":
        quit(winAmt, lostAmt, quitAmt, rightAns, firstOp, secondOp, rightOp, time_limit, qno)
      elif user_input == "lifeline":
        useLifeline(user_input, lostAmt, winAmt, quitAmt, rightAns, firstOp, secondOp, rightOp, time_limit, qno)
      else:
        winsound.PlaySound("sounds/" + str(winAmt) + "final.wav", winsound.SND_FILENAME)
        wrong(rightOp, winAmt, lostAmt, qno)
  elif qno == 15:
      if user_input == rightAns:
        winsound.PlaySound("sounds/10000000final.wav", winsound.SND_FILENAME)
        print(f"Correct Answer! You win Rs {winAmt}")
        print("EXCELLENT! You have become a crorepati!")
        time.sleep(1)
        winsound.PlaySound("sounds/10000000win.wav", winsound.SND_FILENAME)
        time.sleep(2)
      elif user_input == "quit":
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
      elif user_input == "lifeline":
        useLifeline(user_input, lostAmt, winAmt, quitAmt, rightAns, firstOp, secondOp, rightOp, time_limit, qno)
      else:
        winsound.PlaySound("sounds/" + str(winAmt) + "final.wav", winsound.SND_FILENAME)
        print("Oh no! That's the wrong answer! You fall back to Rs 3,20,000!")
        winsound.PlaySound("sounds/10000000lose.wav", winsound.SND_FILENAME)
        time.sleep(2)
        print("You should have quit if you were not sure! I feel sad for you :-(")
        print("Here's your cheque")
        cheque(lostAmt)
        time.sleep(1)
        print("Nevertheless, you played really well! Thank you for playing!")
        winsound.PlaySound("sounds/closing.wav", winsound.SND_FILENAME)
        exit()
  elif qno == 16:
    if user_input == rightAns:
      winsound.PlaySound("sounds/10000000final.wav", winsound.SND_FILENAME)
      print(f"EXCELLENT EXCELLENT EXCELLENT!!")
      print("YOU HAVE WON RS 7 CRORES!!")
      time.sleep(1)
      winsound.PlaySound("sounds/10000000win.wav", winsound.SND_FILENAME)
      time.sleep(2)
      print("Unbelievable! You have played exceptionally well!")
      time.sleep(1.5)
      print("Congratulations! You have won the bumper prize! Very Well played! I am intrigued by your knowledge!")
      cheque(winAmt)
      time.sleep(2)
      print("We will take your leave now!")
      winsound.PlaySound("sounds/closing.wav", winsound.SND_FILENAME)
      exit()
    elif user_input == "quit":
      winsound.PlaySound("sounds/ping.wav", winsound.SND_FILENAME)
      print("Wise decision! It is only safe to quit at this point if you aren't sure!")
      time.sleep(1.5)
      print(f"Thank you for playing! You win Rs {quitAmt}")
      time.sleep(1.5)
      print(f"The correct answer is {rightOp}")
      print("Here's your cheque")
      time.sleep(1)
      cheque(quitAmt)
      time.sleep(2)
      print("We will take your leave now!")
      winsound.PlaySound("sounds/closing.wav", winsound.SND_FILENAME)
    elif user_input == "lifeline":
      print("All the lifelines are disbanded!")
      answer = input("Enter the answer ").lower()
      check_ans(answer, winAmt, lostAmt, quitAmt, rightAns, firstOp, secondOp, rightOp, time_limit, qno)
    else:
      winsound.PlaySound("sounds/" + str(winAmt) + "final.wav", winsound.SND_FILENAME)
      print("Oh no! That's the wrong answer! You fall back to Rs 3,20,000!")
      winsound.PlaySound("sounds/10000000lose.wav", winsound.SND_FILENAME)
      print(f"The right answer is {rightOp}!")
      time.sleep(2)
      print("You should have quit if you were not sure! I feel sad for you :-(")
      print("Here's your cheque")
      time.sleep(1)
      cheque(lostAmt)
      time.sleep(1)
      print("Nevertheless, you played really well! Thank you for playing!")
      winsound.PlaySound("sounds/closing.wav", winsound.SND_FILENAME)
# The questions start from here!
def questions(ques, options, winAmt, lostAmt, quitAmt, rightAns, firstOp, secondOp, rightOp, time_limit, qno):
  ques_position = num2words(qno, to='ordinal')
  print(f"The {ques_position} question for Rs {winAmt}")
  time.sleep(1.5)
  print("On your screen!!")
  time.sleep(2)
  print(ques)
  time.sleep(2)
  if qno <= 5:
    winsound.PlaySound("sounds/1st.wav", winsound.SND_ASYNC + winsound.SND_LOOP)
    print(options)
    answer = inputtime(rightOp, lostAmt, time_limit)
    check_ans(answer, winAmt, lostAmt, quitAmt, rightAns, firstOp, secondOp, rightOp, time_limit, qno)
  elif qno == 10:
    winsound.Playsound(f"sounds/{winAmt}play.wav", winsound.SND_FILENAME)
    print(options)
    time.sleep(3)
    image = cv.imread("lbj.jpg")
    cv.imshow("Press any key to exit", image)
    cv.waitKey(0)
    cv.destroyAllWindows()
    answer = inputtime(rightOp, lostAmt, time_limit)
    check_ans(answer, winAmt, lostAmt, quitAmt, rightAns, firstOp, secondOp, rightOp, time_limit, qno)
  elif qno == 15:
    winsound.Playsound(f"sounds/{winAmt}play.wav", winsound.SND_FILENAME)
    print(options)
    winsound.PlaySound(f"sounds/{winAmt}ques.wav", winsound.SND_ASYNC + winsound.SND_LOOP)
    def answer15():
      answer = input("Enter your answer ").lower()
      confirm = input("Are you sure? (y/n)").lower()
      if confirm == "y":
        check_ans(answer, winAmt, lostAmt, quitAmt, rightAns, firstOp, secondOp, rightOp, time_limit, qno)
      else:
        answer15()
  elif qno < 11:
    winsound.Playsound(f"sounds/{winAmt}play.wav", winsound.SND_FILENAME)
    print(options)
    winsound.PlaySound(f"sounds/{winAmt}ques.wav", winsound.SND_ASYNC + winsound.SND_LOOP)
    answer = inputtime(rightOp, lostAmt, time_limit)
    check_ans(answer, winAmt, lostAmt, quitAmt, rightAns, firstOp, secondOp, rightOp, time_limit, qno)
  else:
    winsound.Playsound(f"sounds/{winAmt}play.wav", winsound.SND_FILENAME)
    print(options)
    winsound.PlaySound(f"sounds/{winAmt}ques.wav", winsound.SND_ASYNC + winsound.SND_LOOP)
    answer = input("Enter your answer ")
    check_ans(answer, winAmt, lostAmt, quitAmt, rightAns, firstOp, secondOp, rightOp, time_limit, qno)
questions("Who is the current President of India?", "a)Draupadi Murmu b)Ram Nath Kovind c)Venkaiah Naidu d)Pranab Mukherjee", 1000, 0, 0, "a", "a)Draupadi Murmu", "c)Venkaiah Naidu", "a)Draupadi Murmu", 45, 1)
questions("What is the main ingredient in Lassi?", "a)Dahi (curd) b)Milk c)Dal (Pulses) d)Cheese", 2000, 0, 1000, "a", "a)Dahi (curd)", "b)Milk", "a)Dahi (curd)", 45, 2)
questions("Where is the Motera stadium, which is the largest stadium, situated?", "a)Delhi b)Mohali c)Ahmedabad d)Chennai",3000, 0, 2000, "c", "c)Ahmedabad", "d)Chennai", "c)Ahmedabad", 45, 3)
questions("Which of these films was the first Indian movie with sound and music?", "a)Raja Harishchandra b)Alam Ara c)Shaheed d)Shree 420", 5000, 0, 3000, "b", "a)Raja Harishchandra", "b)Alam Ara", "b)Alam Ara", 45, 4)
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
questions("Which Enterprise is constructing the new Parliament building in India?", "a)Adani Group b)Tata projects c)Larsen and Toubro d)GMR Projects", 20000, 10000, 10000, "b", "a)Adani Group", "b)Tata Projects", "b)Tata Projects", 60, 6)
questions("Who was the first person to get the Param Vir Chakra, the highest gallantry award of India?", "a)Sam Manekshaw b)Somnath Sharma c)K.M. Cariappa d)Mohammed Usman", 40000, 10000, 20000, "b", "b)Somnath Sharma", "c)K.M. Cariappa", "b)Somnath Sharma", 60, 7)
questions("Which salty lake located at the lowest point of Earth has such high density  that makes it impossible for people to sink?", "a)Dead sea b)Lake Baikal c)Caspian Sea d)Vembanad Lake", 80000, 10000, 40000, "a", "a)Dead Sea", "c)Caspian Sea", "a)Dead Sea", 60, 8)
questions("Roger Penrose was awarded the Nobel Prize in Physics for his work in which of the following fields?", "a)Black Holes b)Quantum Theory c)Electronics d)Structure of atoms", 160000, 10000, 80000, "a", "a)Black Holes", "b)Quantum Theory", "a)Black Holes", 60, 9)
questions("The person shown in this picture was the former president of which country?", "a)Australia b)United States of America c)France d)Canada", 320000, 10000, 160000, "b", "b)United States of America", "d)Canada", "b)United States of America", 60, 10)
questions("What was the name of the rover which was sent along with Chandrayaan-2 to the moon?", "a)Vigyan b)Abhigyaan c)Pragyan d)Vikram", 640000, 320000, 320000, "c", "b)Abhigyaan", "c)Pragyan", "c)Pragyan", None, 11)
questions("According to Hindu Mythology, who was burned by Lord Shiva's gaze when he tried to disturb his tapasya (meditation)?", "a)Ganesha b)Indra c)Kama d)Vayu", 1250000, 320000, 640000, "c", "b)Indra", "c)Kama", "c)Kama", None, 12)
questions("Around 300 Indian soldiers were also evacuated as part of Operation Dynamo by the Allies in World War II, from which place in the north of France?", "a)Dunkirk b)Normandy c)Calais d)Lyon", 2500000, 320000, 1250000, "a", "a)Dunkirk", "b)Normandy", "a)Dunkirk", None, 13)
questions("Which of these institutes maintains the National Digital Library of India?", "a)Indian Insitute of Science b)IIT Kharagpur c)Jawaharlal Nehru University D)NIT Trichy", 5000000, 320000, 2500000, "b", "b)IIT Kharagpur", "c)Jawaharlal Nehru University", "b)IIT Kharagpur", None, 1)
print("You are playing excellent! Now get ready for the 15th question of the game!")
time.sleep(3.5)
questions("Which case was heard by the largest ever constitution bench of 13 Supreme Court judges?", "a)Golaknath case b)Ashok Kumar case c)Shah Bano case d)Kesavananda Bharati Case", 10000000, 320000, 5000000, "d", "c)Shah Bano case", "d)Kesavananda Bharati Case", "d)Kesavananda Bharati Case", None, 15)
def sixteenth():
  print(f"Mr. {name}...")
  time.sleep(1)
  print("Not many people reach till this stage of the game...")
  time.sleep(2.5)
  print("But you have reached here with your knowledge.")
  time.sleep(0.5)
  print("Now get ready for the last question of the game...")
  time.sleep(3)
  print("Please note that you can't use any of your lifelines in this question.")
  time.sleep(2.5)
  print("Get ready..")
  time.sleep(2.5)
  print("The 16th question..")
  time.sleep(1)
  print("For Rs. 7 crores...")
  time.sleep(2.5)
  print("On your screen!!!")
  winsound.PlaySound("sounds/10000000play.wav", winsound.SND_FILENAME)
  print("Which is the only bird with a digestive system that ferments vegetation as a bovine does, which enables it to eat leaves and buds exclusively?")
  winsound.PlaySound("sounds/10000000ques.wav", winsound.SND_LOOP + winsound.SND_ASYNC)
  time.sleep(1)
  print("a)Shoebill stork b)Hoatzin c)Shoveler, d)Galapagos cormoran")
  def confirm():
    answer = input("Enter your answer ").lower()  
    confirm16 = input("Are you sure?(y/n) ").lower()
    if confirm16 == "y":
      check_ans(answer, 70000000, 320000, 10000000, "d", "c)Shah Bano case", "d)Kesavananda Bharati Case", "d)Kesavananda Bharati Case", None, 15)
    else:
      confirm()
sixteenth()