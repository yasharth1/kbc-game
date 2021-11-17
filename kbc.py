# Welcome, here are the guideline if you need them again
# lifeline - to use lifeline
# quit - to quit
import pyttsx3 # pip install pyttsx3
import winsound # pip install winsound
import time 
from inputimeout import inputimeout, TimeoutOccurred # pip install inputimeout
import matplotlib.pyplot as plt # pip install matplotlib
fiftyUsed = False
flipUsed = False
apUsed = False
ateUsed = False
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

def timeout(rightAns, lostAmt):
  print(f"Time Over!!")
  print(f"The correct answer is {rightAns}. You win Rs {lostAmt}")
  exit()
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def quit(quitAmt, rightAns, rightOp):
  if quitAmt == 10000 or quitAmt == 320000:
    print("I will not let you quit at this point! You will not lose anything even if you get the question wrong!")
    input("Enter your answer!")
  else:
    print(f"Thank you for playing! You won Rs {quitAmt}!")
    print(f"The correct answer is {rightOp}")
    exit()
  
def wrong(correctAns, winAmt, lostAmt, qno):
  if qno > 5:
    print(f"Wrong answer! The correct answer is {correctAns}! You fall back to Rs {lostAmt}")
    winsound.PlaySound("sounds/" + str(winAmt) + "lose.wav", winsound.SND_FILENAME)
    print("Thank you for playing the game! You played really well!")
    winsound.PlaySound("sounds/closing.wav", winsound.SND_FILENAME)
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
  print(f"I believe answer of this question should be {rightOp}")
  speak(f"I believe answer of this question should be {rightOp}")
  if qno < 11:
    try:
      winsound.PlaySound("sounds/timer.wav", winsound.SND_LOOP + winsound.SND_ASYNC)
      user_input = inputimeout(prompt="Enter your answer", timeout=time_limit).lower()
      check_ans(user_input, winAmt, lostAmt, quitAmt, rightAns, firstOp, secondOp, rightOp, time_limit, qno)
    except TimeoutOccurred:
      winsound.PlaySound("sounds/" + str(winAmt) + "lose.wav", winsound.SND_FILENAME)
      print("Time Over!!")
      print(f"The correct answer is {rightOp} ! You win Rs {lostAmt}")
      exit()
  else:
    user_input = input("Enter your answer").lower()
    check_ans(user_input, winAmt, lostAmt, quitAmt, rightAns, firstOp, secondOp, rightOp, time_limit, qno)    
def flip(winAmt, lostAmt, quitAmt, time_limit, qno):
  global flipUsed
  flipUsed = True
  print("Activating Flip the Question Lifeline...")
  print("Before proceeding, we would like you to guess the answer")
  flip_input = input("Guess an answer").lower()
  if flip_input == rightAns:
    print("Your answer would have been correct!")
    time.sleep(1)
    print("Now flipping the question...")
  else:
    print("Your answer would have been wrong! Thank God you took a lifeline")
    time.sleep(2)
    print("Now flipping the question...")
  time.sleep(1.5)
  if qno <= 5:
    try:
      winsound.PlaySound("sounds/1st.wav", winsound.SND_FILENAME)
      print("Fill in the blank in this hindi proverb which means to run away- '______ Dabaakar Bhaagna'")
      winsound.PlaySound("sounds/timer.wav", winsound.SND_LOOP + winsound.SND_ASYNC)
      flip_1 = inputimeout(prompt="a)दुम b)पेट c)हाथ d)कान", timeout=time_limit).lower()
      check_ans(flip_1, winAmt, lostAmt, quitAmt, "a", "a)दुम", "c)हाथ", "a)दुम", time_limit, qno)
    except TimeoutOccurred:
      winsound.PlaySound("sounds/" + winAmt + "lose.wav", winsound.SND_FILENAME)
      print("Time Over!!")
      print(f"The correct answer is a)दुम ! You win Rs {lostAmt}")
      exit()
  elif qno > 5 and qno <= 10:
    winsound.PlaySound("sounds/question.wav", winsound.SND_FILENAME)
    print("To which group of sportspersons is the Dronacharya Award given?")
    try:
      winsound.PlaySound("sounds/timer.wav", winsound.SND_LOOP + winsound.SND_ASYNC)
      flip_2 = inputimeout(prompt="a)Players b)Support Staff c)Administrators d)Coaches", timeout=time_limit).lower()
      check_ans(flip_2, winAmt, lostAmt, quitAmt, "d", "d)Support Staff", "d)Coaches", "d)Coaches", time_limit, qno)
    except TimeoutOccurred:
      winsound.PlaySound("sounds/" + str(winAmt) + "lose.wav", winsound.SND_FILENAME)
      print("Time Over!!")
      print(f"The correct answer is d)Coaches ! You win Rs {lostAmt}")
      exit()
  elif qno > 10:
    winsound.PlaySound("sounds/" + str(winAmt) + "play.wav", winsound.SND_FILENAME)
    print("When the Lucknow pact was adopted in 1916 Mohammad Ali Jinnah represented the Muslin League, who represented the Indian National Congress?")
    time.sleep(1.5)
    print("a)Mahatma Gandhi b)Bal Gangadhar Tilak c)Motilal Nehru d)Sardar Vallabhbhai Patel")
    winsound.PlaySound("sounds/" + str(winAmt) + "ques.wav", winsound.SND_FILENAME)
    flip_3 = input("Enter your answer").lower()
    check_ans(flip_3, winAmt, lostAmt, quitAmt, "b", "a)Mahatma Gandhi", "b)Bal Gangadhar Tilak", "b)Bal Gangadhar Tilak", time_limit, qno)
def fifty_fifty(lostAmt, winAmt, quitAmt, firstOp, secondOp, rightOp, rightAns, time_limit, qno):
  if qno < 11:
    global fiftyUsed
    fiftyUsed = True
    try:
      time.sleep(2)
      winsound.PlaySound("sounds/fifty2.wav", winsound.SND_FILENAME)
      print(f"Two options are left {firstOp} and {secondOp}")
      winsound.PlaySound("sounds/timer.wav", winsound.SND_LOOP + winsound.SND_ASYNC)
      userAns = inputimeout("Enter your answer!", timeout=time_limit).lower()
      check_ans(userAns, winAmt, lostAmt, quitAmt, rightAns, firstOp, secondOp, rightOp, time_limit, qno)
    except TimeoutOccurred:
      winsound.PlaySound("sounds/" + str(winAmt) + "lose.wav", winsound.SND_FILENAME)
      print("Time Over!!")
      print(f"Right answer is {rightAns}. You win Rs {lostAmt}")
      exit()
  else:
    time.sleep(2)
    winsound.PlaySound("sounds/fifty2.wav", winsound.SND_FILENAME)
    print(f"Two options are left {firstOp} and {secondOp}")
    winsound.PlaySound("sounds/" + str(winAmt) + "ques.wav", winsound.SND_LOOP + winsound.SND_ASYNC)
    userAns = input("Enter your answer!").lower()
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
  plt.bar(options, percent, color ='maroon', width = 0.4)
  plt.show()
  if qno < 11:
    try:
      winsound.PlaySound("sounds/timer.wav", winsound.SND_LOOP + winsound.SND_ASYNC)
      answer = inputimeout(prompt="Enter Your answer", timeout=time_limit).lower()
      check_ans(answer, winAmt, lostAmt, quitAmt, rightAns, firstOp, secondOp, rightOp, time_limit, qno)
    except TimeoutOccurred:
      print(f"Time Over!!")
      print(f"The correct answer is {rightOp}. You win {lostAmt}")
      exit()
  else:
    winsound.PlaySound("sounds/" + str(winAmt) + "ques.wav", winsound.SND_FILENAME)
    answer = input("Enter Your answer").lower()
    check_ans(answer, winAmt, lostAmt, quitAmt, rightAns, firstOp, secondOp, rightOp, time_limit, qno)    
def useLifeline(ll_input, lostAmt, winAmt, quitAmt, rightAns, firstOp, secondOp, rightOp, time_limit, qno):
  if ll_input == "lifeline":
    if fiftyUsed == True and apUsed == True and ateUsed == True and flipUsed == True:
      print("You have used all the lifelines. Please choose another option")
      all_lfl_used = input("You can either quit or try to answer")
      check_ans(all_lfl_used, winAmt, lostAmt, quitAmt, rightAns, firstOp, secondOp, rightOp, time_limit, qno)
    global lifeline
    lifeline = input("What lifeline do you want to use? Type ff' for 50-50, 'flip' for flip the question, 'ate' for ask the expert and 'ap' for audience poll").lower()
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
      print(f"The correct answer of this question is {rightOp}")
      flip(winAmt, lostAmt, quitAmt, time_limit, qno)
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
    hello = input("Invalid input! Do you really want to use a lifeline? (Y/n)")
    if hello == "y" or hello == "Y":
      useLifeline(ll_input, lostAmt, winAmt, quitAmt, rightAns, firstOp, secondOp, rightOp, time_limit, qno)
    elif hello == "n" or hello == "N":
      return "Bye! You are not worthy to play this game"
def useLifeline_2(input12, lostAmt, winAmt, quitAmt, rightAns, firstOp, secondOp, rightOp, time_limit, qno):
  hello = input("Do you want to use the 50-50 lifeline? (Y/n)").lower()
  if hello == "y":
    fifty_fifty(lostAmt, winAmt, quitAmt, firstOp, secondOp, rightOp, rightAns, time_limit, qno)
  else:
    hello2 = input("Okay! Please enter your answer or quit! ")
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
      wrong(rightOp, winAmt, lostAmt, qno)
  elif qno < 5:
    if input == rightAns or input == rightAns.upper():
      winsound.PlaySound("sounds/correct-answer_1.wav", winsound.SND_FILENAME)
      print(f"Correct Answer! You win Rs {winAmt}")
    elif input == "quit":
      quit(quitAmt, rightAns, rightOp)
    elif input == "lifeline":
      useLifeline(input, lostAmt, winAmt, quitAmt, rightAns, firstOp, secondOp, rightOp, time_limit, qno)
    else:
      wrong(rightOp, winAmt, lostAmt, qno)
  elif qno == 5:
    if input == rightAns or input == rightAns.upper():
      winsound.PlaySound("sounds/locknew_1.wav", winsound.SND_FILENAME)
      print(f"Correct Answer! You win Rs {winAmt}")
      winsound.PlaySound("sounds/stage1correct.wav", winsound.SND_FILENAME)
    elif input == "quit":
      quit(quitAmt, rightAns, rightOp)
    elif input == "lifeline":
      useLifeline(input, lostAmt, winAmt, quitAmt, rightAns, firstOp, secondOp, rightOp, time_limit, qno)
    else:
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
      wrong(rightOp, winAmt, lostAmt, qno)
  elif qno == 11 or qno == 6:
    if input == rightAns:
      winsound.PlaySound("sounds/" + str(winAmt) + "final.wav", winsound.SND_FILENAME)
      print(f"Correct Answer! You win Rs {winAmt}")
      winsound.PlaySound("sounds/" + str(winAmt) + "win.wav", winsound.SND_FILENAME)
    elif input == "quit":
      print("I will NOT let you quit at this point! You will not lose anything even if the answer is wrong!")
      quit_input = input("Enter your answer or enter 'lifeline' to use a lifeline")
      check_ans(quit_input, winAmt, lostAmt, quitAmt, rightAns, firstOp, secondOp, rightOp, time_limit, qno)
    elif input == "lifeline":
      useLifeline(input, lostAmt, winAmt, quitAmt, rightAns, firstOp, secondOp, rightOp, time_limit, qno)
  elif qno == 15:
    if input == rightAns:
      winsound.PlaySound("sounds/10000000final.wav", winsound.SND_FILENAME)
      print(f"Correct Answer! You win Rs {winAmt}")
      time.sleep(1)
      winsound.PlaySound("sounds/10000000win.wav", winsound.SND_FILENAME)
      print("Excellent! You have become a crorepati!")
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
      useLifeline_2(input, lostAmt, winAmt, quitAmt, rightAns, firstOp, secondOp, rightOp, time_limit, qno)
    else:
      winsound.PlaySound("sounds/10000000lose.wav", winsound.SND_FILENAME)
      print("Oh no! That's the wrong answer! You fall back to Rs 3,20,000!")
      time.sleep(2)
      print("You should have quit if you were not sure! I feel sad for you :-(")
      time.sleep(1)
      print("Nevertheless, you played really well! Thank you for playing!")
      winsound.PlaySound("sounds/closing.wav", winsound.SND_FILENAME)
time.sleep(2)
print("The 15th question for Rs 1,00,00,000")
time.sleep(1)
print("On your screen!!")
winsound.PlaySound("sounds/10000000play.wav", winsound.SND_FILENAME)
time.sleep(0.25)
print("Which of these films was the first Indian movie with sound and music?")
time.sleep(1)
print("a)Raja Harishchandra b)Alam Ara c)Shaheed d)Shree 420")
winsound.PlaySound("sounds/10000000ques.wav", winsound.SND_LOOP + winsound.SND_ASYNC)
def fifteenth():
  input15 = input("Enter your Answer").lower()
  confirm = input("Are you sure? (y/n)").lower()
  if confirm == "y":
    check_ans(input15, 10000000, 320000, 5000000, "b", "a)Raja Harishchandra", "b)Alam Ara", "b)Alam Ara", None, 15)
  else:
    fifteenth()
fifteenth()