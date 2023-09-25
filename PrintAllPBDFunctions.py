# Import the GIMP module
from gimpfu import *

# Get the list of all PDB procedures/functions
pdb_procedures = pdb.procedures()

# Print the list of PDB procedures
for procedure_name in pdb_procedures:
    print(procedure_name)

# Print the total number of PDB procedures
print("Total number of PDB procedures:", len(pdb_procedures))
