# Purpose : This tool reads in a file and will duplicate the entries.  Can use delimteter to indicate an
#           incrementing number
# Author : Andrew Lyons

import argparse
import os

print("***********************************************************")
print()
print("________               .__  .__               __                ")
print("\\______ \\  __ ________ |  | |__| ____ _____ _/  |_  ___________ ")
print(" |    |  \\|  |  \\____ \\|  | |  |/ ___\\__   \\    __\\/  _ \\_  __ \\ ")
print(" |    `   \\  |  /  |_> >  |_|  \\  \\___ / __ \\|  | (  <_> )  | \\/ ")
print("/_______  /____/|   __/|____/__|\\___  >____  /__|  \\____/|__|    ")
print("        \\/      |__|                \\/     \\/                   ")
print("                                            ")
print("***********************************************************")


# Get a list of parameters
parser = argparse.ArgumentParser(description = "List of parameters")
parser.add_argument("-f", "--file", help="Path to the input file", required=True)
parser.add_argument("-v", "--verbose", help="Increase output verbosity", action="store_true")
parser.add_argument("-o", "--output", help="File the output is directed to", required=False)
parser.add_argument("-r", "--repeat", help="Number of times the input should be repeated.\r\nIf a number is not defined, then the output will only duplicate once.", required=False)
parser.add_argument("-s","--start", help="The number the index should start at. Make sure the key \%n is found in the input file.", required=False)
#parser.add_argument("-t","--total", help="Indicate a field name to keep a total of.", required=False)
parser.add_argument("-d","--delimiter", help="Separate each entry with a provided delimieter (example ,)", required=False)


args = parser.parse_args()

if(args.verbose):
	print("File path:", args.file)
	if args.verbose:
		print("Verbose mode enabled")
	if args.output:
		print("Output is directed to : ", args.output)
	if args.repeat:
		print("Duplicating the input (x) times ", args.repeat)

# configure settings based on inputs
if args.repeat is None:
	x = 1
else :
	x = int(args.repeat)

if args.start is None:
	s = 0
else :
	s = int(args.start)

if args.output is not None:
	# replace the file, find a more elegant
	#os.remove(args.output)
	open(args.output,"w")

# Defined here so it's not calculated on each pass in the for loop
lastEntry = (x-1)

for n in range(0, x):

	# Open the file that is to be read in from
	f = open(args.file, "r")
	orig_file = f.read()

#	if total in orig_file:
#		print("found")
	### Changes here, can make numerous flags for the tool to iterate over.
	### Could replace %s% for string, and give a format.

	f1 = orig_file.replace("%n%", str(s+n))

	if args.output is None:
		if n != lastEntry and args.delimiter is not None:
				f2 = f1 + args.delimiter
		else:
			f2= f1
		print(f2)
	else:
		with open(args.output, "a") as file:
			if n != lastEntry and args.delimiter is not None:
				f2 = f1 + args.delimiter
			else:
				f2 = f1
			file.write(f2)



