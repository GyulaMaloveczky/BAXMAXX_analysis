def sum_nosc_atoms(atom_counts_list):
    """
    Sums up N, O, S, and C atoms from each atom count dictionary.
    
    Args:
        atom_counts_list (list): List of dictionaries containing atom counts
        
    Returns:
        list: List of dictionaries with summed N, O, S, C counts for each PDB file
    """
    summary_list = []
    
    for atom_counts in atom_counts_list:
        # Initialize counts for this file
        summary = {'N': 0, 'O': 0, 'S': 0, 'C': 0}
        
        # Sum up the specified atom types
        for atom_name, count in atom_counts.items():
            if atom_name == 'N':
                summary['N'] = count
            elif atom_name == 'O':
                summary['O'] = count
            elif atom_name == 'S':
                summary['S'] = count
            elif atom_name == 'C':
                summary['C'] = count
        
        summary_list.append(summary)
    
    return summary_list

# Example usage:
# atom_counts = get_all_atom_counts("/path/to/pdb/directory/")
# nosc_counts = sum_nosc_atoms(atom_counts)
# print(nosc_counts)

# Alternative one-liner version:
def sum_nosc_atoms_one_liner(atom_counts_list):
    """
    One-liner version that sums up N, O, S, and C atoms.
    """
    return [
        {
            'N': atom_dict.get('N', 0),
            'O': atom_dict.get('O', 0), 
            'S': atom_dict.get('S', 0),
            'C': atom_dict.get('C', 0)
        }
        for atom_dict in atom_counts_list
    ]
