import os
import subprocess

input_folder = "12S_seqs"   # Change folder with FASTA files
output_folder = "12S_seqs/aligned_files"

os.makedirs(output_folder, exist_ok=True)

# Get all FASTA files
fasta_files = [f for f in os.listdir(input_folder) if f.endswith(".fasta")]

for file in fasta_files:
    input_path = os.path.join(input_folder, file)
    output_path = os.path.join(output_folder, file.replace(".fasta", "_aligned.fasta"))
    
    # Run MAFFT
    subprocess.run(["mafft", "--auto", input_path], stdout=open(output_path, "w"))
