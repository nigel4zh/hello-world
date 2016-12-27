# 7.1 Write a program that prompts for a file name, then opens that file and reads through the file, and print the contents of the file in upper case. Use the file words.txt to produce the output below.
# You can download the sample data at http://www.pythonlearn.com/code/words.txt

# Use words.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
# These two blocks below works the same.
fh_str = fh.read()
fh_strup = fh_str.upper()
fh_lt = fh_strup.rstrip()
print fh_lt

for line in fh:
	line_up = line.upper()
	line_lt = line_up.rstrip()
	print line_lt