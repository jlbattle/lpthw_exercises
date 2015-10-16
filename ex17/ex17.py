from sys import argv

#see this link for more info on os.path: https://pymotw.com/2/ospath/
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

in_data = open(from_file).read()

print "The input file %s is %d bytes long" % (from_file, len(in_data))


print "Does the output file exist? %r" % (exists(to_file))
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()


out_file = open(to_file, 'w')
out_file.write(in_data)

print "Alright, all done"

#must close the file because there is no guarantee the OS will do it for you
#if you don't get in the habit of closing files, you may have problems in 
#programs that repeatedly access the file
out_file.close()