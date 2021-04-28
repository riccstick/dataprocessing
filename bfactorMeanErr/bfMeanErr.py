#!/home/ricci/anaconda3/bin/python3
import argparse, textwrap
import pandas as pd
from biopandas.pdb import PandasPdb


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

parser.add_argument("-i", "--Inputfiles", nargs='+', help='Specify input filenames containing bfactors in pdb format!')
parser.add_argument("-ref", "--refFile", nargs='+', help='Specify input reference filename in pdb format!')
parser.add_argument("-o", "--Outputfile", default="MeanErrOutput.dat", help='Optional: Specify output filename')

args = parser.parse_args()
#ref File
'''with open(args.refFile[0], 'r') as f:     
    f = f.readlines()    
ppdb = PandasPdb().read_pdb_from_list(f)
ppdb.df['ATOM'] = ppdb.df['ATOM'][['record_name','atom_number','blank_1', 'atom_name', 'alt_loc', 'residue_name', 'blank_2', 'chain_id', 'residue_number', 'blank_3', 'x_coord', 'y_coord', 'z_coord', 'occupancy']]
ppdb.to_pdb(path='./test.pdb')
'''
ppdb = PandasPdb()
#bfactors average, err
bfall = pd.DataFrame() #emtpy dataframe for pd.concat
for filename in enumerate(args.Inputfiles):
    with open(filename[1], 'r') as f:
        f = f.readlines()
    ppdb.read_pdb_from_list(f)
    num = filename[0] + 1
    bf = ppdb.df['ATOM']['b_factor']
    bfall = pd.concat([bfall, bf], axis=1)

bfMean = bfall.mean(axis=1)
bfMean.to_csv(args.Outputfile, index=False)


# combine to pdb file
#finalPdb = pd.concat([ref, bfMean], axis=1)

#ppdb.to_pdb(path='./test.pdb')

print("+--------------------------------------------------+")
print("                   bfMeanErr")
print("+--------------------------------------------------+")
print("   Calculated average bfactors of " + str(num) + " files.")
print("   Used " + str(args.refFile) + " for coordinates.")
print("   Output pdb file saved as " + args.Outputfile)
print("+--------------------------------------------------+")