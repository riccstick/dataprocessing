#!/usr/bin/python3

import argparse, textwrap
import pandas as pd

parser = argparse.ArgumentParser(
	prog='PROG',
	formatter_class=argparse.RawDescriptionHelpFormatter,
	description=textwrap.dedent('''\
 +------------------+
 | dataMeanErr_v1.0 |
 +------------------+
 by Erik Breslmayr, 2021

 - dataMeanErr takes several input files, containing 2 columns with x and y data.
 - Important to note is that the x data have to be the same, because only the y columns will be used for the calculations
 - The Average and StDev of all y columns will be calculated.
 - Output is the x column + average + stdev
 
 - Input and Output seperator can be chosen.
 
 - Example Usage: python3 dataMeanErr.py -i inputdata1.dat inputdata2.dat -isep tab -osep comma
    
'''))

parser.add_argument("-i", "--Inputfiles", nargs='+', required=True, help='Specify input filenames in csv format!')
parser.add_argument("-o", "--Outputfile", default="MeanErrOutput.dat", help='Optional: Specify output filename')

parser.add_argument("-isep", "--inputseperator", default=" ", help='Optional: Choose seperator (tab, space, comma, dot, minus); default is a space')

parser.add_argument("-osep", "--outputseperator", default="\t", help='Optional: Choose seperator (tab, space, comma, dot, minus); default is a comma tab')

args = parser.parse_args()
        
if args.inputseperator == "tab":
    args.inputseperator = "\t"
elif args.inputseperator == "space":
    args.inputseperator = " "
elif args.inputseperator == "comma":
    args.inputseperator = ","
elif args.inputseperator == "dot":
    args.inputseperator = "."
elif args.inputseperator == "minus":
    args.inputseperator = "-"
else:
    args.inputseperator = args.inputseperator
    
if args.outputseperator == "tab":
    args.outputseperator = "\t"
elif args.outputseperator == "space":
    args.outputseperator = " "
elif args.outputseperator == "comma":
    args.outputseperator = ","
elif args.outputseperator == "dot":
    args.outputseperator = "."
elif args.outputseperator == "minus":
    args.outputseperator = "-"
else:
    args.outputseperator = args.outputseperator

# calculates rows to skip
hashlines = ""
atlines = ""
with open(args.Inputfiles[0], 'r') as f:     
        header = f.readlines()
        for i in header:
            if i.startswith('#'):
                hashlines += str(1)
            elif i.startswith('@'):
                atlines += str(1)
        skiprows = len(hashlines) + len(atlines)        

with open(args.Inputfiles[0], 'r') as f:     
        data = pd.read_csv(f, sep=args.inputseperator, skipinitialspace = True, skiprows=skiprows, names = ['@TYPE xydy','y'])
        datax = data['@TYPE xydy']
        dataxy = datax
            
for filename in enumerate(args.Inputfiles):
    with open(filename[1], 'r') as f:     
        data = pd.read_csv(f, sep=args.inputseperator, skipinitialspace = True, skiprows=skiprows, names = ['@TYPE xydy','y'])
        num = filename[0] + 1
        datay = data['y']
        dataxy = pd.concat([dataxy, datay], axis=1)
        
dataMean = dataxy['y'].mean(axis=1)
datastd = dataxy['y'].std(axis=1)

meanErr = pd.concat([datax, dataMean, datastd], keys = ['@TYPE xydy', 'Average', 'StDev'], axis=1)
meanErr.to_csv(args.Outputfile, sep=args.outputseperator, index=False)

footerlines = "# xmgrace settings:\n"
with open(args.Inputfiles[0], 'r') as f:     
        header = f.readlines()
        for i in header:
            if i.startswith('@'):
                footerlines += i

footerlines = footerlines.replace("@TYPE xy", "")
ff = open(args.Outputfile, "a")
ff.write(footerlines)


print("+--------------------------------------------------+")
print("                 dataMeanErr")
print("+--------------------------------------------------+")
print("   Skipped the first " + str(skiprows) + " rows starting with # or @")
print("   Calculated average and stdev of " + str(num) + " files.")
print("   Output saved to " + args.Outputfile)
print("+--------------------------------------------------+")
    
    
    
    
    
    
    
