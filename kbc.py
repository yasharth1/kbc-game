# Welcome, here are the guideline if you need them again
# lifeline - to use lifeline
# quit - to quit
from threading import Timer
import pyttsx3
import winsound
import time
import matplotlib.pyplot as plt
import cv2 as cv
fiftyUsed = False
flipUsed = False
apUsed = False
ateUsed = False
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)
def speak(audio):
  engine.say(audio)
  engine.runAndWait()
def inputtime(rightOp, lostAmt, time_limit):
  t = Timer(time_limit, print, [f'Time up!!The correct answer is {rightOp}! You fall back to {lostAmt}'], winsound.PlaySound("sounds/timer.wav", winsound.SND_LOOP + winsound.SND_ASYNC))
  t.start()
  global answer
  answer = input("Enter your answer ").lower()
  t.cancel()
def quit(quitAmt, rightAns, rightOp):
  if quitAmt == 10000:
    print("I will not let you quit at this point! You will not lose anything even if you get the question wrong!")
    time.sleep(2)
    inputtime(rightOp, 0, 45)
    check_ans(answer, 20000, 10000, 10000, rightAns, "a)Sardar Patel", "d)Jawaharlal Nehru", rightOp, 45, 5)
  elif quitAmt == 320000:
    print("I will not let you quit at this point! You will not lose anything even if you get the question wrong!")
    time.sleep(2)
    winsound.PlaySound("sounds/640000ques.wav", winsound.SND_FILENAME)
    input("Enter Your answer ").lower()
    check_ans(answer, 640000, 320000, 320000, rightAns, "a)Raja Harishchandra", "b)Alam Ara", rightOp, 45, 5)
  else:
    confirm = input("Are you sure you want to quit?(y/n) ").lower()
    if confirm == "y":
      print(f"Thank you for playing! You won Rs {quitAmt}!")
      time.sleep(2)
      print(f"The correct answer is {rightOp}")
      time.sleep(2)
      print("We will take your leave now!")
      winsound.PlaySound("sounds/closing.wav", winsound.SND_FILENAME)
      exit()
    elif confirm == "n":
      print("Okay, let's continue the game!")
      time.sleep(2)
      input("Enter your answer ").lower()
def wrong(correctAns, winAmt, lostAmt, qno):
  if qno > 5:
    print(f"Wrong answer! The correct answer is {correctAns}! You fall back to Rs {lostAmt}")
    winsound.PlaySound("sounds/" + str(winAmt) + "lose.wav", winsound.SND_FILENAME)
    print("Thank you for playing the game! You played really well!")
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
    user_input = input("Enter your answer ").lower()
    winsound.PlaySound("sounds/" + str(winAmt) + "ques.wav", winsound.SND_LOOP + winsound.SND_ASYNC)
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
    print("Your answer would have been wrong! Thank God you took a lifeline! Correct answr is " + rightOp)
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
    inputtime("a)Coaches", 10000, 60)
    winsound.PlaySound("sounds/timer.wav", winsound.SND_LOOP + winsound.SND_ASYNC)
    check_ans(answer, winAmt, lostAmt, quitAmt, "d", "d)Support Staff", "d)Coaches", "d)Coaches", time_limit, qno)
  elif qno > 10:
    winsound.PlaySound("sounds/" + str(winAmt) + "play.wav", winsound.SND_FILENAME)
    print("When the Lucknow pact was adopted in 1916 Mohammad Ali Jinnah represented the Muslim League, who represented the Indian National Congress?")
    time.sleep(1.5)
    print("a)Mahatma Gandhi b)Lokmanya Tilak c)Motilal Nehru d)Sardar Vallabhbhai Patel")
    flip_3 = input("Enter your answer ").lower()
    winsound.PlaySound("sounds/" + str(winAmt) + "ques.wav", winsound.SND_LOOP + winsound.SND_ASYNC)
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
      lifeline = input("What lifeline do you want to use? Type ff' for 50-50, 'flip' for flip the question, 'ate' for ask the expert and 'ap' for audience poll  ").lower()
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
        if hello == "y" or hello == "Y":
            useLifeline(ll_input, lostAmt, winAmt, quitAmt, rightAns, firstOp, secondOp, rightOp, time_limit, qno)
        elif hello == "n" or hello == "N":
            return "Bye! You are not worthy to play this game"
def useLifeline_2(lostAmt, winAmt, quitAmt, rightAns, firstOp, secondOp, rightOp, time_limit, qno):
  print("You can only use the  50-50 lifeline! All other lifelines are disbanded!")
  time.sleep(2.5)
  if fiftyUsed == True:
    print("You have already used the 50-50 lifeline! You will have to either answer or quit!")
  elif fiftyUsed == False:
    hello = input("Do you want to use the 50-50 lifeline (y/n)?").lower()
    if hello == "y":
      fifty_fifty(lostAmt, winAmt, quitAmt, firstOp, secondOp, rightOp, rightAns, time_limit, qno)
    else:
      winsound.PlaySound("sounds/10000000ques.wav", winsound.SND_LOOP + winsound.SND_ASYNC)
      hello2 = input("Okay! Please enter your answer or quit! ").lower()
      check_ans(hello2, winAmt, lostAmt, quitAmt, rightAns, firstOp, secondOp, rightOp, time_limit, qno)
def check_ans(input, winAmt, lostAmt, quitAmt, rightAns, firstOp, secondOp, rightOp, time_limit, qno):
  if qno > 5 and qno != 5 and qno != 11 and qno != 6 and qno != 15:
    if input == rightAns or input == rightAns.upper():
      winsound.PlaySound("sounds/" + str(winAmt) + "final.wav", winsound.SND_FILENAME)
      print(f"Correct Answer! You win Rs {winAmt}")
      winsound.PlaySound("sounds/" + str(winAmt) + "win" + ".wav", winsound.SND_FILENAME)
    elif input == "quit":
      quit(quitAmt, rightAns, rightOp)
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
      quit(quitAmt, rightAns, rightOp)
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
        quit(quitAmt, rightAns, rightOp)
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
        quit(quitAmt, rightAns, rightOp)
      elif input == "lifeline":
        useLifeline(input, lostAmt, winAmt, quitAmt, rightAns, firstOp, secondOp, rightOp, time_limit, qno)
      else:
        winsound.PlaySound("sounds/" + str(winAmt) + "final.wav", winsound.SND_FILENAME)
        wrong(rightOp, winAmt, lostAmt, qno)
  elif qno == 11 or qno == 6:
      if input == rightAns:
        winsound.PlaySound("sounds/" + str(winAmt) + "final.wav", winsound.SND_FILENAME)
        print(f"Correct Answer! You win Rs {winAmt}")
        winsound.PlaySound("sounds/" + str(winAmt) + "win.wav", winsound.SND_FILENAME)
      elif input == "quit":
        print("I will NOT let you quit at this point! You will not lose anything even if the answer is wrong!")
        quit_input = input("Enter your answer or enter 'lifeline' to use a lifeline ").lower()
        check_ans(quit_input, winAmt, lostAmt, quitAmt, rightAns, firstOp, secondOp, rightOp, time_limit, qno)
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
        time.sleep(2)
        print("Thank you for playing!")
        winsound.PlaySound("sounds/closing.wav", winsound.SND_FILENAME)
      elif input == "quit":
        print("Wise decision! It is only safe to quit at this point if you aren't sure!")
        time.sleep(1.5)
        print(f"Thank you for playing! You win Rs {quitAmt}")
        winsound.PlaySound("sounds/closing.wav", winsound.SND_FILENAME)
      elif input == "lifeline":
        print("You can only use the Fifty-Fifty lifeline. All other lifelines are disbanded")
        useLifeline_2(lostAmt, winAmt, quitAmt, rightAns, firstOp, secondOp, rightOp, time_limit, qno)
      else:
        winsound.PlaySound("sounds/" + str(winAmt) + "final.wav", winsound.SND_FILENAME)
        winsound.PlaySound("sounds/10000000lose.wav", winsound.SND_FILENAME)
        print("Oh no! That's the wrong answer! You fall back to Rs 3,20,000!")
        time.sleep(2)
        print("You should have quit if you were not sure! I feel sad for you :-(")
        time.sleep(1)
        print("Nevertheless, you played really well! Thank you for playing!")
        winsound.PlaySound("sounds/closing.wav", winsound.SND_FILENAME)
        exit()

def fourteenth():
  time.sleep(2)
  print("The 14th question for Rs 50,00,000")
  time.sleep(1)
  print("On your screen!!")
  winsound.PlaySound("sounds/5000000play.wav", winsound.SND_FILENAME)
  time.sleep(0.25)
  print("Who among the following was the author of Anand Math?")
  time.sleep(1)
  print("a)Bankim Chandra Chatterjee b)Rabindranath Tagore c)Raja Ram Mohan Roy d)Bal Gangadhar Tilak")
  winsound.PlaySound("sounds/5000000ques.wav", winsound.SND_LOOP + winsound.SND_ASYNC)
  input14 = input("Enter your Answer ").lower()
  check_ans(input14, 5000000, 320000, 2500000, "a", "a)Bankim Chandra Chatterjee", "b)Rabindranath Tagore", "a)Bankim Chandra Chatterjee", None, 14)
fourteenth()
