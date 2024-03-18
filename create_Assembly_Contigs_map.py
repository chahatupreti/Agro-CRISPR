#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 23:55:21 2020

@author: chahat
"""

from collections import defaultdict
import io
import os

#--------------------------------------- 
#THIS SECTION OF THE CODE CREATES THE MAP BETWEEN ASSEMBLY ID AND CORRESPONDING SCAFFOLD IDs USING THE ASSEMBLY STRUCTURE FILES FOR ALL ASSEMBLIES IN E FAECALIS (THERE ARE ABOUT 1500 ASSEMBLY FILES BEING PROCESSED HERE)
address="/Volumes/bam/DRG/PK/results/2020-06-30/EF_genome_assemblies_asm_struct"
Assembly_Contigs_accession_map=defaultdict(list)
for path, dirs, files in os.walk(address): 
    for file in files:
        if file!='.DS_Store':
            sentences = io.open(os.path.join(path,file), encoding="utf8").readlines(); 
            for s in sentences:
                if s.startswith('# RefSeq assembly accession'):
                    elements=s.split(': ')
                    RefseqAssemblyAccn=str(elements[1].rstrip())
    
                if s.__contains__('=\t'):
                    elements=s.split('\t')
                    Assembly_Contigs_accession_map[RefseqAssemblyAccn].append(str(elements[6]))

print(len(Assembly_Contigs_accession_map))
#---------------------------------------



#---------------------------------------
# THIS SECTION CREATES A LIST OF ALL IDs THAT ARE OUTPUTTED BY BLAST FOR SEARCHING AGAINST T11 CAS9 GENE AND OG1RF CAS9 GENE. SOME OF THESE IDs ARE FROM THE NR/NT SEARCH, AND OTHERS FROM THE REFSEQ SEARCH. I HAVE ONLY RESTRICTED THIS TO OUTPUTS WHERE THERE WAS A COMPLETE MATCH FOR THE CAS9 GENE. 
T11_BLASTlist=[]
t11_refseq_list_fullmatch=open("/Volumes/bam/DRG/PK/results/2020-06-25/T11_Refseq_BLAST_outputs_fullmatch.txt").readlines() # this file has the BLAST refseq results for T11, which have FULL cas9 gene in it
for line in t11_refseq_list_fullmatch:
    refseqID=line.rstrip()
    T11_BLASTlist.append(refseqID) # all BLAST IDs saved here

t11_nrnt_list=open("/Volumes/bam/DRG/PK/results/2020-06-25/T11_NRNT_BLAST_outputs.txt").readlines() # this file has the BLAST NRNT results for T11, which obviously have FULL cas9 gene in it
for line in t11_nrnt_list:
    nrntID='NZ_'+line.rstrip()
    T11_BLASTlist.append(nrntID) # all BLAST IDs saved here

OG1RF_BLASTlist=[]
OG1RF_refseq_list_fullmatch=open("/Volumes/bam/DRG/PK/results/2020-06-25/OG1RF_Refseq_BLAST_outputs_fullmatch.txt").readlines() # this file has the BLAST refseq results for OG1RF, which have FULL cas9 gene in it
for line in OG1RF_refseq_list_fullmatch:
    refseqID=line.rstrip()
    OG1RF_BLASTlist.append(refseqID) # all BLAST IDs saved here

OG1RF_nrnt_list=open("/Volumes/bam/DRG/PK/results/2020-06-25/OG1RF_NRNT_BLAST_outputs.txt").readlines() # this file has the BLAST NRNT results for OG1RF, which obviously have FULL cas9 gene in it
for line in OG1RF_nrnt_list:
    nrntID='NZ_'+line.rstrip()
    OG1RF_BLASTlist.append(nrntID) # all BLAST IDs saved here
print(len(T11_BLASTlist))
print(len(OG1RF_BLASTlist))
#---------------------------------------


#---------------------------------------
# THIS SECTION USES THE MAP OF THE FIRST SECTION AND THE LIST OF BLAST OUTPUT IDs (MOSTLY SCAFFOLDS, AND NOT COMPLETE GENOMES, EXPCEPT FOR THE NR/NT OUTPUTS), AND USES THEM BOTH TO GET THE "ASSEMBLY" IDs FOR THE BLAST OUTPUTS. ONCE WE HAVE THIS, WE CAN DOWNLOAD THE FASTA FOR THIS ASSEMBLY ID, WHICH IS SUPPOSED TO CONTAIN THE SEQUENCES OF ALL CONSTITUENT SCAFFOLDS. THIS COMPREHENSIVE 'ASSEMBLY' FASTA FILE CAN THEN BE SENT TO RESFINDER
T11_AssemblyIDs=[]
OG1RF_AssemblyIDs=[]
for contigID in T11_BLASTlist:
    assemblyID= [k for k, v in Assembly_Contigs_accession_map.items() if contigID in v]
    if assemblyID:
        T11_AssemblyIDs.append(assemblyID[0])
    else:
        print("No Assembly ID for ", contigID)

for contigID in OG1RF_BLASTlist:
    assemblyID= [k for k, v in Assembly_Contigs_accession_map.items() if contigID in v]
    if assemblyID:
        OG1RF_AssemblyIDs.append(assemblyID[0])
    else:
        print("No Assembly ID for ", contigID)
    

#print(T11_BLASTlist)
#asse=[k for k, v in Assembly_Contigs_accession_map.items() if "NZ_FP929058.1" in v]
#print(asse)
#print(T11_AssemblyIDs)
T11_AssemblyIDs_file=open("/Volumes/bam/DRG/PK/results/2020-06-30/T11_AssemblyIDs.txt", 'w')
for ID in T11_AssemblyIDs:
    T11_AssemblyIDs_file.write(ID)
    T11_AssemblyIDs_file.write("\n")
T11_AssemblyIDs_file.close()

OG1RF_AssemblyIDs_file=open("/Volumes/bam/DRG/PK/results/2020-06-30/OG1RF_AssemblyIDs.txt", 'w')
for ID in OG1RF_AssemblyIDs:
    OG1RF_AssemblyIDs_file.write(ID)
    OG1RF_AssemblyIDs_file.write("\n")
OG1RF_AssemblyIDs_file.close()    