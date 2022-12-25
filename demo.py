import threading
from queue import Queue

def input_with_timeout(prompt, timeout):
    def input_thread():
        input_queue.put(input(prompt))

    input_queue = Queue()
    input_thread = threading.Thread(target=input_thread)
    input_thread.daemon = True
    input_thread.start()

    input_thread.join(timeout)
    if input_thread.is_alive():
        return None
    else:
        return input_queue.get()

# Get input from the user, with a timeout of 5 seconds
response = input_with_timeout("Enter something: ", 5)
if response is None:
    print("Timed out!")
else:
    print("You entered:", response)
