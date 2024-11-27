from Bio import SeqIO
import pandas as pd

# Ruta del archivo FASTA
fasta_file_path = "genes/fasta/Arabidopsis thaliana DNA chromosome 4, contig fragment No. 17.fasta"

# Leer y analizar el archivo FASTA
fasta_data = []
with open(fasta_file_path, "r") as file:
    for record in SeqIO.parse(file, "fasta"):
        seq = record.seq
        length = len(seq)
        composition = {
            "A": seq.count("A"),
            "T": seq.count("T"),
            "C": seq.count("C"),
            "G": seq.count("G")
        }
        total_bases = sum(composition.values())
        proportions = {base: count / total_bases for base, count in composition.items()}
        fasta_data.append({
            "ID": record.id,
            "Description": record.description,
            "Length": length,
            "Composition": composition,
            "Proportions": proportions
        })

# Convertir resultados a un DataFrame
fasta_df = pd.DataFrame(fasta_data)

# Guardar resultados en un archivo CSV
fasta_df.to_csv("Arabidopsis_fasta_analysis.csv", index=False)
print("Análisis completado. Los resultados se han guardado en 'Arabidopsis_fasta_analysis.csv'.")
