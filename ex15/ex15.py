from sys import argv

#this line assigns the command line arguments to two local variables
script, filename = argv

#this line opens the file input by the user and assigns it to a local variable
txt = open(filename)


#Display filename to user, print contents of file, close file
print "Here's your file %r: " % filename
print txt.read()
txt.close()


#Run through cycle again, except use raw_input() to get filename this time
print "Type the filename again: "
file_again =  raw_input(">  ")

#open file, assign to local variable, print out contents, close file
txt_again = open(file_again)
print txt_again.read()
txt_again.close()