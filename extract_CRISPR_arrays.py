#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import distance 
import os
from collections import defaultdict



Crispr1DR="GTTTTAGAGTCATGTTGTTTAGAATGGTACCAAAAC"
Crispr2DR="GTTTTAGAGTCATGTTGTTTAGAATGGTACCAAAAC"
Crispr2DR_RevComp="GTTTTGGTACCATTCTAAACAACATGACTCTAAAAC"
Crispr3DR="GTTTTTGTACTCTCAATAATTTCTTATCAGTAAAAC"
Crispr3DR_RevComp="GTTTTACTGATAAGAAATTATTGAGAGTACAAAAAC"


C1_contigs_aligned_MDR_CC = "/Volumes/bam/DRG/PK/results/2020-07-21/crisprcasfinder_results_OG1RF"
C3_contigs_aligned_MDR_CC = "/Volumes/bam/DRG/PK/results/2020-07-21/crisprcasfinder_results_T11"
C1_contigs_aligned_nonMDR_CC= "/Volumes/bam/DRG/PK/results/2020-08-21/CCfinder_results/C1_contigs_aligned_nonMDR_CC"
C3_contigs_aligned_nonMDR_CC= "/Volumes/bam/DRG/PK/results/2020-08-21/CCfinder_results/C3_contigs_aligned_nonMDR_CC"


######################################################################

# C1 contig (MDR)
C1_Spacer_Flags=defaultdict(list)
for path, dirs, files in os.walk(C1_contigs_aligned_MDR_CC): 
    for dirr in dirs:
        #os.mkdir("/Volumes/bam/DRG/PK/results/2021-06-22/CRISPR_arrays/C1_MDR/"+dirr[:-3])
        C1_Spacer_Flags[dirr]=[0,0,0]
        Crisprs_Report=open(path+'/'+dirr+'/TSV/Crisprs_REPORT.tsv').readlines()
        Array_list = [line.strip() for line in Crisprs_Report if line.strip()]
        DRlist=[]
        for i in range(1,len(Array_list)):
            items=Array_list[i].split('\t')
            DRlist.append(items[10])

        for i in range(0,len(DRlist)):
            if distance.levenshtein(DRlist[i], Crispr1DR)<=3:
                C1_Spacer_Flags[dirr][0]=1 # flag that Crispr1 array has been found
                inputArrayFile=open(path+'/'+dirr+'/rawCRISPRs.fna').read()
                outputArrayFile=open("/Volumes/bam/DRG/PK/results/2021-06-22/CRISPR_arrays/C1_MDR/"+dirr[:-3]+'_C1_array.txt','w')
                arrays=inputArrayFile.split('>')
                for j in arrays[1:]:
                    name=j.split()
                    if name[0].endswith(str(int(i)+1)):
                        outputArrayFile.write('>'+j)                    
                        outputArrayFile.close()

            elif (distance.levenshtein(DRlist[i], Crispr3DR)<=3)or (distance.levenshtein(DRlist[i], Crispr3DR_RevComp)<=3):
                C1_Spacer_Flags[dirr][2]=1 # flag that Crispr3 array has been found
                print("Found C3 in C1!! The strain is "+dirr[:-3])
                inputArrayFile=open(path+'/'+dirr+'/rawCRISPRs.fna').read()
                outputArrayFile=open("/Volumes/bam/DRG/PK/results/2021-06-22/CRISPR_arrays/C3_MDR/"+dirr[:-3]+'_C3_array.txt','w')
                arrays=inputArrayFile.split('>')
                for j in arrays[1:]:
                    name=j.split()
                    if name[0].endswith(str(int(i)+1)):
                        outputArrayFile.write('>'+j)                    
                        outputArrayFile.close()
    break
print("C1 contig (MDR) DONE")
            
# # C3 contig (MDR)
C3_Spacer_Flags=defaultdict(list)
for path, dirs, files in os.walk(C3_contigs_aligned_MDR_CC): 
    for dirr in dirs:
        C3_Spacer_Flags[dirr]=[0,0,0]
        Crisprs_Report=open(path+'/'+dirr+'/TSV/Crisprs_REPORT.tsv').readlines()
        Array_list = [line.strip() for line in Crisprs_Report if line.strip()]
        DRlist=[]
        for i in range(1,len(Array_list)):
            items=Array_list[i].split('\t')
            DRlist.append(items[10])
        for i in range(0,len(DRlist)):
            if distance.levenshtein(DRlist[i], Crispr3DR)<=3:
                C3_Spacer_Flags[dirr][2]=1 # flag that Crispr1 array has been found
                inputArrayFile=open(path+'/'+dirr+'/rawCRISPRs.fna').read()
                outputArrayFile=open("/Volumes/bam/DRG/PK/results/2021-06-22/CRISPR_arrays/C3_MDR/"+dirr[:-3]+'_C3_array.txt','w')
                arrays=inputArrayFile.split('>')
                for j in arrays[1:]:
                    name=j.split()
                    if name[0].endswith(str(int(i)+1)):
                        outputArrayFile.write('>'+j)                    
                        outputArrayFile.close()
    break
print("C3 contig (MDR) DONE")

# # C1 contig (non-MDR)
for path, dirs, files in os.walk(C1_contigs_aligned_nonMDR_CC): 
    for dirr in dirs:
        C1_Spacer_Flags[dirr]=[0,0,0]
        Crisprs_Report=open(path+'/'+dirr+'/TSV/Crisprs_REPORT.tsv').readlines()
        Array_list = [line.strip() for line in Crisprs_Report if line.strip()]
        DRlist=[]
        for i in range(1,len(Array_list)):
            items=Array_list[i].split('\t')
            DRlist.append(items[10])

        for i in range(0,len(DRlist)):
            if distance.levenshtein(DRlist[i], Crispr1DR)<=3:
                C1_Spacer_Flags[dirr][0]=1 # flag that Crispr1 array has been found
                inputArrayFile=open(path+'/'+dirr+'/rawCRISPRs.fna').read()
                outputArrayFile=open("/Volumes/bam/DRG/PK/results/2021-06-22/CRISPR_arrays/C1_nonMDR/"+dirr[:-3]+'_C1_array.txt','w')
                arrays=inputArrayFile.split('>')
                for j in arrays[1:]:
                    name=j.split()
                    if name[0].endswith(str(int(i)+1)):
                        outputArrayFile.write('>'+j)                    
                        outputArrayFile.close()

            elif (distance.levenshtein(DRlist[i], Crispr3DR)<=3)or (distance.levenshtein(DRlist[i], Crispr3DR_RevComp)<=3):
                C1_Spacer_Flags[dirr][2]=1 # flag that Crispr3 array has been found
                inputArrayFile=open(path+'/'+dirr+'/rawCRISPRs.fna').read()
                outputArrayFile=open("/Volumes/bam/DRG/PK/results/2021-06-22/CRISPR_arrays/C3_nonMDR/"+dirr[:-3]+'_C3_array.txt','w')
                print("Found C3 in C1!! The strain is "+dirr[:-3])
                arrays=inputArrayFile.split('>')
                for j in arrays[1:]:
                    name=j.split()
                    if name[0].endswith(str(int(i)+1)):
                        outputArrayFile.write('>'+j)                    
                        outputArrayFile.close()
    break
print("C1 contig (non-MDR) DONE")
            
# # C3 contig (non-MDR)
for path, dirs, files in os.walk(C3_contigs_aligned_nonMDR_CC): 
    for dirr in dirs:
        C3_Spacer_Flags[dirr]=[0,0,0]
        Crisprs_Report=open(path+'/'+dirr+'/TSV/Crisprs_REPORT.tsv').readlines()
        Array_list = [line.strip() for line in Crisprs_Report if line.strip()]
        DRlist=[]
        for i in range(1,len(Array_list)):
            items=Array_list[i].split('\t')
            DRlist.append(items[10])
        for i in range(0,len(DRlist)):
            if distance.levenshtein(DRlist[i], Crispr3DR)<=3:
                C3_Spacer_Flags[dirr][2]=1 # flag that Crispr1 array has been found
                inputArrayFile=open(path+'/'+dirr+'/rawCRISPRs.fna').read()
                outputArrayFile=open("/Volumes/bam/DRG/PK/results/2021-06-22/CRISPR_arrays/C3_nonMDR/"+dirr[:-3]+'_C3_array.txt','w')
                arrays=inputArrayFile.split('>')
                for j in arrays[1:]:
                    name=j.split()
                    if name[0].endswith(str(int(i)+1)):
                        outputArrayFile.write('>'+j)                    
                        outputArrayFile.close()
    break
print("C3 contig (non-MDR) DONE")


######################################################################
# CRISPR2 array extraction using cydA results


C1_MDR=[]
for path, dirs, files in os.walk(C1_contigs_aligned_MDR_CC):
    for dirr in dirs:
        C1_MDR.append(dirr)

C1_nonMDR=[]
for path, dirs, files in os.walk(C1_contigs_aligned_nonMDR_CC):
    for dirr in dirs:
        C1_nonMDR.append(dirr)


C1C2_CCfinderResults="/Volumes/bam/DRG/PK/results/2020-12-10/CCfinder_results_of_cydA-C1_contigs"


# C1 contig (MDR, nonMDR)
C1_Spacer_Flags=defaultdict(list)

for path, dirs, files in os.walk(C1C2_CCfinderResults): 
    for dirr in dirs:
        Crisprs_Report=open(path+'/'+dirr+'/TSV/Crisprs_REPORT.tsv').readlines()
        Array_list = [line.strip() for line in Crisprs_Report if line.strip()]
        DRlist=[]
        for i in range(1,len(Array_list)):
            items=Array_list[i].split('\t')
            DRlist.append(items[10])
        for i in range(0,len(DRlist)):
            if distance.levenshtein(DRlist[i], Crispr2DR)<=3:
                inputArrayFile=open(path+'/'+dirr+'/rawCRISPRs.fna').read()
                if dirr in C1_MDR:
                    outputArrayFile=open("/Volumes/bam/DRG/PK/results/2021-06-22/CRISPR_arrays/C2_C1MDR/"+dirr[:-3]+'_C2_array.txt','w')
                    arrays=inputArrayFile.split('>')
                    for j in arrays[1:]:
                        name=j.split()
                        if name[0].endswith(str(int(i)+1)):
                            outputArrayFile.write('>'+j)                    
                            outputArrayFile.close()
                elif dirr in C1_nonMDR:
                    outputArrayFile=open("/Volumes/bam/DRG/PK/results/2021-06-22/CRISPR_arrays/C2_C1nonMDR/"+dirr[:-3]+'_C2_array.txt','w')
                    arrays=inputArrayFile.split('>')
                    for j in arrays[1:]:
                        name=j.split()
                        if name[0].endswith(str(int(i)+1)):
                            outputArrayFile.write('>'+j)                    
                            outputArrayFile.close()
                
    break
print("C1 contig (MDR,nonMDR) for C2 DONE")






