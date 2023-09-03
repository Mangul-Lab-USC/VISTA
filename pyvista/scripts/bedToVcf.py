#! /usr/bin/evn python

import sys
import os

BED_input = open(sys.argv[1], "r")
VCF_output = open(sys.argv[2], "w")

header_lines = "##fileformat=VCFv4.2\n\
##source=LUMPY\n\
##INFO=<ID=SVTYPE,Number=1,Type=String,Description=\"Type of structural variant detected\">\n\
##INFO=<ID=SVLEN,Number=1,Type=Integer,Description=\"Length of structural variant\">\n\
##INFO=<ID=END,Number=1,Type=Integer,Description=\"End position of structural variant\">\n\
#CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\tINFO\n"

VCF_output.write(header_lines)

for line in BED_input.readlines():
    if "#" not in line: # making sure it's not a header line
        line = line.split()
        chromosome = line[0]
        start = line[1]
        end = line[2]
        length = abs(int(start)-int(end))

        vcf_line = chromosome + "\t" + start + "\t.\t.\t" + "<INS>" + "\t.\tPASS\tSVTYPE=DEL" + ";SVLEN=" + str(length) + ";END=" + str(end) + "\n"
        VCF_output.write(vcf_line)

BED_input.close()
VCF_output.close()
