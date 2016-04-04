x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary,do_not)

print x
print y

print "I said: %r" % x
print "I also said: '%s'." %y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation %hilarious

w = "This is the left side of..."
e = "a string with a right side."
print w + e

text = "I am %d years old." % 22
print "%%s is-> I said: %s." % text
print "%%r is-> I said: %r." % text

#利用三引号（ """or”’），你可以指示一个多行的字符串。你可以在三引号中自由
#的使用单引号和双引号。例如：