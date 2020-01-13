from sys import argv

script, user_name = argv
prompt = ' > '
mark = "*************************"

print "Hi %s, I'm the %s script.\n%s" % (user_name,script,mark)
print "I'd like to sak you a few questions..\n%s" % mark
print "Do you like me %s ?.\n%s" % (user_name,mark)
likes = raw_input(prompt)

print "Where do you live %s ?\n%s" % (user_name,mark)
lives = raw_input(prompt)

print "What kind of computer do you have?\n%s" % mark
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)