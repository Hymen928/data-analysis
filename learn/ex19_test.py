def human_defect(name, age, address):
    print "This is %s !" % name
    print "He or she is %d years old ." % age
    print "He or she lives in %s." % address
    print "Now ,you knew a new friend ! Do you like it ?"
    print "***********************************"

print "I will introduced you a new friend ."
human_defect("Murphy", 18, "Anhui")

print "Next one:"
n = "Sera"
a = 16
ad = "Shanghai"
human_defect(n, a, ad)

print "Third :"
human_defect( n+ " Hu" , a*2 , ad *2)