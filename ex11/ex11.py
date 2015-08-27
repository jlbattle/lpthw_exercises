#The commas are here bc otherwise print automatically puts an endline at the end of the string 
print "How old are you?",
age = raw_input()

print "How tall are you?",
height = raw_input()

print "How much do you weigh?",
weight = raw_input()


print "So you're %r tall, %r old, and %r heavy." % (height, age, weight)

'''
You could consider this a form --> this prompting the user for info, 
and then processing it
'''

