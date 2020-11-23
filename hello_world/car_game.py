started=False
print("""
    start -to start the car
    stop- to stop the car
    quit-to quit the program
    help - to ask for the help """)
while True:
    command = input(" >:").lower()
    if command== "help":
        print("""
    start -to start the car
    stop- to stop the car
    quit-to quit the program""")
    elif command == "start":
        if started:
            print("car already started")
        else:
            print("car started")
            started=True
    elif command == "stop":
        if not started:
            print(" car already stopped ")

        else:
            print("car stopped")
            started = False

    elif command in ["exit", "quit"]:
        print(" all process has now ended:"
              "thanku for chossing us:")
        break
    else:
        print("i don't understand that")
