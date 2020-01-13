#while-loops
'''
def my_while(loop, step):
    i = 0
    numbers = []
    while i < loop:
        print "At the top i is %d" % i
        numbers.append(i)
        i += step
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i
        print ("\n----------------------")

        print "The numbers:"
        for num in numbers:
            print num

my_while(5,3)
'''
#for-loop + range
def my_for(loop,step):
    i = 0
    numbers =[]
    for i in range(0,loop,step):
        print "At the top i is %d" % i
        numbers.append(i)
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i
        print ("\n----------------------")
        print "The numbers:"
        for num in numbers:
            print num

my_for(10,2)