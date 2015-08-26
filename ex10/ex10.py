tabby_cat = "\tI'm tabbed in."

persian_cat = "I'm split\non a line"

backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat nip
\t* Fishes
\t* Cat food\n\t* Grass 
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat


#This makes a little animation on the command line :) 
#\r is for a carriage return - without it, the characters would print in succession
#instead of in place; without the comma at the end, the characters print on different lines
while True:
	for i in ["/", "-", "|", "\\", "|"]:
		print "%s\r" % i ,