from Bio import SeqIO
import pandas as pd

# Archivos a analizar
file_paths = [
    "genes/fasta/hemoglobina.fasta",
    "genes/fasta/insulina.fasta",
    "genes/fasta/egfr.fasta",
    "genes/fasta/gfp.fasta",
    "genes/fasta/proteinaS.fasta",
    "genes/fasta/app.fasta",
    "genes/fasta/brca1.fasta",
    "genes/fasta/cftr.fasta",
    "genes/fasta/dmd.fasta",
    "genes/fasta/insulina.fasta",
    "genes/fasta/htt.fasta",
    "genes/genbank/hemoglobina.gb",
    "genes/genbank/insulina.gb",
    "genes/genbank/egfr.gb",
    "genes/genbank/gfp.gb",
    "genes/genbank/proteinaS.gb",
    "genes/genbank/app.gb",
    "genes/genbank/brca1.gb",
    "genes/genbank/cftr.gb",
    "genes/genbank/dmd.gb",
    "genes/genbank/insulina.gb",
    "genes/genbank/htt.gb"
]

def analyze_sequence(file_path):
    """
    Analyze sequences in a file. Supports FASTA and GenBank formats.
    """
    results = []
    # Detect file format based on extension
    file_format = "fasta" if file_path.endswith(".fasta") else "genbank"

    with open(file_path, "r") as file:
        for record in SeqIO.parse(file, file_format):
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
            results.append({
                "File": file_path.split("/")[-1],
                "ID": record.id,
                "Description": record.description,
                "Length": length,
                "Composition": composition,
                "Proportions": proportions
            })
    return results

# Análisis
analysis_results = []
for file_path in file_paths:
    analysis_results.extend(analyze_sequence(file_path))

# Convertir resultados a DataFrame
df = pd.DataFrame(analysis_results)

# Guardar resultados en un archivo CSV
df.to_csv("analysis_results.csv", index=False)
print("Análisis completado. Los resultados se han guardado en 'analysis_results.csv'.")
