import time
from threading import Thread

answer = None

def check():
    time.sleep(2)
    if answer != None:
        return
    while True:
      print("Too Slow")

Thread(target = check).start()

answer = input("Input something: ")
print(answer)