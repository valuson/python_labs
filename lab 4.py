#v12
from Bio import SeqIO

file1 = "C:/Users/user\Downloads\sequence (1).gb"
file2 = "C:/Users/user\Downloads\sequence.gb"
output_file = "combined_species.gb"

with open(output_file, "w") as outfile:

    for record in SeqIO.parse(file1, "genbank"):
        SeqIO.write(record, outfile, "genbank")


    for record in SeqIO.parse(file2, "genbank"):
        SeqIO.write(record, outfile, "genbank")

print(f"Файлы успешно объединены в {output_file}.")


#лаба 4 задание 2

from Bio import SeqIO

def calculate_gc_content(sequence):

    g_count = sequence.count('G')
    c_count = sequence.count('C')
    total_count = len(sequence)
    if total_count == 0:
        return 0
    return (g_count + c_count) / total_count * 100

def main(input_file):
    records_gc = []

    for record in SeqIO.parse(input_file, "genbank"):
        gc_content = calculate_gc_content(str(record.seq))
        records_gc.append((record, gc_content))

    records_gc.sort(key=lambda x: x[1])

    for record, gc_content in records_gc:
        print(f"ID: {record.id}, GC Content: {gc_content:.2f}%, Sequence: {record.seq}")

if __name__ == "__main__":
    input_file ="C:/Users/user\PycharmProjects\PythonProject7\.venv\combined_species.gb"
    main(input_file)

#задание 3

from Bio import SeqIO


def extract_protein_sequences(input_file):
    for record in SeqIO.parse(input_file, "genbank"):

        for feature in record.features:
            if feature.type == "CDS":

                protein_id = record.id
                description = record.description
                location = feature.location
                translation = feature.qualifiers.get('translation', [''])[0]

                print(f"{protein_id}: {description}")
                print(f"Coding sequence location = [{location.start}:{location.end}]({location.strand})")
                print("Translation =")
                print(translation)
                print()


if __name__ == "__main__":
    input_file ="C:/Users/user\PycharmProjects\PythonProject7\.venv\combined_species.gb"
    extract_protein_sequences(input_file)