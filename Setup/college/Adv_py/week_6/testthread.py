import threading
import time 

def task1():
        print("task 1 is executed")
        time.sleep(1)

def task2():
        print("task 2 is executed")    
        time.sleep(1)
cpu=0
for cpu in range(5):
    if cpu == 5:
          print("cpu core is full")
          if cpu==15:
                print("core is full")
          else : 
               cpu=cpu+5
               task2()
               cpu = cpu +1

    else:   
        task1()
        cpu = cpu + 1
            

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