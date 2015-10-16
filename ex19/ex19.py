#define the function, its parameters, and its content
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "That's enought for a party!"
	print "Get a blanket. \n"


#These are all different ways we can pass parameters to the function
print "We can just give the function numbers directly:"
cheese_and_crackers(20,30)

print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)


print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)



#My function
def santas_little_helper(jolly_level):
	print "Hi Santa's Little Helper!"
	print "How jolly is the big guy today?"
	print "He is at level %d of jolliness" % jolly_level

	for x in range(0, jolly_level-1):
		print "Ho!  "

print "\nRunning the function with an integer parameter"
santas_little_helper(3)

print "\nLet's run this with a variable parameter"
hohos = 10
santas_little_helper(hohos)


print "\nRunning the function with math in the parameter list"
hohos = 1
santas_little_helper(hohos * 6)
