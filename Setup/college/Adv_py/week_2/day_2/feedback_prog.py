def collect_feedback():
    name=None
    name = str(input("enter your name"))
    feedback = str(input("enter your feedback"))
    with open("feedback.txt", "a") as f:
        f.write("{}, {}, /n"..format(name, feedback))
    print("feedback submitted")
def main():
    while True:
        print(" 1. Submit Feedback")
        print(" 2. Exit ")
        choice = input("enter your choice")
        if choice == "1":
            collect_feedback()
        elif choice == "2":
            break
        else :
            print("invalid choice")

if __name__ = "__main__" : 
    main()