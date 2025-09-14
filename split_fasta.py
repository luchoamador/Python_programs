# Split fasta files based on sample coordinates groups
# Luis Amador June 2024

from Bio import SeqIO

def read_groups(group_file):
    groups = {}
    with open(group_file, 'r') as file:
        for line in file:
            group_name, seq_names = line.strip().split(':')
            groups[group_name] = seq_names.split(',')
    return groups

def split_fasta(fasta_file, groups, output_dir):
    sequences = SeqIO.to_dict(SeqIO.parse(fasta_file, "fasta"))
    for group_name, seq_names in groups.items():
        output_file = f"{output_dir}/{group_name}.fasta"
        with open(output_file, 'w') as out_handle:
            for seq_name in seq_names:
                if seq_name in sequences:
                    SeqIO.write(sequences[seq_name], out_handle, "fasta")

def main():
    fasta_file = "input.fasta"  # Replace with your input fasta file
    group_file = "groups.txt"   # Replace with your group file
    output_dir = "output"       # Replace with your desired output directory

    groups = read_groups(group_file)
    split_fasta(fasta_file, groups, output_dir)

if __name__ == "__main__":
    main()
