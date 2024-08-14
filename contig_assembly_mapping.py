#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# This code creates a mapping between the assemblies and corresponding contigs

import os
from collections import defaultdict
from time import sleep

animalcontiglist=[i[:-4].rstrip() for i in open("/Volumes/bam/DRG/PK/USDA_project/results/2021-11-26/animalcontiglist.txt").readlines()] 
animalmapping=defaultdict(list)

humancontiglist=[i[:-4].rstrip() for i in open("/Volumes/bam/DRG/PK/USDA_project/results/2021-11-26/humancontiglist.txt").readlines()] 
humanmapping=defaultdict(list)


for path, dirs, files in os.walk("/Volumes/bam/DRG/PK/USDA_project/results/2021-09-01/Efs_allanimal_temp"):
    for filename in files:
        if not filename.startswith('.'):
            assemblyfile=open(os.path.join(path,filename)).readlines()
            lineswithaccession=''
            for lin in assemblyfile:
                if lin.startswith('>'): # only saving lines that have accession numbers since other lines won't have contig names
                    lineswithaccession=lineswithaccession+' '+lin
            for contig in animalcontiglist:
                if contig in lineswithaccession: # checking if contig
                    animalmapping[filename[:-3]].append(contig)

print(animalmapping)

# save the assembly-contig mapping to a file
anfile=open("/Volumes/bam/DRG/PK/USDA_project/results/2021-11-26/animal_assembly_contig_mapping.tsv",'w')
for key,values in animalmapping.items():
    anfile.write(key+'\t'+','.join(values)+'\n')
anfile.close()
                    


for path, dirs, files in os.walk("/Volumes/bam/DRG/PK/USDA_project/results/2021-09-01/Efs_allhuman_temp"):
    for filename in files:
        if not filename.startswith('.'):
            assemblyfile=open(os.path.join(path,filename)).readlines()
            lineswithaccession=''
            for lin in assemblyfile:
                if lin.startswith('>'): 
                    lineswithaccession=lineswithaccession+' '+lin
            for contig in humancontiglist:
                if contig in lineswithaccession:
                    print('yes')
                    humanmapping[filename[:-3]].append(contig)

# save the assembly-contig mapping to a file
hufile=open("/Volumes/bam/DRG/PK/USDA_project/results/2021-11-26/human_assembly_contig_mapping.tsv",'w')
for key,values in humanmapping.items():
    hufile.write(key+'\t'+','.join(values)+'\n')
hufile.close()
    

