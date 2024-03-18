#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 13:39:38 2020

@author: chahat
"""

import os 
import io

#spacersfile_c1=open("/Volumes/bam/DRG/PK/results/2020-12-10/All_Spacers_C1.txt",'w')
#spacersfile_c2=open("/Volumes/bam/DRG/PK/results/2020-12-10/All_Spacers_C2.txt",'w')
spacerlist_c1=[]
spacerlist_c2=[]

c1mdradd="/Volumes/bam/DRG/PK/results/2020-08-21/Spacers/C1_MDR"
for path, dirs, files in os.walk(c1mdradd): 
    for file in files:
        if file!='.DS_Store':
            if 'C1' in file:
                cfile=io.open(os.path.join(path,file), encoding="utf8").readlines()
                for line in cfile:
                    if not line.startswith('>'):
           #             spacersfile_c1.write(line)
                        spacerlist_c1.append(line.rstrip())
            elif 'C2' in file:
                cfile=io.open(os.path.join(path,file), encoding="utf8").readlines()
                for line in cfile:
                    if not line.startswith('>'):
            #            spacersfile_c2.write(line)
                        spacerlist_c2.append(line.rstrip())

        
c1nonmdradd="/Volumes/bam/DRG/PK/results/2020-08-21/Spacers/C1_nonMDR"
for path, dirs, files in os.walk(c1nonmdradd): 
    for file in files:
        if file!='.DS_Store':
            if 'C1' in file:
                cfile=io.open(os.path.join(path,file), encoding="utf8").readlines()
                for line in cfile:
                    if not line.startswith('>'):
             #           spacersfile_c1.write(line)
                        spacerlist_c1.append(line.rstrip())
            elif 'C2' in file:
                cfile=io.open(os.path.join(path,file), encoding="utf8").readlines()
                for line in cfile:
                    if not line.startswith('>'):
              #          spacersfile_c2.write(line)
                        spacerlist_c2.append(line.rstrip())

#spacersfile_c3=open("/Volumes/bam/DRG/PK/results/2020-12-10/All_Spacers_C3.txt",'w')
spacerlist_c3=[]

c3mdradd="/Volumes/bam/DRG/PK/results/2020-08-21/Spacers/C3_MDR"
for path, dirs, files in os.walk(c1mdradd): 
    for file in files:
        if file!='.DS_Store':
            if 'C3' in file:
                cfile=io.open(os.path.join(path,file), encoding="utf8").readlines()
                for line in cfile:
                    if not line.startswith('>'):
 #                       spacersfile_c3.write(line)
                        spacerlist_c3.append(line.rstrip())
        
c1nonmdradd="/Volumes/bam/DRG/PK/results/2020-08-21/Spacers/C3_nonMDR"
for path, dirs, files in os.walk(c1nonmdradd): 
    for file in files:
        if file!='.DS_Store':
            if 'C3' in file:
                cfile=io.open(os.path.join(path,file), encoding="utf8").readlines()
                for line in cfile:
                    if not line.startswith('>'):
  #                      spacersfile_c3.write(line)
                        spacerlist_c3.append(line.rstrip())

print(11111111111111111111111111111111111111111)
print(len(spacerlist_c1))
print(11111111111111111111111111111111111111111)
print(len(spacerlist_c2))
print(11111111111111111111111111111111111111111)
print(len(spacerlist_c3))

C1spacer_set=set(spacerlist_c1)
C3spacer_set=set(spacerlist_c3)
C2spacer_set=set(spacerlist_c2)

print(11111111111111111111111111111111111111111)
print(len(C1spacer_set))
print(11111111111111111111111111111111111111111)
print(len(C2spacer_set))
print(11111111111111111111111111111111111111111)
print(len(C3spacer_set))

#spacersfile_c1.close()        
#spacersfile_c3.close()                
#spacersfile_c2.close()        

# 3373 c1 and c2 spacers total
# 590 c3 spacers total

# 526 and 204 after setting

totalSpacerlist=spacerlist_c1+spacerlist_c2+spacerlist_c3
print(len(totalSpacerlist))
totalSpacerSet=set(totalSpacerlist)
print(len(totalSpacerSet))
spacers_set_file=open("/Volumes/bam/DRG/PK/results/2020-12-10/All_Spacers_set.fasta",'w')
spacer_set_with_strain_name=open("/Volumes/bam/DRG/PK/results/2020-12-10/All_Spacers_set_withStrainname.fasta",'w')
count=0
for el in totalSpacerSet:
    count+=1
    print(count, el)
    spacers_set_file.write('>spacer'+str(count)+'\n')
    spacers_set_file.write(el+'\n')

lengthlist=[]
for i in list(totalSpacerSet):
    j=len(i)
    lengthlist.append(j)
    if 'NNN' in i:
        print(i)
        
lengthfile=open("/Volumes/bam/DRG/PK/results/2020-12-10/spacerlengths.txt",'w')
for i in lengthlist:
    lengthfile.write(str(i)+'\n')
    
lengthfile.close()