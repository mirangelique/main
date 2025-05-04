
from Bio import SeqIO
import os
#Задание 1
#скрипт для вычисления GC-состава GenBank файлов


def calculate_gc(seq):
  #берет последовательность и считает GC-состав.
  seq = seq.upper()
  g_count = seq.count('G')
  c_count = seq.count('C')
  return float(g_count + c_count) / len(seq)

def process_gb_file(gb_file, organism="Ananas comosus"):
  #считывает GenBank файл, считает GC для каждой последовательности, фильтрует по организму и выводит отсортированные результаты.
  seqs_with_gc = []
  for rec in SeqIO.parse(gb_file, "genbank"):
    #ищет наш организм
    if organism in rec.description:
      gc = calculate_gc(rec.seq)
      seqs_with_gc.append((rec.id, rec.description, gc, str(rec.seq)))
    else:
      print("Не наш организм: %s" % rec.id)

  #сортировка
  sorted_seqs = sorted(seqs_with_gc, key=lambda x: x[2])

  for id, desc, gc, seq in sorted_seqs:
    print("%s: %s, GC = %.2f" % (id, desc, gc))

gb_file = r"d:\reflection\ananas comosus.gb"
organism = "Ananas comosus" 

process_gb_file(gb_file, organism)

#Задание 2
from Bio import SeqIO
from Bio.Seq import Seq

def translate_cds(rec, organism="Ananas comosus"):
    """
    Транслирует CDSы в GenBank записи, но только если это наш организм.
    """
    translations = []
    if organism in rec.description:
        for feat in rec.features:
            if feat.type == "CDS":
                try:
                    #собирает CDS из экзонов, если они есть
                    cds_seq = ""
                    for part in feat.location.parts:
                        sub_seq = part.extract(rec.seq)
                        if part.strand == -1:
                            sub_seq = sub_seq.reverse_complement()
                        cds_seq += str(sub_seq)

                    #учитывает codon_start, если он есть
                    codon_start = int(feat.qualifiers.get("codon_start", [1])[0]) - 1
                    cds_seq = cds_seq[codon_start:]

                    #трансляция
                    transl_table = int(feat.qualifiers.get("transl_table", [1])[0])
                    prot_seq = Seq(cds_seq).translate(table=transl_table, to_stop=True)

                    #местоположение тоже надо
                    loc = f"[{feat.location.start}:{feat.location.end}] ({'+' if feat.strand == 1 else '-'})"
                    translations.append((loc, str(prot_seq)))
                except Exception as e:
                    print(f"Ой, что-то сломалось в CDS: {e}") 
    else:
        print(f"Запись {rec.id} - не наш пациент!")

    return translations

gb_file = r"d:\reflection\ananas comosus.gb"
org = "Ananas comosus" 

#читка и вывод
for rec in SeqIO.parse(gb_file, "genbank"):
    print(f"\n{rec.id}: {rec.description}")
    translations = translate_cds(rec, org)
    for loc, prot in translations:
        print(f"CDS location = {loc}")
        print("Translation =")
        print(prot)
        print("-" * 50)

