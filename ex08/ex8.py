#set up a string with 4 formatters
formatter = "%r %r %r %r"

#now replace the formatter with different types of objects
print formatter % (1,2,3,4)

print formatter % ("one","two","three","four")

print formatter % (True,False,False,True)

print formatter % (formatter,formatter,formatter,formatter)

print formatter % ("I had this thing", "that you could type up, right","But it didn't sing", "So I said goodnight.")