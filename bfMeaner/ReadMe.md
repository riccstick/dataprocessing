# bfMeanEr

- bfMeaner is a bash script to help wrapping up bfactor data generated with Gromacs (tested with gmx_2018.8) `rmsf` utility. 
- It can use a reference file for getting the coordinates, if rmsf has problems with fitting the coordinates into the box.
- Therefore, visualization of the bfactors in e.g. Pymol is possible.

- Furthermore, it can use 3 replicates of simulations and calculates the mean of the 3 given bfactor pdb files.
- It also generates a dat file with the atoms, mean bfactors and stdev for plotting.

- Also only `.xvg` data generated also from `gmx` can be used to calculate the mean and stdev. (3 files limited)
