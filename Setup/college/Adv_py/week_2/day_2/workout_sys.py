import datetime

def log_exercise():
    date = datetime.date(input("enter date (YYYY/MM/DD)"))
    exercise = str(input("enter the exercise"))
    duration = float(input("enter time in minutes"))
    calories_burnt = float(input("enter the calories burnt"))
    with open("workout_log.txt", "a") as f:
        f.write("{}, {}, {}, {} \n". format(date, exercise, duration, calories_burnt))
    print("Exercise Logged!")

def view_log():
    with open("workout_log.txt", "r")as f:
        for line in f:
            print(f.strip())


def main():
    while True:
        print("1. Log exercise")
        print("2. View log")
        print("3. Exit")
        choice = input("enter your choice")

        if choice == "1":
            log_exercie()
        elif choice == "2"
            view_log()
        elif choice == "3"
            break
        else:
            print("invalid choice")

if __name__ == "__main__":
    main()