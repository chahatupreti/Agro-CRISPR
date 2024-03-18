import io

blastresults=open("/Volumes/bam/DRG/PK/results/2020-10-26/cydA_BLAST_results_Refseq.csv").readlines()
orientoutput=open("/Volumes/bam/DRG/PK/results/2020-10-26/BlastHits_orientation_Refseq_cydA.csv",'w')
for line in blastresults:
    line=line.rstrip()
    splitted=line.split(',')
    ID=splitted[1]
    start=int(splitted[8])
    end=int(splitted[9])
    if start>end:
        orientoutput.write(ID+'\t'+'-'+'\n')
    if start<end:
        orientoutput.write(ID+'\t'+'+'+'\n')

orientoutput.close()