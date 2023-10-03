import schedule
import time
from datetime import datetime

def change_shift(P1, P2):
    print(f"Shift change: {P1} is now on duty, replacing {P2}")

if __name__ == "__main__":
    P1 = "Person A"  
    P2 = "Person B"  
    
    schedule.every().day.at("08:00").do(change_shift, P1=P1, P2=P2)
    schedule.every().day.at("20:00").do(change_shift, P1=P2, P2=P1)
    
    while True:
        schedule.run_pending()
        time.sleep(1)
