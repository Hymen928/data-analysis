class Golden_room(object):
    def __init__(self,number):
        self.number = 0

    def gold_add(self):
        print "You are a lucky guy ! You win the choice to add you gold"
        self.number += 100
        print "Now you have: %d" %self.number
        print "***********************************"

    def gold_reduce(self):
        print "Poor guy !"
        self.number -= 100
        print "Now you have: %d" %self.number
        print "***********************************"