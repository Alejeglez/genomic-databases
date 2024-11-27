import Bio
from Bio import SeqIO
from collections import Counter

def get_seq_records(file, format):
    seq_records = []
    for seq_record in SeqIO.parse(file, format):
        seq_records.append(seq_record)

    return seq_records

seq_records_1A3N_gp = get_seq_records("proteínas/1A3N.gp", "genbank")
seq_records_1EMA_gp = get_seq_records("proteínas/1EMA.gp", "genbank")

seq_records_1A3N_fasta = get_seq_records("proteínas/1A3N.fasta", "fasta")
seq_records_1EMA_fasta = get_seq_records("proteínas/1EMA.fasta", "fasta")

seq_records_1IVO_gp = get_seq_records("proteínas/1IVO.gp", "genbank")
seq_records_1IVO_fasta = get_seq_records("proteínas/1IVO.fasta", "fasta")

seq_records_4INS_gp = get_seq_records("proteínas/4INS.gp", "genbank")
seq_records_4INS_fasta = get_seq_records("proteínas/4INS.fasta", "fasta")

seq_records_1TFX_gp = get_seq_records("proteínas/1TFX.gp", "genbank")
seq_records_1TFX_fasta = get_seq_records("proteínas/1TFX.fasta", "fasta")

print(len(seq_records_1A3N_fasta))


def calcular_composicion_aminoacidos(secuencia):
    aminoacidos = 'ACDEFGHIKLMNPQRSTVWY'
    contador = Counter(secuencia)
    total_aminoacidos = len(secuencia)
    proporciones = {}
    
    for aa in aminoacidos:
        proporciones[aa] = contador[aa] / total_aminoacidos if total_aminoacidos > 0 else 0
    
    return proporciones

for seq_record in seq_records_1A3N_fasta:
    print(seq_record.description)
    print(f"Longitud de la secuencia: {len(seq_record)}")
    composicion = calcular_composicion_aminoacidos(seq_record.seq)
    composicion = dict(sorted(composicion.items(), key=lambda item: item[1], reverse=True))
    print("Proporción de aminoácidos:")
    for aa, proporcion in composicion.items():
        print(f"{aa}: {proporcion:.4f}")

for seq_record in seq_records_1EMA_fasta:
    print(seq_record.description)
    print(f"Longitud de la secuencia: {len(seq_record)}")
    composicion = calcular_composicion_aminoacidos(seq_record.seq)
    composicion = dict(sorted(composicion.items(), key=lambda item: item[1], reverse=True))
    print("Proporción de aminoácidos:")
    for aa, proporcion in composicion.items():
        print(f"{aa}: {proporcion:.4f}")

for seq_record in seq_records_1IVO_fasta:
    print(seq_record.description)
    print(f"Longitud de la secuencia: {len(seq_record)}")
    composicion = calcular_composicion_aminoacidos(seq_record.seq)
    composicion = dict(sorted(composicion.items(), key=lambda item: item[1], reverse=True))
    print("Proporción de aminoácidos:")
    for aa, proporcion in composicion.items():
        print(f"{aa}: {proporcion:.4f}")

for seq_record in seq_records_4INS_fasta:
    print(seq_record.description)
    print(f"Longitud de la secuencia: {len(seq_record)}")
    composicion = calcular_composicion_aminoacidos(seq_record.seq)
    print("Proporción de aminoácidos:")
    for aa, proporcion in composicion.items():
        print(f"{aa}: {proporcion:.4f}")

for seq_record in seq_records_1TFX_fasta:
    print(seq_record.description)
    print(f"Longitud de la secuencia: {len(seq_record)}")
    composicion = calcular_composicion_aminoacidos(seq_record.seq)
    composicion = dict(sorted(composicion.items(), key=lambda item: item[1], reverse=True))
    print("Proporción de aminoácidos:")
    for aa, proporcion in composicion.items():
        print(f"{aa}: {proporcion:.4f}")