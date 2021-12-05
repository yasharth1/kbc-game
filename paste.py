# Welcome, here are the guideline if you need them again
# lifeline - to use lifeline
# quit - to quit
from threading import Timer
import pyttsx3  # pip install pyttsx3
import winsound 
import time
import matplotlib.pyplot as plt  # pip install matplotlib
import cv2 as cv  # pip install opencv-python
fiftyUsed = False
flipUsed = False
apUsed = False
ateUsed = False
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
time.sleep(2)
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
print("So let's start the game!")
time.sleep(2)
engine.setProperty('voice', voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    from threading import Timer
def inputtime(rightOp, lostAmt):
  t = Timer(time_limit, print, [f'Time up!!The correct answer is {rightOp}! You fall back to {lostAmt}'], winsound.PlaySound("sounds/timer.wav", winsound.SND_FILENAME))
  t.start()
  prompt = "Enter your answer " % time_limit
  global answer
  winsound.PlaySound("sounds/timer.wav", winsound.SND_LOOP + winsound.SND_ASYNC)
  answer = input(prompt)
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
    print("Analyzing the brain database...")
    time.sleep(3)
    print("Okay, I have found the answer!")
    time.sleep(3)
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


def flip(winAmt, lostAmt, quitAmt, rightAns, time_limit, qno):
    global flipUsed
    flipUsed = True
    print("Activating Flip the Question Lifeline...")
    time.sleep(2)
    print("Before proceeding, we would like you to guess the answer")
    time.sleep(1)
    flip_input = input("Guess an answer").lower()
    time.sleep(1.5)
    if flip_input == rightAns:
        print("Your answer would have been correct!")
        time.sleep(1)
        print("Now flipping the question...")
    else:
        print("Your answer would have been wrong! Thank God you took a lifeline! Correct answr is " + rightAns)
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
            winsound.PlaySound("sounds/4000.wav", winsound.SND_FILENAME)
            print("Time Over!!")
            print(f"The correct answer is a)दुम ! You win Rs {lostAmt}")
            exit()
    elif qno > 5 and qno <= 10:
        winsound.PlaySound("sounds/question.wav", winsound.SND_FILENAME)
        print("To which group of sportspersons is the Dronacharya Award given?")
        try:
            winsound.PlaySound("sounds/timer.wav", winsound.SND_LOOP + winsound.SND_ASYNC)
            flip_2 = inputimeout(prompt="a)Players b)Support Staff c)Administrators d)Coaches",
                                 timeout=time_limit).lower()
            check_ans(flip_2, winAmt, lostAmt, quitAmt, "d", "d)Support Staff", "d)Coaches", "d)Coaches", time_limit,
                      qno)
        except TimeoutOccurred:
            winsound.PlaySound("sounds/" + str(winAmt) + "lose.wav", winsound.SND_FILENAME)
            print("Time Over!!")
            print(f"The correct answer is d)Coaches ! You win Rs {lostAmt}")
            exit()
    elif qno > 10:
        winsound.PlaySound("sounds/" + str(winAmt) + "play.wav", winsound.SND_FILENAME)
        print(
            "When the Lucknow pact was adopted in 1916 Mohammad Ali Jinnah represented the Muslin League, who represented the Indian National Congress?")
        time.sleep(1.5)
        print("a)Mahatma Gandhi b)Bal Gangadhar Tilak c)Motilal Nehru d)Sardar Vallabhbhai Patel")
        winsound.PlaySound("sounds/" + str(winAmt) + "ques.wav", winsound.SND_FILENAME)
        flip_3 = input("Enter your answer").lower()
        check_ans(flip_3, winAmt, lostAmt, quitAmt, "b", "a)Mahatma Gandhi", "b)Bal Gangadhar Tilak",
                  "b)Bal Gangadhar Tilak", time_limit, qno)


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


def audience_poll(lostAmt, winAmt, quitAmt, firstOp, secondOp, rightOp, rightAns, time_limit, qno, a_percent, b_percent,
                  c_percent, d_percent):
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
    winsound.PlaySound("dnjjd.wav", winsound.SND_FILENAME)
    if ll_input == "lifeline":
        if fiftyUsed == True and apUsed == True and ateUsed == True and flipUsed == True:
            print("You have used all the lifelines. Please choose another option")
            all_lfl_used = input("You can either quit or try to answer")
            check_ans(all_lfl_used, winAmt, lostAmt, quitAmt, rightAns, firstOp, secondOp, rightOp, time_limit, qno)
        global lifeline
        lifeline = input(
            "What lifeline do you want to use? Type ff' for 50-50, 'flip' for flip the question, 'ate' for ask the expert and 'ap' for audience poll").lower()
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
            flip(winAmt, lostAmt, quitAmt, rightAns, time_limit, qno)
    elif lifeline == "ap":
        if apUsed:
            print("You have already used the Audience poll Lifeline")
            useLifeline(ll_input, lostAmt, winAmt, quitAmt, rightAns, firstOp, secondOp, rightOp, time_limit, qno)
        elif apUsed == False:
            if rightAns == "a":
                audience_poll(lostAmt, winAmt, quitAmt, firstOp, secondOp, rightOp, rightAns, time_limit, qno, 52, 36,
                              5, 7)
            elif rightAns == "b":
                audience_poll(lostAmt, winAmt, quitAmt, firstOp, secondOp, rightOp, rightAns, time_limit, qno, 12, 45,
                              23, 20)
            elif rightAns == "c":
                audience_poll(lostAmt, winAmt, quitAmt, firstOp, secondOp, rightOp, rightAns, time_limit, qno, 10, 24,
                              47, 19)
            elif rightAns == "d":
                audience_poll(lostAmt, winAmt, quitAmt, firstOp, secondOp, rightOp, rightAns, time_limit, qno, 19, 21,
                              22, 38)
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
            winsound.PlaySound("sounds/" + str(winAmt) + "final.wav", winsound.SND_FILENAME)
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
            winsound.PlaySound("sounds/locknew_1.wav", winsound.SND_FILENAME)
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
            quit_input = input("Enter your answer or enter 'lifeline' to use a lifeline")
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
            winsound.PlaySound("sounds/" + str(winAmt) + "final.wav", winsound.SND_FILENAME)
            winsound.PlaySound("sounds/10000000lose.wav", winsound.SND_FILENAME)
            print("Oh no! That's the wrong answer! You fall back to Rs 3,20,000!")
            time.sleep(2)
            print("You should have quit if you were not sure! I feel sad for you :-(")
            time.sleep(1)
            print("Nevertheless, you played really well! Thank you for playing!")
            winsound.PlaySound("sounds/closing.wav", winsound.SND_FILENAME)
            exit()


def first():
    print("The 1st question for Rs 1000")
    time.sleep(1)
    print("On your screen!!")
    print("Who is the current President of India?")
    winsound.PlaySound("sounds/1st.wav", winsound.SND_FILENAME)
    print("a)Narendra Modi b)Ram Nath Kovind c)Venkaiah Naidu d)Pranab Mukherjee")
    inputtime("b)Ram Nath Kovind", 0)
    winsound.PlaySound("sounds/timer.wav", winsound.SND_LOOP + winsound.SND_ASYNC)
    inputtime("b)Ram Nath Kovind", 0)
    check_ans(answer, 1000, 0, 0, "b", "b)Ram Nath Kovind", "c)Venkaiah Naidu", "b)Ram Nath Kovind", 45, 1)
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
    inputtime("a)Dahi(Curd)", 0)
    check_ans(answer, 2000, 0, 1000, "a", "a)Dahi (curd)", "b)Milk", "a)Dahi (curd)", 45, 2)
second()
def third():
    print("The 3rd question for Rs 3000")
    time.sleep(1)
    print("On your screen!")
    time.sleep(0.25)
    print("Where is the Motera stadium, which is the largest stadium, situated?")
    winsound.PlaySound("sounds/1st.wav", winsound.SND_FILENAME)
    print("a)Delhi b)Mohali c)Ahmedabad d)Chennai")
    inputtime("c)Ahmedabad", 0)
    check_ans(answer, 3000, 0, 2000, "c", "c)Ahmedabad", "d)Chennai", "c)Ahmedabad", 45, 3)
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
    inputtime("b)Alam Ara", 0)
    check_ans(input3, 5000, 0, 3000, "b", "a)Raja Harishchandra", "b)Alam Ara", "b)Alam Ara", 45, 4)
fourth()


def audio1():
    winsound.PlaySound("sounds/trystwithdestiny.wav", winsound.SND_FILENAME)


def option5():
    time.sleep(1)
    print("a)Sardar Patel b)Maulana Abul Kalam c)Veer Savarkar d)Jawaharlal Nehru")
    winsound.PlaySound("sounds/timer.wav", winsound.SND_LOOP + winsound.SND_ASYNC)
    inputtime("d)Jawaharlal Nehru", 0)
    check_ans(answer, 10000, 0, 3000, "d", "c)Veer Savarkar", "d)Jawaharlal Nehru", "d)Jawaharlal Nehru", 45, 5)
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
    print("Which Enterprise is constructing the new Parliament building in India?")
    winsound.PlaySound("sounds/20000play.wav", winsound.SND_FILENAME)
    print("a)Adani Group b)Tata projects c)Larsen and Toubro d)GMR Projects")
    inputtime("b)Tata Projects", 10000)
    check_ans(answer, 20000, 10000, 10000, "b", "a)Adani Group", "b)Tata Projects", "b)Tata Projects", 60, 6)
sixth()
def seventh():
    time.sleep(2)
    print("The 7th question for Rs 40,000")
    time.sleep(1)
    print("On your screen!!")
    winsound.PlaySound("sounds/40000play.wav", winsound.SND_FILENAME)
    time.sleep(1)
    print("The person shown in this picture was the president of which Country?")
    print("Press any key to exit (Do NOT press the close icon)")
    time.sleep(3)
    image = cv.imread("jfk.jpg")
    cv.imshow("Press any key to exit", image)
    cv.waitKey(0)
    cv.destroyAllWindows()
    print("a)Russia b)Britain c)Canada d)United States of America")
    inputtime("d)United States of America", 10000)
    check_ans(answer, 40000, 0, 20000, "d", "c)Canada", "d)United States of America", "d)United States of America", 60, 7)
seventh()
def eighth():
    time.sleep(2)
    print("The 8th question for Rs 80,000")
    time.sleep(1)
    print("On your screen!!")
    winsound.PlaySound("sounds/80000play.wav", winsound.SND_FILENAME)
    time.sleep(0.25)
    print("Who was the first Field Marshal of Indian Army?")
    time.sleep(1)
    print("a)Sam Manekshaw b)Vikram Batra c)K.M. Cariappa d)Mohammed Usman")
    inputtime("a)Sam Manekshaw", 10000)
    check_ans(answer, 80000, 10000, 40000, "a", "a)Sam Manekshaw", "c)K.M. Cariappa", "a)Sam Manekshaw", 60, 8)
eighth()
def ninth():
    time.sleep(2)
    print("The 9th question for Rs 1,60,000")
    time.sleep(1)
    print("On your screen!!")
    winsound.PlaySound("sounds/160000play.wav", winsound.SND_FILENAME)
    time.sleep(0.25)
    print("")
    time.sleep(1)
    print("a)Raja Harishchandra b)Alam Ara c)Shaheed d)Shree 420")
    inputtime("b)Alam Ara", 10000)
    check_ans(answer, 160000, 10000, 80000, "b", "a)Raja Harishchandra", "b)Alam Ara", "b)Alam Ara", 60, 9)
ninth()
def tenth():
    time.sleep(2)
    print("The 10th question for Rs 3,20,000")
    time.sleep(1)
    print("On your screen!!")
    winsound.PlaySound("sounds/320000play.wav", winsound.SND_FILENAME)
    time.sleep(0.25)
    print("Which of these films was the first Indian movie with sound and music?")
    time.sleep(1)
    print("a)Raja Harishchandra b)Alam Ara c)Shaheed d)Shree 420")
    inputtime("b)Alam Ara", 10000)
    check_ans(answer, 320000, 10000, 160000, "b", "a)Raja Harishchandra", "b)Alam Ara", "b)Alam Ara", 60, 10)
tenth()
print("Congratulations, You have successfully passed the 2nd stage! Now you will take at least Rs 3,20,000 from here")
time.sleep(2)
print("Now there is no time limit on the questions, You can take as much time as you want!")
time.sleep(1.5)
print("The questions are slowly going to get difficult, so play wisely and quit if you feel so!")
time.sleep(1.5)
print("Good Luck!")
time.sleep(1)


def eleventh():
    time.sleep(2)
    print("The 11th question for Rs 6,40,000")
    time.sleep(1)
    print("On your screen!!")
    winsound.PlaySound("sounds/640000play.wav", winsound.SND_FILENAME)
    time.sleep(0.25)
    print("Which of these films was the first Indian movie with sound and music?")
    time.sleep(1)
    winsound.PlaySound("sounds/640000ques.wav", winsound.SND_LOOP + winsound.SND_ASYNC)
    print("a)Raja Harishchandra b)Alam Ara c)Shaheed d)Shree 420")
    input11 = input("Enter your Answer").lower()
    check_ans(input11, 640000, 320000, 320000, "b", "a)Raja Harishchandra", "b)Alam Ara", "b)Alam Ara", None, 11)


eleventh()


def twelfth():
    time.sleep(2)
    print("The 12th question for Rs 12,50,000")
    time.sleep(1)
    print("On your screen!!")
    winsound.PlaySound("sounds/1250000play.wav", winsound.SND_FILENAME)
    time.sleep(0.25)
    print("Which of these films was the first Indian movie with sound and music?")
    time.sleep(1)
    print("a)Raja Harishchandra b)Alam Ara c)Shaheed d)Shree 420")
    winsound.PlaySound("sounds/1250000ques.wav", winsound.SND_LOOP + winsound.SND_ASYNC)
    input12 = input("Enter your Answer").lower()
    check_ans(input12, 1250000, 320000, 640000, "b", "a)Raja Harishchandra", "b)Alam Ara", "b)Alam Ara", None, 12)


twelfth()


def thirteenth():
    time.sleep(2)
    print("The 13th question for Rs 25,00,000")
    time.sleep(1)
    print("On your screen!!")
    winsound.PlaySound("sounds/2500000play.wav", winsound.SND_FILENAME)
    time.sleep(0.25)
    print("Which of these films was the first Indian movie with sound and music?")
    time.sleep(1)
    print("a)Raja Harishchandra b)Alam Ara c)Shaheed d)Shree 420")
    winsound.PlaySound("sounds/1250000ques.wav", winsound.SND_LOOP + winsound.SND_ASYNC)
    input13 = input("Enter your Answer").lower()
    check_ans(input13, 2500000, 320000, 1250000, "b", "a)Raja Harishchandra", "b)Alam Ara", "b)Alam Ara", None, 13)


thirteenth()


def fourteenth():
    time.sleep(2)
    print("The 14th question for Rs 50,00,000")
    time.sleep(1)
    print("On your screen!!")
    winsound.PlaySound("sounds/5000000play.wav", winsound.SND_FILENAME)
    time.sleep(0.25)
    print("Which of these films was the first Indian movie with sound and music?")
    time.sleep(1)
    print("a)Raja Harishchandra b)Alam Ara c)Shaheed d)Shree 420")
    winsound.PlaySound("sounds/5000000ques.wav", winsound.SND_LOOP + winsound.SND_ASYNC)
    input14 = input("Enter your Answer").lower()
    check_ans(input14, 5000000, 320000, 2500000, "b", "a)Raja Harishchandra", "b)Alam Ara", "b)Alam Ara", None, 14)
fourteenth()
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


def fifteenth():
    input15 = input("Enter your Answer").lower()
    confirm = input("Are you sure? (y/n)").lower()
    if confirm == "y":
        check_ans(input15, 10000000, 320000, 5000000, "b", "a)Raja Harishchandra", "b)Alam Ara", "b)Alam Ara", None, 15)
    else:
        fifteenth()


fifteenth()
