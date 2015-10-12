#this round, I open the file and read it again after writing to it
from sys import argv

script, filename = argv


print "We're going to erase %r." % filename
print "If you don't want that, hit CNTRL-C (^C)"
print "If you do want that, hit RETURN."

raw_input("?")

#Opens the file in write('w') and truncate('+') mode
print "Opening and truncating the file..."
target = open(filename,'w+')

print "Now I will ask you for three lines of input"
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

#close out file (like saving)
target.close()

#re-open file with new content and print to console
print	"What did you write?"
newTarget = open(filename)
print newTarget.read()

print "And finally, we close it"
newTarget.close()