#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This code now takes a set of files created using the Overall Data excel sheet (for the 2 sources) that has col1= tab separated contigs (coming from one genome) and col2= ST of that genome. Using these files (Do all of this for both animal and human) - 
1) it makes a dictionary with contigs as the keys and the STs as the values. 
2) Next, it extracts the spacers for each contig from the files and makes another dictionary which has the contigs as the keys and spacers as the values. 
3) Then using these two dictionaries, it makes a dictionary which has STs as the key and spacers as the values. 
4) Then I make the set of spacers unique and using this last dictionary, make another one with unique spacers as the key and corresponding STs as the values. 
5)Use the final dictionary to ask questions about specific set of spacers with corresponding targets
"""



import xlrd
import os
from collections import defaultdict


# import the file that maps contigs and STs and make a dict with contigs as key and ST as values

animal_contig_ST={}
human_contig_ST={}

animal_contig_ST_input=[i.rstrip() for i in open("/Volumes/bam/DRG/PK/USDA_project/results/2021-11-26/animal_contig_ST_mapping.tsv").readlines()]
human_contig_ST_input=[i.rstrip() for i in open("/Volumes/bam/DRG/PK/USDA_project/results/2021-11-26/human_contig_ST_mapping.tsv").readlines()]

for line in animal_contig_ST_input:
    elements=line.split('\t')
    contiglist=elements[0].split(',')
    ST=elements[1]
    for c in contiglist:
        animal_contig_ST[c]=ST

for line in human_contig_ST_input:
    elements=line.split('\t')
    contiglist=elements[0].split(',')
    ST=elements[1]
    for c in contiglist:
        human_contig_ST[c]=ST


# extract the spacers for each contig from the files and makes another dictionary which has the contigs as the keys and spacers as the values. 
C1_animal_CC = "/Volumes/bam/DRG/PK/USDA_project/results/2021-10-21/Spacers/C1_animal"
C1_human_CC= "/Volumes/bam/DRG/PK/USDA_project/results/2021-10-21/Spacers/C1_human"
C2_animal_CC = "/Volumes/bam/DRG/PK/USDA_project/results/2021-10-21/Spacers/C2_animal"
C2_human_CC= "/Volumes/bam/DRG/PK/USDA_project/results/2021-10-21/Spacers/C2_human"
C3_animal_CC = "/Volumes/bam/DRG/PK/USDA_project/results/2021-10-21/Spacers/C3_animal"
C3_human_CC= "/Volumes/bam/DRG/PK/USDA_project/results/2021-10-21/Spacers/C3_human"
allspacers=[]
animal_contig_spacers={}
human_contig_spacers={}

def SpacerPerGenome(location,source,CRISPRtype):
    for path, dirs, files in os.walk(location): 
        for dirr in dirs:
            if os.path.exists(os.path.join(path,dirr,CRISPRtype+'_Spacers.txt')):
                Spacerfile=open(os.path.join(path,dirr,CRISPRtype+'_Spacers.txt')).readlines() 
                Spacerlist = [line.strip() for line in Spacerfile if (line.strip() and line.startswith('>')==False)]
                allspacers.extend(Spacerlist)
                Spacerstring = ','.join(Spacerlist)
                if source=='animal':
                    if dirr in animal_contig_spacers:
                        animal_contig_spacers[dirr]=animal_contig_spacers[dirr]+','+Spacerstring
                    else:
                        animal_contig_spacers[dirr]=Spacerstring
                if source=='human':
                    if dirr in human_contig_spacers:
                        human_contig_spacers[dirr]=human_contig_spacers[dirr]+','+Spacerstring
                    else:
                        human_contig_spacers[dirr]=Spacerstring

    

SpacerPerGenome(C1_animal_CC,'animal','C1')
SpacerPerGenome(C2_animal_CC,'animal','C2')
SpacerPerGenome(C3_animal_CC,'animal','C3')
SpacerPerGenome(C1_human_CC,'human','C1')
SpacerPerGenome(C2_human_CC,'human','C2')
SpacerPerGenome(C3_human_CC,'human','C3')


# using the above two dictionaries, make another that maps ST to spacers

animal_ST_spacers={}
human_ST_spacers={}

for key,values in animal_contig_ST.items():
    if key in animal_contig_spacers:
        if values in animal_ST_spacers: # some STs will have multiple set of spacers
            animal_ST_spacers[values]=animal_ST_spacers[values]+','+animal_contig_spacers[key]
        else:
            animal_ST_spacers[values]=animal_contig_spacers[key]
        
for key,values in human_contig_ST.items():
    if key in human_contig_spacers:
        if values in human_ST_spacers:
            human_ST_spacers[values]=human_ST_spacers[values]+','+human_contig_spacers[key]
        else:
            human_ST_spacers[values]=human_contig_spacers[key]
        
        

# make a final dict which has unique spacers as keys and their corresponding STs as values
uniquespacers=set(allspacers)


animal_spacer_STs=defaultdict(list)
human_spacer_STs=defaultdict(list)

for sp in uniquespacers:
    for key,values in animal_ST_spacers.items(): # need to use ,items() when values are more than one for a given key
        if sp in values:
            animal_spacer_STs[sp].append(key)
    
    for key,values in human_ST_spacers.items(): # need to use ,items() when values are more than one for a given key
        if sp in values:
            human_spacer_STs[sp].append(key)
    
print(len(animal_spacer_STs))     
print(len(human_spacer_STs))    

# save the spacer-ST mapping to a file

anfile=open("/Volumes/bam/DRG/PK/USDA_project/results/2021-11-26/animal_spacer_ST_mapping.tsv",'w')
for key,values in animal_spacer_STs.items():
    anfile.write(key+'\t'+','.join(values)+'\n')
anfile.close()
    
hufile=open("/Volumes/bam/DRG/PK/USDA_project/results/2021-11-26/human_spacer_ST_mapping.tsv",'w')
for key,values in human_spacer_STs.items():
    hufile.write(key+'\t'+','.join(values)+'\n')
hufile.close()



# create an output of contig-ST-spacers


an1file=open("/Volumes/bam/DRG/PK/USDA_project/results/2021-11-26/animal_contig_ST_spacer_mapping.tsv",'w')    
for key,values in animal_contig_ST.items():
    if key in animal_contig_spacers:
        an1file.write(key+'\t'+values+'\t'+animal_contig_spacers[key]+'\n')
    else:
        an1file.write(key+'\t'+values+'\n')
an1file.close()
    
hu1file=open("/Volumes/bam/DRG/PK/USDA_project/results/2021-11-26/human_contig_ST_spacer_mapping.tsv",'w')    
for key,values in human_contig_ST.items():
    if key in human_contig_spacers:
        hu1file.write(key+'\t'+values+'\t'+human_contig_spacers[key]+'\n')
    else:
        hu1file.write(key+'\t'+values+'\n')
hu1file.close()
    
