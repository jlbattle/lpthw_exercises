#This sentence will have a number swapped in for the format character
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"

#This sentence will have two strings swapped in for the format characters - so it has strings inside it, also
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

#This string has another string inside it
print "I said: %r." % x

#This string has another string inside it
print "I also said: '%s'." % y

hilarious = False

#This string has another string inside it
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

#The '+' concatenates the two strings w & e
print w + e