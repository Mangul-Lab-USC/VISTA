#! /usr/bin/evn python

import sys
import os

LUMPY_input = open(sys.argv[1], "r")
VCF_output = open(sys.argv[2], "w")

header_lines = "##fileformat=VCFv4.2\n\
##source=PARLIAMENT2\n\
##INFO=<ID=SVTYPE,Number=1,Type=String,Description=\"Type of structural variant detected\">\n\
##INFO=<ID=SVLEN,Number=1,Type=Integer,Description=\"Length of structural variant\">\n\
##INFO=<ID=END,Number=1,Type=Integer,Description=\"End position of structural variant\">\n\
#CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\tINFO\tFORMAT\tHG002\n"

VCF_output.write(header_lines)

for line in LUMPY_input.readlines():
    if "#" not in line: # making sure it's not a header line
        line = line.split()
        chromosome = line[0]
        start = line[1]
        alternate = line[4]

        #have to parse other fields for final elements
       
        end = start
        length = "."
        sv_type = ""
        info = line[7]
        info = info.split(';')
        for part in info:
            if "SVLEN=" in part and "CI" not in part and "AVG" not in part:
                length = part.replace('SVLEN=', '')
                end = int(length) + int(start)
            if "SVTYPE=" in part:
                sv_type = part.replace("SVTYPE=", "")

        if length == ".":
            length = 0
        vcf_line = "17" + "\t" + start + "\t.\t.\t" + "<DEL>" + "\t.\tPASS\tSVTYPE=" + sv_type + ";SVLEN=" + str(length) + ";END=" + str(end) + "\n"
        # if chromosome == "17" and 'INS' in sv_type and int(length) >= 50 and int(length) <= 100:
        VCF_output.write(vcf_line)

LUMPY_input.close()
VCF_output.close()
