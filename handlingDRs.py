#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# This code collected direct repeats for all identified CRISPR sequences so that they can be tested as belonging to bonafide CRISPR arrays. It does this for each CRISPR subtype

import distance 
import os
from collections import defaultdict


C1_contigs_aligned_MDR_CC = "/Volumes/bam/DRG/PK/results/2020-07-21/crisprcasfinder_results_OG1RF"
C3_contigs_aligned_MDR_CC = "/Volumes/bam/DRG/PK/results/2020-07-21/crisprcasfinder_results_T11"
C1_contigs_aligned_nonMDR_CC= "/Volumes/bam/DRG/PK/results/2020-08-21/CCfinder_results/C1_contigs_aligned_nonMDR_CC"
C3_contigs_aligned_nonMDR_CC= "/Volumes/bam/DRG/PK/results/2020-08-21/CCfinder_results/C3_contigs_aligned_nonMDR_CC"
C1_AssembliesWithoutCas9Contig_MDR_CC="/Volumes/bam/DRG/PK/results/2020-08-21/CCfinder_results/C1_AssembliesWithoutCas9Contig_MDR_CC"
C1_AssembliesWithoutCas9Contig_nonMDR_CC="/Volumes/bam/DRG/PK/results/2020-08-21/CCfinder_results/C1_AssembliesWithoutCas9Contig_nonMDR_CC"
C3_AssembliesWithoutCas9Contig_MDR_CC="/Volumes/bam/DRG/PK/results/2020-08-21/CCfinder_results/C3_AssembliesWithoutCas9Contig_MDR_CC"
C3_AssembliesWithoutCas9Contig_nonMDR_CC="/Volumes/bam/DRG/PK/results/2020-08-21/CCfinder_results/C3_AssembliesWithoutCas9Contig_nonMDR_CC"


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
            #print(len(items),dirr)
            DRlist.append(items[10])
            fullDRlist.append(items[10])
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
            #print(len(items),dirr)
            DRlist.append(items[10])
            fullDRlist.append(items[10])
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
            #print(len(items),dirr)
            DRlist.append(items[10])
            fullDRlist.append(items[10])
    break
print("C3 contig (non-MDR) DONE")
