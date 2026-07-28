import os
import re
from collections import defaultdict

def get_atom_count(pdb_file_path):
    """
    Parses a PDB file to count the number of each atom type in Chain B.
    
    Args:
        pdb_file_path (str): Path to the PDB file
        
    Returns:
        dict: Dictionary with atom names as keys and counts as values
    """
    atom_counts = defaultdict(int)
    
    try:
        with open(pdb_file_path, 'r') as f:
            for line in f:
                # ATOM records contain the coordinate and atom data
                if line.startswith("ATOM"):
                    chain_id = line[21].strip()
                    atom_name = line[12:16].strip()
                    
                    # Filter for Chain B only
                    if chain_id == 'B':
                        atom_counts[atom_name] += 1
                
                # Stop if a TER record is reached for Chain B
                elif line.startswith("TER"):
                    # Check if we've processed any Chain B atoms
                    if len(atom_counts) > 0:
                        break
        
        return dict(atom_counts)
    
    except FileNotFoundError:
        return {"error": "File not found."}

def get_all_atom_counts(directory_path):
    """
    Processes all PDB files in a directory and returns atom counts for Chain B.
    
    Args:
        directory_path (str): Path to the directory containing PDB files
        
    Returns:
        list: List of dictionaries containing atom counts for each PDB file
    """
    atom_counts_list = []
    
    # Retrieve filenames from the directory
    filenames = os.listdir(directory_path)
    
    # Sort filenames numerically by extracting the leading integer
    # This regex matches one or more digits at the start of the string
    filenames.sort(key=lambda f: int(re.match(r'\d+', f).group()) if re.match(r'\d+', f) else float('inf'))
    
    for filename in filenames:
        file_path = os.path.join(directory_path, filename)
        
        if os.path.isfile(file_path) and filename.endswith('.pdb'):
            atom_counts = get_atom_count(file_path)
            atom_counts_list.append(atom_counts)
            print(f"Processed: {file_path}")
    
    return atom_counts_list

# Example usage:
# atom_counts = get_all_atom_counts("/path/to/pdb/directory/")
# print(atom_counts)
