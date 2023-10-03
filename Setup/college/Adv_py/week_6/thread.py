import threading
import time 

def task1():
    for i in range(5):
        print("task1 execute")
        time.sleep(1)

def task2():
    for i in range(5):
        print("task2 execute")
        time.sleep(1)

if __name__ == "__main__":
    thread1 = threading.Thread(target=task1)
    thread2 = threading.Thread(target=task2)

#start ops
    thread1.start()
    thread2.start()

#join ops
    thread1.join()
    thread2.join()

    print("all task done")