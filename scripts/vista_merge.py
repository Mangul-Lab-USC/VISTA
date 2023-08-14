import sys

#AUTHOR: SEUNGMO LEE
def merge_vcfs(input_files, output_file):
    merged_records = []
    header_lines = "##fileformat=VCFv4.2\n##source=VISTA\n##INFO=<ID=SVTYPE,Number=1,Type=String,Description=\"Type of structural variant detected\">\n##INFO=<ID=SVLEN,Number=1,Type=Integer,Description=\"Length of structural variant\">\n##INFO=<ID=END,Number=1,Type=Integer,Description=\"End position of structural variant\">\n##CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\tINFO\tFORMAT\tHG002\n"

    for i in range(len(input_files)):
        with open(input_files[i], 'r') as vcf_file:
            if i==0:
                for line in vcf_file:
                    if not line.startswith('##') and not line.startswith("#"):
                        temp = line.split()
                        info = temp[7]
                        info = info.split(';')
                        for part in info:
                            if "SVLEN=" in part and "CI" not in part:
                                length = part.replace('SVLEN=', '')
                                if int(length) >= 50 and int(length) <=100:
                                    merged_records.append(line)
                                
            if i==1:
                for line in vcf_file:
                    if not line.startswith('##') and not line.startswith("#"):
                        temp = line.split()
                        info = temp[7]
                        info = info.split(';')
                        for part in info:
                            if "SVLEN=" in part and "CI" not in part:
                                length = part.replace('SVLEN=', '')
                                if int(length) >= 100 and int(length) <=500:
                                    merged_records.append(line)
            
            if i==2:
                for line in vcf_file:
                    if not line.startswith('##') and not line.startswith("#"):
                        temp = line.split()
                        info = temp[7]
                        info = info.split(';')
                        for part in info:
                            if "SVLEN=" in part and "CI" not in part:
                                length = part.replace('SVLEN=', '')
                                if int(length) >= 500 and int(length) <=1000:
                                    merged_records.append(line)

            if i==3:
                for line in vcf_file:
                    if not line.startswith('##') and not line.startswith("#"):
                        temp = line.split()
                        info = temp[7]
                        info = info.split(';')
                        for part in info:
                            if "SVLEN=" in part and "CI" not in part:
                                length = part.replace('SVLEN=', '')
                                if int(length) >= 1000:
                                    merged_records.append(line)

    with open(output_file, 'w') as merged_vcf:
        merged_vcf.write(header_lines)
        for record_line in merged_records:
            merged_vcf.write(record_line)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python human_merger.py outputfile_name VCFs \n Input total 5 VCF Files")
    else:
        input_files = sys.argv[2:]
        output_file = sys.argv[1]

        merge_vcfs(input_files, output_file)
