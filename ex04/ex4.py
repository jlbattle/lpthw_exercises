#100 cars
cars = 100

#4.0 units of space in a cars
space_in_a_car = 4.0

#30 drivers
drivers = 30

#90 passengers
passengers = 90

#cars no one is driving
cars_not_driven = cars - drivers

#cars someone is driving
cars_driven = drivers

#total number of people that can be transported in carpool
carpool_capacity = cars_driven * space_in_a_car

#average number of passengers in each car
average_passengers_per_car = passengers / cars_driven

print "There are", cars , "cars available."
print "There are only", drivers , "drivers available."
print "There will be", cars_not_driven , "empty cars today."
print "We can transport", carpool_capacity , "people today."
print "We have", passengers , "who want to carpool today."
print "We need to put about", average_passengers_per_car , "people in each car."
