import os
import sys
import vcf
import re

#AUTHOR: SEUNGMO LEE
input = open(sys.argv[1], "r")
gold = open(sys.argv[2], "r")
reader = vcf.Reader(input)
reader_ref = vcf.Reader(gold)
output = open(sys.argv[3], "a+")

ref = 0

for line in reader_ref:
    svlen = int(line.INFO['SVLEN'])
    ref += 1

tp = "TP"
fp = "FP"
tpCount = 0
fpCount = 0

for line in reader:
    svlen = int(line.INFO['SVLEN'])
    if tp in line.INFO['FLAG']:
        tpCount += 1
    if fp in line.INFO['FLAG']:
        fpCount += 1


prec = tpCount / (tpCount + fpCount)

sensitivity = tpCount / ref

with output as f:
        sys.stdout = f
        print(sys.argv[1]+"\n")
        print("f score: ", (2 * prec * sensitivity) / (prec + sensitivity))
        print("Precision: ", prec)
        print("Sensitivity: ", sensitivity)
        print("\n")
