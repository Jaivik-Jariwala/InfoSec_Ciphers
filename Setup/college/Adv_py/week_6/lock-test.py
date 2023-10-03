import threading
import time

globaled_resource = 0
lock = threading.Lock()

def increment_resource():
    global shared_resource
    for i in range(5):
        with lock:
            shared_resource += 1
            print(f"increment: {shared_resource}")
        time.sleep(1)

def decrement_resource():
    global shared_resource
    for _ in range(5):
        with lock:
            shared_resource -=1
            print(f"decremented {shared_resrource}")
        time.sleep(1)
