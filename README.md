# VISTA: An integrated framework for structural variant discovery

VISTA is an integrated SV calling framework that leverages results of individual callers using a novel and robust filtering and merging algorithm.

## Installation

`git clone https://github.com/Addicted-to-coding/VISTA/tree/main`
`cd VISTA`

## Prerequisites
- python 3.8

`pip install PyVCF`
`pip install matplotlib`

## Usage

`python vista.py -i [MANTA VCF] [LUMPY VCF] [DELLY VCF] [GENOMESTRIP VCF] [CLEVER VCF] [POPDEL VCF] [OCTOPUS VCF] -s [mouse or human] -o [output folder]`

- Note: Input files' tool names should be all in lowercase

## EXAMPLE

- `python vista.py -i manta_HG002.vcf delly_HG002.vcf genomestrip_HG002.vcf octopus_HG002.vcf -o ./results -s human`

## Command-line Options

- `-h, --help`: Show the help message and exit.

- `-i INPUTS, --inputs`: Input VCF files to be merged

- `-s SAMPLE, --sample`: Specify the sample type, either "mouse" or "human"

- `-o OUTPUT, --output`: Ouptut folder where VISTA will be saved

- `-g GOLD, --gold`: Provide the path to a single gold standard VCF file

- `-a, --analysis`: If this flag is included, it reports statistics

- `-t, --threshold`: threshold number for comparison
