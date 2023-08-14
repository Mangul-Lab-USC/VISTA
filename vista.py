import argparse
import subprocess

#AUTHOR: SEUNGMO LEE

def filter_vcfs_by_name(inputs, names):
    filtered_vcfs = []
    for name in names:
        matching_vcfs = [vcf for vcf in inputs if name in vcf]
        if not matching_vcfs:
            raise ValueError(f"No VCF file found with '{name}' in the name.")
        filtered_vcfs.extend(matching_vcfs)
    return filtered_vcfs

def merge_vcfs(inputs, sample, output_folder):
    if sample == "mouse" or sample == "human":
        script = "scripts/vista_merge.py"
    else:
        raise ValueError("Invalid sample type. Use 'mouse' or 'human'.")

    cmd = ["python", script, f"{output_folder}/VISTA.vcf"] + inputs
    subprocess.run(cmd, check=True)
    
    
def analyze_vcfs(gold_ref, threshold, output_folder):
    output_file = f"{output_folder}/modified_VISTA_{threshold}.vcf"

    compare_cmd = ["python", "scripts/compare_script.py", str(threshold), f"{output_folder}/VISTA.vcf" , gold_ref, output_file]
    subprocess.run(compare_cmd, check=True)

    print(f"Comparison for {threshold} completed. Output file: {output_file}")

    record = f"{output_folder}/summary.txt"
    summarize_cmd = ["python", "scripts/summarize2.py", output_file, gold_ref, record]
    subprocess.run(summarize_cmd, check=True)

    print(f"Summarization for {threshold} completed. Summary output file: {record}")


def vista(args):
    if len(args.inputs) < 4:
        raise ValueError("At least 4 VCF files are required for -inputs.")
    
    if args.sample == "human":
        vcf_names_to_filter = ["manta", "octopus", "delly", "genomestrip"]
        filtered_vcfs = filter_vcfs_by_name(args.inputs, vcf_names_to_filter)
    else:
        vcf_names_to_filter = ["lumpy", "manta", "clever", "popdel"]
        filtered_vcfs = filter_vcfs_by_name(args.inputs, vcf_names_to_filter)        

    merge_vcfs(filtered_vcfs, args.sample, args.output)

    if args.analysis:
        if not args.gold or not args.threshold:
            raise ValueError("Missing Gold Standard or threshold number!")
        analyze_vcfs(args.gold, args.threshold, args.output)
        
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Run VISTA \n Command: python vista.py -i [MANTA VCF] [LUMPY VCF] [DELLY VCF] [GENOMESTRIP VCF] [CLEVER VCF] [POPDEL VCF] [OCTOPUS VCF] -s [mouse or human] -o [output folder]\n Note: Input files' tool names should be all in lowercase",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    
    parser.add_argument("-i", "--inputs", nargs="+", required=True, help="Input VCF files")
    parser.add_argument("-s", "--sample", required=True, choices=["mouse", "human"], help="Sample type")
    parser.add_argument("-o", "--output", required=True, help="Output folder path")
    parser.add_argument("-g", "--gold", help="Input gold standard VCF")
    parser.add_argument("-a", "--analysis", action="store_true", help="Include statistics analysis")
    parser.add_argument("-t", "--threshold", help="Threshold for comparison")

    args = parser.parse_args()
    vista(args)
    