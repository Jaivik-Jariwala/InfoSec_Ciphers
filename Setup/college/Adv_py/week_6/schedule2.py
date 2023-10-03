import schedule
import time

def task1():
    print("Wake up sid, task 1 is done")

def task2():
    print("death coffee, so task 2 is done")

def task3():
    #
 if __name__ == "__main__":
    schedule.every(2).seconds.do(task1)
    schedule.every(3).seconds.do(task2)
    while True:
        schedule.run_pending()
        time.sleep(1)
