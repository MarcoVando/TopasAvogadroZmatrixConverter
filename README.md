# TopasAvogadroZmatrixConverter
Script to convert Gaussian ZMatrix to Topas format ZMatrix. This way u can create a rigid body in Avogadro, save it as Gaussian ZMatrix and then load it into Topas.  
When saving in .gzmat format, Avogadro saves the molecules you draw placing the atoms in the order you drew them! When you want some atoms to be defined in specific positions keep in mind this detail! (Like dummy atoms in the middle of benzene rings or two dummy atoms in a line to be placed on an axis should be drawn first!)

# Instructions
To use the script simply run the .py file.  
You just need to change the **path** to the gzmat file and the **start_matrix** variable from the .py file.  
- **start_matrix**: the line number in which first atom is written
- **path**: the file path

.pynb file (Jupyter Notebook) provides a step-by-step conversion tutorial.  
