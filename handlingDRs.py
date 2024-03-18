#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 23:32:15 2020

@author: chahat
"""

import distance 
import os
from collections import defaultdict


#print(distance.levenshtein("GTTTTAGAGTCATGTTGTTTAGAATGGTACCAAAACT", "AGTTTTGGTACCATTCTAAACAACATGACTCTAAAAC"))

Crispr1DR="GTTTTAGAGTCATGTTGTTTAGAATGGTACCAAAAC"
Crispr2DR="GTTTTAGAGTCATGTTGTTTAGAATGGTACCAAAAC"
Crispr2DR_RevComp="GTTTTGGTACCATTCTAAACAACATGACTCTAAAAC"
Crispr3DR="GTTTTTGTACTCTCAATAATTTCTTATCAGTAAAAC"
Crispr3DR_RevComp="GTTTTACTGATAAGAAATTATTGAGAGTACAAAAAC"


C1_contigs_aligned_MDR_CC = "/Volumes/bam/DRG/PK/results/2020-07-21/crisprcasfinder_results_OG1RF"
C3_contigs_aligned_MDR_CC = "/Volumes/bam/DRG/PK/results/2020-07-21/crisprcasfinder_results_T11"
C1_contigs_aligned_nonMDR_CC= "/Volumes/bam/DRG/PK/results/2020-08-21/CCfinder_results/C1_contigs_aligned_nonMDR_CC"
C3_contigs_aligned_nonMDR_CC= "/Volumes/bam/DRG/PK/results/2020-08-21/CCfinder_results/C3_contigs_aligned_nonMDR_CC"
C1_AssembliesWithoutCas9Contig_MDR_CC="/Volumes/bam/DRG/PK/results/2020-08-21/CCfinder_results/C1_AssembliesWithoutCas9Contig_MDR_CC"
C1_AssembliesWithoutCas9Contig_nonMDR_CC="/Volumes/bam/DRG/PK/results/2020-08-21/CCfinder_results/C1_AssembliesWithoutCas9Contig_nonMDR_CC"
C3_AssembliesWithoutCas9Contig_MDR_CC="/Volumes/bam/DRG/PK/results/2020-08-21/CCfinder_results/C3_AssembliesWithoutCas9Contig_MDR_CC"
C3_AssembliesWithoutCas9Contig_nonMDR_CC="/Volumes/bam/DRG/PK/results/2020-08-21/CCfinder_results/C3_AssembliesWithoutCas9Contig_nonMDR_CC"


# CODE TO GET NUMBER OF DR_S FOR AN IDENTIFIED CRISPR ARRAY
# for path, dirs, files in os.walk(C1_contigs_aligned_MDR_CC): 
#     for dirr in dirs:
#         DRs_folder_path=path+'/'+dirr+'/CRISPRFinderProperties/'+dirr[:-5]+'_properties/DRs'
#         No_of_DRs=len([name for name in os.listdir(DRs_folder_path) if os.path.isfile(os.path.join(DRs_folder_path, name))])
        
#         print(dirr, No_of_DRs)
#     break # to avoid going recursively into subfolders
        

# for path, dirs, files in os.walk(C3_contigs_aligned_MDR_CC): 
#     for dirr in dirs:
#         DRs_folder_path=path+'/'+dirr+'/CRISPRFinderProperties/'+dirr[:-5]+'_properties/DRs'
#         No_of_DRs=len([name for name in os.listdir(DRs_folder_path) if os.path.isfile(os.path.join(DRs_folder_path, name))])
#         print(dirr, No_of_DRs)
#     break # to avoid going recursively into subfolders


# WE DONT REALLY NEED THE ABOVE CODE ACTUALLY, SINCE I CAN JUST USE THE CRIPRS_REPORT FILE THAT HAS INFO FOR EACH IDENTIFIED ARRAY






######################################################################
fullDRlist=[] # contains all DRs across all files

# C1 contig (MDR)
C1_Spacer_Flags=defaultdict(list)
for path, dirs, files in os.walk(C1_contigs_aligned_MDR_CC): 
    for dirr in dirs:
        os.mkdir("/Volumes/bam/DRG/PK/results/2020-08-21/Spacers/C1_MDR/"+dirr[:-3])
        C1_Spacer_Flags[dirr]=[0,0,0]
        Crisprs_Report=open(path+'/'+dirr+'/TSV/Crisprs_REPORT.tsv').readlines()
        Array_list = [line.strip() for line in Crisprs_Report if line.strip()]
        DRlist=[]
        for i in range(1,len(Array_list)):
            items=Array_list[i].split('\t')
            #print(len(items),dirr)
            DRlist.append(items[10])
            fullDRlist.append(items[10])
        # for i in range(0,len(DRlist)):
        #     if distance.levenshtein(DRlist[i], Crispr1DR)<=3:
        #         C1_Spacer_Flags[dirr][0]=1 # flag that Crispr1 array has been found
        #         inputSpFile=open(path+'/'+dirr+'/CRISPRFinderProperties/'+dirr[:-5]+'_properties/Spacers/Spacers_'+str(i+1)).read()
        #         outputSpFile=open("/Volumes/bam/DRG/PK/results/2020-08-21/Spacers/C1_MDR/"+dirr[:-3]+'/C1_Spacers.txt','w')
        #         outputSpFile.write(inputSpFile)
        #         outputSpFile.close()
        #     elif distance.levenshtein(DRlist[i], Crispr2DR_RevComp)<=3:
        #         C1_Spacer_Flags[dirr][1]=1 # flag that Crispr2 array has been found
        #         inputSpFile=open(path+'/'+dirr+'/CRISPRFinderProperties/'+dirr[:-5]+'_properties/Spacers/Spacers_'+str(i+1)).read()
        #         outputSpFile=open("/Volumes/bam/DRG/PK/results/2020-08-21/Spacers/C1_MDR/"+dirr[:-3]+'/C2_Spacers.txt','w')
        #         outputSpFile.write(inputSpFile)
        #         outputSpFile.close()
        #     elif (distance.levenshtein(DRlist[i], Crispr3DR)<=3)or (distance.levenshtein(DRlist[i], Crispr3DR_RevComp)<=3):
        #         C1_Spacer_Flags[dirr][2]=1 # flag that Crispr3 array has been found
        #         inputSpFile=open(path+'/'+dirr+'/CRISPRFinderProperties/'+dirr[:-5]+'_properties/Spacers/Spacers_'+str(i+1)).read()
        #         outputSpFile=open("/Volumes/bam/DRG/PK/results/2020-08-21/Spacers/C1_MDR/"+dirr[:-3]+'/C3_Spacers.txt','w')
        #         outputSpFile.write(inputSpFile)
        #         outputSpFile.close()
    break
print("C1 contig (MDR) DONE")
            
# # C3 contig (MDR)
C3_Spacer_Flags=defaultdict(list)
for path, dirs, files in os.walk(C3_contigs_aligned_MDR_CC): 
    for dirr in dirs:
        # os.mkdir("/Volumes/bam/DRG/PK/results/2020-08-21/Spacers/C3_MDR/"+dirr[:-3])
        C3_Spacer_Flags[dirr]=[0,0,0]
        Crisprs_Report=open(path+'/'+dirr+'/TSV/Crisprs_REPORT.tsv').readlines()
        Array_list = [line.strip() for line in Crisprs_Report if line.strip()]
        DRlist=[]
        for i in range(1,len(Array_list)):
            items=Array_list[i].split('\t')
            #print(len(items),dirr)
            DRlist.append(items[10])
            fullDRlist.append(items[10])
        # for i in range(0,len(DRlist)):
        #     if distance.levenshtein(DRlist[i], Crispr3DR)<=3:
        #         C3_Spacer_Flags[dirr][2]=1 # flag that Crispr1 array has been found
        #         inputSpFile=open(path+'/'+dirr+'/CRISPRFinderProperties/'+dirr[:-5]+'_properties/Spacers/Spacers_'+str(i+1)).read()
        #         outputSpFile=open("/Volumes/bam/DRG/PK/results/2020-08-21/Spacers/C3_MDR/"+dirr[:-3]+'/C3_Spacers.txt','w')
        #         outputSpFile.write(inputSpFile)
        #         outputSpFile.close()
        #     elif (distance.levenshtein(DRlist[i], Crispr2DR)<=3)or (distance.levenshtein(DRlist[i], Crispr2DR_RevComp)<=3):
        #         C3_Spacer_Flags[dirr][1]=1 # flag that Crispr2 array has been found
        #         inputSpFile=open(path+'/'+dirr+'/CRISPRFinderProperties/'+dirr[:-5]+'_properties/Spacers/Spacers_'+str(i+1)).read()
        #         outputSpFile=open("/Volumes/bam/DRG/PK/results/2020-08-21/Spacers/C3_MDR/"+dirr[:-3]+'/C2_Spacers.txt','w')
        #         outputSpFile.write(inputSpFile)
        #         outputSpFile.close()
    break
print("C3 contig (MDR) DONE")

# # C1 contig (non-MDR)
for path, dirs, files in os.walk(C1_contigs_aligned_nonMDR_CC): 
    for dirr in dirs:
        # os.mkdir("/Volumes/bam/DRG/PK/results/2020-08-21/Spacers/C1_nonMDR/"+dirr[:-3])
        C1_Spacer_Flags[dirr]=[0,0,0]
        Crisprs_Report=open(path+'/'+dirr+'/TSV/Crisprs_REPORT.tsv').readlines()
        Array_list = [line.strip() for line in Crisprs_Report if line.strip()]
        DRlist=[]
        for i in range(1,len(Array_list)):
            items=Array_list[i].split('\t')
            #print(len(items),dirr)
            DRlist.append(items[10])
            fullDRlist.append(items[10])
        # for i in range(0,len(DRlist)):
        #     if distance.levenshtein(DRlist[i], Crispr1DR)<=3:
        #         C1_Spacer_Flags[dirr][0]=1 # flag that Crispr1 array has been found
        #         inputSpFile=open(path+'/'+dirr+'/CRISPRFinderProperties/'+dirr[:-5]+'_properties/Spacers/Spacers_'+str(i+1)).read()
        #         outputSpFile=open("/Volumes/bam/DRG/PK/results/2020-08-21/Spacers/C1_nonMDR/"+dirr[:-3]+'/C1_Spacers.txt','w')
        #         outputSpFile.write(inputSpFile)
        #         outputSpFile.close()
        #     elif distance.levenshtein(DRlist[i], Crispr2DR_RevComp)<=3:
        #         C1_Spacer_Flags[dirr][1]=1 # flag that Crispr2 array has been found
        #         inputSpFile=open(path+'/'+dirr+'/CRISPRFinderProperties/'+dirr[:-5]+'_properties/Spacers/Spacers_'+str(i+1)).read()
        #         outputSpFile=open("/Volumes/bam/DRG/PK/results/2020-08-21/Spacers/C1_nonMDR/"+dirr[:-3]+'/C2_Spacers.txt','w')
        #         outputSpFile.write(inputSpFile)
        #         outputSpFile.close()
        #     elif (distance.levenshtein(DRlist[i], Crispr3DR)<=3)or (distance.levenshtein(DRlist[i], Crispr3DR_RevComp)<=3):
        #         C1_Spacer_Flags[dirr][2]=1 # flag that Crispr3 array has been found
        #         inputSpFile=open(path+'/'+dirr+'/CRISPRFinderProperties/'+dirr[:-5]+'_properties/Spacers/Spacers_'+str(i+1)).read()
        #         outputSpFile=open("/Volumes/bam/DRG/PK/results/2020-08-21/Spacers/C1_nonMDR/"+dirr[:-3]+'/C3_Spacers.txt','w')
        #         outputSpFile.write(inputSpFile)
        #         outputSpFile.close()
    break
print("C1 contig (non-MDR) DONE")
            
# # C3 contig (non-MDR)
for path, dirs, files in os.walk(C3_contigs_aligned_nonMDR_CC): 
    for dirr in dirs:
        # os.mkdir("/Volumes/bam/DRG/PK/results/2020-08-21/Spacers/C3_nonMDR/"+dirr[:-3])
        C3_Spacer_Flags[dirr]=[0,0,0]
        Crisprs_Report=open(path+'/'+dirr+'/TSV/Crisprs_REPORT.tsv').readlines()
        Array_list = [line.strip() for line in Crisprs_Report if line.strip()]
        DRlist=[]
        for i in range(1,len(Array_list)):
            items=Array_list[i].split('\t')
            #print(len(items),dirr)
            DRlist.append(items[10])
            fullDRlist.append(items[10])
        # for i in range(0,len(DRlist)):
        #     if distance.levenshtein(DRlist[i], Crispr3DR)<=3:
        #         C3_Spacer_Flags[dirr][2]=1 # flag that Crispr1 array has been found
        #         inputSpFile=open(path+'/'+dirr+'/CRISPRFinderProperties/'+dirr[:-5]+'_properties/Spacers/Spacers_'+str(i+1)).read()
        #         outputSpFile=open("/Volumes/bam/DRG/PK/results/2020-08-21/Spacers/C3_nonMDR/"+dirr[:-3]+'/C3_Spacers.txt','w')
        #         outputSpFile.write(inputSpFile)
        #         outputSpFile.close()
        #     elif (distance.levenshtein(DRlist[i], Crispr2DR)<=3)or (distance.levenshtein(DRlist[i], Crispr2DR_RevComp)<=3):
        #         C3_Spacer_Flags[dirr][1]=1 # flag that Crispr2 array has been found
        #         inputSpFile=open(path+'/'+dirr+'/CRISPRFinderProperties/'+dirr[:-5]+'_properties/Spacers/Spacers_'+str(i+1)).read()
        #         outputSpFile=open("/Volumes/bam/DRG/PK/results/2020-08-21/Spacers/C3_nonMDR/"+dirr[:-3]+'/C2_Spacers.txt','w')
        #         outputSpFile.write(inputSpFile)
        #         outputSpFile.close()
    break
print("C3 contig (non-MDR) DONE")

#--------------------------------------------------------------
# THE ANALYSIS BELOW (OF ASSEMBLIES) IS BOTH IMPRECISE AND REDUNDANT, A BETTER METHOD OF FINDING C2 SPACERS IS USING THE CYDA CONTIG METHOD, SO WILL USE THOSE SPACERS INSTEAD OF FROM HERE

# ASSEMBLIES 
            
# # C1 Assembly (MDR)
# for path, dirs, files in os.walk(C1_AssembliesWithoutCas9Contig_MDR_CC): 
#     for dirr in dirs:
#         Crisprs_Report=open(path+'/'+dirr+'/TSV/Crisprs_REPORT.tsv').readlines()
#         Array_list = [line.strip() for line in Crisprs_Report if line.strip()]
#         DRlist=[]
#         for i in range(1,len(Array_list)):
#             items=Array_list[i].split('\t')
#             DRlist.append(items[10])
#             fullDRlist.append(items[10])
#     break
# print("C1 assembly (MDR) DONE")
                
# # C3 Assembly (MDR)
# for path, dirs, files in os.walk(C3_AssembliesWithoutCas9Contig_MDR_CC): 
#     for dirr in dirs:
#         Crisprs_Report=open(path+'/'+dirr+'/TSV/Crisprs_REPORT.tsv').readlines()
#         Array_list = [line.strip() for line in Crisprs_Report if line.strip()]
#         DRlist=[]
#         for i in range(1,len(Array_list)):
#             items=Array_list[i].split('\t')
#             DRlist.append(items[10])
#             fullDRlist.append(items[10])
#     break
# print("C3 assembly (MDR) DONE")
                
# # C1 Assembly (non-MDR)
# for path, dirs, files in os.walk(C1_AssembliesWithoutCas9Contig_nonMDR_CC): 
#     for dirr in dirs:
#         Crisprs_Report=open(path+'/'+dirr+'/TSV/Crisprs_REPORT.tsv').readlines()
#         Array_list = [line.strip() for line in Crisprs_Report if line.strip()]
#         DRlist=[]
#         for i in range(1,len(Array_list)):
#             items=Array_list[i].split('\t')
#             DRlist.append(items[10])
#             fullDRlist.append(items[10])
#     break
# print("C1 assembly (non-MDR) DONE")
                
# # C3 Assembly (non-MDR)
# for path, dirs, files in os.walk(C3_AssembliesWithoutCas9Contig_nonMDR_CC): 
#     for dirr in dirs:
#         Crisprs_Report=open(path+'/'+dirr+'/TSV/Crisprs_REPORT.tsv').readlines()
#         Array_list = [line.strip() for line in Crisprs_Report if line.strip()]
#         DRlist=[]
#         for i in range(1,len(Array_list)):
#             items=Array_list[i].split('\t')
#             DRlist.append(items[10])
#             fullDRlist.append(items[10])
#     break
# print("C3 assembly (non-MDR) DONE")

levenDists=open("/Volumes/bam/DRG/PK/results/2020-08-21/levenshteinDistances_1.txt",'w')
for ele in fullDRlist:
    LD=distance.levenshtein(ele,Crispr1DR)
    levenDists.write(str(LD)+'\n')
levenDists.close()
                