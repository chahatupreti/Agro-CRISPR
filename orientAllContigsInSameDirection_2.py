#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 15:14:51 2021

@author: chahat
"""

# The goal of this code is to align all the contigs in the same direction so that all crisprs are identified in the same direction. That way when we later make a crispr dictionary, the spacers that are common are identifed, rather than them being reverse complements of each other. This is diffferent from the previous code with the same name since here I deal directly with the csv file that has the start and end positions, rather than making another (set of) files with the +/- sign

import io
import os
from collections import defaultdict 
import shutil


def reverse_complement(dna):
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A', 'N': 'N', 'R': 'Y', 'Y':'R', 'S':'S', 'W':'W', 'M':'K', 'K':'M', 'B':'B', 'D':'D', 'H':'H', 'V':'V'} # added 'N': 'N' as some nucleotides are N, so its best reverse complement would be N I guess? And same for B? B means C/G/T ! And D,H,V!
    return ''.join([complement[base] for base in dna[::-1]])



filewithorientations_C1animal = open("/Volumes/bam/DRG/PK/USDA_project/results/2021-09-03/C1_animal_BLAST_hits_for_orientation.csv").readlines()
filewithorientations_C1human = open("/Volumes/bam/DRG/PK/USDA_project/results/2021-09-03/C1_human_BLAST_hits_for_orientation.csv").readlines()
filewithorientations_C2animal = open("/Volumes/bam/DRG/PK/USDA_project/results/2021-09-03/C2_animal_BLAST_hits_for_orientation.csv").readlines()
filewithorientations_C2human = open("/Volumes/bam/DRG/PK/USDA_project/results/2021-09-03/C2_human_BLAST_hits_for_orientation.csv").readlines()
filewithorientations_C3animal = open("/Volumes/bam/DRG/PK/USDA_project/results/2021-09-03/C3_animal_BLAST_hits_for_orientation.csv").readlines()
filewithorientations_C3human = open("/Volumes/bam/DRG/PK/USDA_project/results/2021-09-03/C3_human_BLAST_hits_for_orientation.csv").readlines()


C1animal_contigs_address="/Volumes/bam/DRG/PK/USDA_project/results/2021-09-01/source_and_Ctype_specific_genomes/C1_animal"
C1human_contigs_address="/Volumes/bam/DRG/PK/USDA_project/results/2021-09-01/source_and_Ctype_specific_genomes/C1_human"
C2animal_contigs_address="/Volumes/bam/DRG/PK/USDA_project/results/2021-09-01/source_and_Ctype_specific_genomes/C2_animal"
C2human_contigs_address="/Volumes/bam/DRG/PK/USDA_project/results/2021-09-01/source_and_Ctype_specific_genomes/C2_human"
C3animal_contigs_address="/Volumes/bam/DRG/PK/USDA_project/results/2021-09-01/source_and_Ctype_specific_genomes/C3_animal"
C3human_contigs_address="/Volumes/bam/DRG/PK/USDA_project/results/2021-09-01/source_and_Ctype_specific_genomes/C3_human"


C1animal_contigs_address_final="/Volumes/bam/DRG/PK/USDA_project/results/2021-09-01/source_and_Ctype_specific_genomes_aligned/C1_animal"
C1human_contigs_address_final="/Volumes/bam/DRG/PK/USDA_project/results/2021-09-01/source_and_Ctype_specific_genomes_aligned/C1_human"
C2animal_contigs_address_final="/Volumes/bam/DRG/PK/USDA_project/results/2021-09-01/source_and_Ctype_specific_genomes_aligned/C2_animal"
C2human_contigs_address_final="/Volumes/bam/DRG/PK/USDA_project/results/2021-09-01/source_and_Ctype_specific_genomes_aligned/C2_human"
C3animal_contigs_address_final="/Volumes/bam/DRG/PK/USDA_project/results/2021-09-01/source_and_Ctype_specific_genomes_aligned/C3_animal"
C3human_contigs_address_final="/Volumes/bam/DRG/PK/USDA_project/results/2021-09-01/source_and_Ctype_specific_genomes_aligned/C3_human"


def orientfiles(file_with_orientation,file_location_original, file_location_final):

    genomelist=defaultdict(list)
    print(file_location_original)
    
    for i in range(1,len(file_with_orientation)):
        if file_with_orientation[i]:
            file_with_orientation[i]=file_with_orientation[i].rstrip()
            splitted=file_with_orientation[i].split(",")
            genomelist[splitted[1]]=(int(splitted[9])-int(splitted[8]))
    
    for path, dirs, files in os.walk(file_location_original):
        for file in files:
            print(file)
            if file[:-3] in genomelist and genomelist[file[:-3]]<0:
                contigfile=io.open(os.path.join(path,file)).readlines();
                firstline=contigfile[0]
                string_without_line_breaks = ""
                for line in contigfile[1:]:
                    stripped_line = line.rstrip()
                    string_without_line_breaks += stripped_line
                revcomp=reverse_complement(string_without_line_breaks)
                writefile=open(os.path.join(file_location_final,file),'w')
                writefile.write(firstline)
                writefile.write(revcomp)
                writefile.close()
            elif file[:-3] in genomelist and genomelist[file[:-3]]>0:
                shutil.copy(file_location_original+'/'+file, file_location_final)

orientfiles(filewithorientations_C1animal, C1animal_contigs_address, C1animal_contigs_address_final)
orientfiles(filewithorientations_C1human, C1human_contigs_address, C1human_contigs_address_final)
orientfiles(filewithorientations_C2animal, C2animal_contigs_address, C2animal_contigs_address_final)
orientfiles(filewithorientations_C2human, C2human_contigs_address, C2human_contigs_address_final)
orientfiles(filewithorientations_C3animal, C3animal_contigs_address, C3animal_contigs_address_final)
orientfiles(filewithorientations_C3human, C3human_contigs_address, C3human_contigs_address_final)