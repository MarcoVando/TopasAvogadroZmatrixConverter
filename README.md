# TopasAvogadroZmatrixConverter
Script to convert Gaussian ZMatrix to Topas format ZMatrix. This way u can create a rigid body in Avogadro, save it as Gaussian ZMatrix and then load it into Topas.   
Don't worry too much about drawing your molecule very precisely. You can always use the Geometry Optimization tool! U can exclude atoms from the optimization using "Ignore selection" and "Fix selected atoms". Check the following GIF.  
When saving in .gzmat format, Avogadro saves the molecules you draw placing the atoms in the order you drew them! When you want some atoms to be defined in specific positions keep in mind this detail! (Like dummy atoms in the middle of benzene rings or two dummy atoms in a line to be placed on an axis should be drawn first!)

<img src="https://github.com/MarcoVando/TopasAvogadroZmatrixConverter/blob/main/demo.gif" width="400" height="400" />


# Instructions
To use the script simply run the .py file.  
You just need to change the **path** to the gzmat file and the **start_matrix** variable from the .py file.  
- **start_matrix**: the line number in which first atom is written
- **path**: the file path

.pynb file (Jupyter Notebook) provides a step-by-step conversion tutorial.  



## Citation 
If you find this useful, please cite the repository using the dedicated button on the right.  
[![DOI](https://zenodo.org/badge/849603228.svg)](https://doi.org/10.5281/zenodo.14996717)
