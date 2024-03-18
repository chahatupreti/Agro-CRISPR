## C1 animal
# python /Volumes/bam/DRG/PK/softwares/faSomeRecords.py -f /Volumes/bam/DRG/PK/USDA_project/annotations/All_Efs_animal_sources_combined.fasta -l /Volumes/bam/DRG/PK/USDA_project/annotations/C1_animal_headers.txt -o /Volumes/bam/DRG/PK/USDA_project/results/2021-09-01/source_and_Ctype_specific_genomes/C1_animal.fasta
# 
# cat C1_animal.fasta | awk -F ' ' '{
#         if (substr($0, 1, 1)==">") {filename=(substr($1,2) ".fa")}
#         print $0 >> filename; close (filename)
# }'
# 
#   # not having the close command leads to 'awk : too many open files' error
  



# C1 human  
python /Volumes/bam/DRG/PK/softwares/faSomeRecords.py -f /Volumes/bam/DRG/PK/USDA_project/annotations/All_Efs_human_sources_combined.fasta -l /Volumes/bam/DRG/PK/USDA_project/annotations/C1_human_headers.txt -o /Volumes/bam/DRG/PK/USDA_project/results/2021-09-01/source_and_Ctype_specific_genomes/C1_human.fasta

cd /Volumes/bam/DRG/PK/USDA_project/results/2021-09-01/source_and_Ctype_specific_genomes/C1_human
cat ../C1_human.fasta | awk -F ' ' '{
        if (substr($0, 1, 1)==">") {filename=(substr($1,2) ".fa")}
        print $0 >> filename; close (filename)
}'
  
  
# C2 animal
python /Volumes/bam/DRG/PK/softwares/faSomeRecords.py -f /Volumes/bam/DRG/PK/USDA_project/annotations/All_Efs_animal_sources_combined.fasta -l /Volumes/bam/DRG/PK/USDA_project/annotations/C2_animal_headers.txt -o /Volumes/bam/DRG/PK/USDA_project/results/2021-09-01/source_and_Ctype_specific_genomes/C2_animal.fasta

cd /Volumes/bam/DRG/PK/USDA_project/results/2021-09-01/source_and_Ctype_specific_genomes/C2_animal
cat ../C2_animal.fasta | awk -F ' ' '{
        if (substr($0, 1, 1)==">") {filename=(substr($1,2) ".fa")}
        print $0 >> filename; close (filename)
}'
  
  
# C2 human  
python /Volumes/bam/DRG/PK/softwares/faSomeRecords.py -f /Volumes/bam/DRG/PK/USDA_project/annotations/All_Efs_human_sources_combined.fasta -l /Volumes/bam/DRG/PK/USDA_project/annotations/C2_human_headers.txt -o /Volumes/bam/DRG/PK/USDA_project/results/2021-09-01/source_and_Ctype_specific_genomes/C2_human.fasta

cd /Volumes/bam/DRG/PK/USDA_project/results/2021-09-01/source_and_Ctype_specific_genomes/C2_human
cat ../C2_human.fasta | awk -F ' ' '{
        if (substr($0, 1, 1)==">") {filename=(substr($1,2) ".fa")}
        print $0 >> filename; close (filename)
}'
  
  
# C3 animal
python /Volumes/bam/DRG/PK/softwares/faSomeRecords.py -f /Volumes/bam/DRG/PK/USDA_project/annotations/All_Efs_animal_sources_combined.fasta -l /Volumes/bam/DRG/PK/USDA_project/annotations/C3_animal_headers.txt -o /Volumes/bam/DRG/PK/USDA_project/results/2021-09-01/source_and_Ctype_specific_genomes/C3_animal.fasta

cd /Volumes/bam/DRG/PK/USDA_project/results/2021-09-01/source_and_Ctype_specific_genomes/C3_animal
cat ../C3_animal.fasta | awk -F ' ' '{
        if (substr($0, 1, 1)==">") {filename=(substr($1,2) ".fa")}
        print $0 >> filename; close (filename)
}'
  
  
# C3 human  
python /Volumes/bam/DRG/PK/softwares/faSomeRecords.py -f /Volumes/bam/DRG/PK/USDA_project/annotations/All_Efs_human_sources_combined.fasta -l /Volumes/bam/DRG/PK/USDA_project/annotations/C3_human_headers.txt -o /Volumes/bam/DRG/PK/USDA_project/results/2021-09-01/source_and_Ctype_specific_genomes/C3_human.fasta

cd /Volumes/bam/DRG/PK/USDA_project/results/2021-09-01/source_and_Ctype_specific_genomes/C3_human
cat ../C3_human.fasta | awk -F ' ' '{
        if (substr($0, 1, 1)==">") {filename=(substr($1,2) ".fa")}
        print $0 >> filename; close (filename)
}'
  
  

















































# while read line
# do
#     if [[ ${line:0:1} == '>' ]]
#     then
#         outfile=${line#>}.fa
#         echo $line > "$outfile"
#     else
#         echo $line >> "$outfile"
#     fi
# done < C1_animal.fasta
  

#awk -F' ' '{if(/^>/){name=$1; print > name".fa"} else{print > name".fa"}}' C1_animal.fasta

#awk -F' ' '{if(/^>/){ name=$2" "$3" "$4; print > name".fa"}else{print > name".fa"}}' C1_animal.fasta

#awk '/^>/ {OUT=substr($0,2) ".fa";print " ">OUT}; OUT{print >OUT}' C1_animal.fasta

