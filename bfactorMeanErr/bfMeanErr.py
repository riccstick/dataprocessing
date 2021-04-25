#!/usr/bin/python3

import argparse, textwrap
import pandas as pd
from biopandas.pdb import PandasPdb

ppdb = PandasPdb()
ppdb.read_pdb('./bfactorConvBackbone1.pdb')
var = ppdb.df['ATOM'].head()
bf = var['b_factor']
print(bf)

'''    for line in f:
        if line.startswith("ATOM"):
            bfactors = line[60:]
print(bfactors)
'''
    
        
                
                
                
'''
for filename in enumerate(args.Inputfiles):
    with open(filename[1], 'r') as f:     
        data = pd.read_csv(f, sep=args.inputseperator, skipinitialspace = True, skiprows=skiprows, names = ['@TYPE xydy','y'])
        num = filename[0] + 1
        datay = data['y']
        dataxy = pd.concat([dataxy, datay], axis=1)        


meanErr.to_csv(args.Outputfile, sep=args.outputseperator, index=False)


print("+--------------------------------------------------+")
print("                   bfMeanErr")
print("+--------------------------------------------------+")
print("   Output saved to " + args.Outputfile)
print("+--------------------------------------------------+")
    
    
    
'''    
    
    
    
