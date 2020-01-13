from sys import exit

def start():
    print "Welcome to The world of game."
    print "There are two doors, you woule have a choice."
    print "Door1 or Door2 ?"

    choice = raw_input("> ")
    if choice == "Door1":
        Door1()
    elif choice == "Door2":
        Door2()
    else:
        print "I got no idea what that means."
        exit(0)

def Door1():
    print "The choice is not good enough, but you can do something to change it! "
    print "left , top or right ?"

    num = raw_input("> ")
    if num == "left":
        print "To be ro not to be, which ?"
        print "Red of Green ?"
        color = raw_input("> ")
        if color == "Red":
            print "Congradulations! You are successed !"
            exit(0)
        elif color == "Green":
            print "Not bad! You can rechoose!"
            print "*" * 30
            start()
        else:
            print "I got no idea what that means."
            Door1()

    elif num == "top":
        print "This is the door of evol! Carefully!"
        print "A dog sit here,what would you do ?"
        print "Threaten or Draw back"
        next = raw_input("> ")
        if next == "Threaten":
            print "This way is correct , you will got many gold or die ..."
            gold()
        elif next == "Draw back":
            print "Poor guy , you will die "
            dead()

    elif num == right:
        pass
    else:
        print "I got no idea what that means."
        exit(0)
def gold():
    pass

def dead(reason):
    pass

start()