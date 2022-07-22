import math
import numpy as np
from pylab import plot, show, xlabel, ylabel
import random
from Bio import motifs
from Bio.Seq import Seq
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import time
import string

file1=open('C:\\Users\\HOME\\Desktop\\Project\\seqs_in_notepad\\#6.EMOPEC.txt', 'r')
x=file1.readlines()
p = [i.replace('\n','') for i in x]
new=[]
for i in range(len(p)):
	new.append(Seq(p[i].upper()))

m = motifs.create(new[:])
print(m.counts);
pwm = m.counts.normalize(pseudocounts= {'A':0.25, 'C': 0.25, 'G' : 0.25, 'T' : 0.25 })
print(pwm)
pssm = pwm.log_odds()
print(pssm)

val=[]
for i in new[:]:
                a,b, c, d, e, f = str(i)
                result = pssm[a,0] +pssm[b,1] +pssm[c,2]+pssm[d,3] +pssm[e,4] + pssm[f,5] 
                val.append([result])
print(val)
def score_cal(seq):
                a,b, c, d, e, f = seq
                result = pssm[a,0] +pssm[b,1] +pssm[c,2]+pssm[d,3] +pssm[e,4] + pssm[f,5] 
                return result
file1 = open("C:\\Users\\HOME\\Desktop\\Project\\^Mini_Project\\Score_generation\\6.EMOPEC_scores_gen.txt","w")
for i in new[:]:
        file1.writelines("\n{}\t{}".format(i, str(score_cal(str(i)))))
file1.close()
      







'''
infile1 = open('C:\\Users\\HOME\\Desktop\\Project\\seqs_in_notepad\\#2. RBS-only_E.coli_4357.txt', 'r')

instances_regdb = list()
#outputResult = list()
infile1 = open(filename1, 'r')
infile2 = open(filename2, 'r')

instances_regdb = list()
instances2_regdb = list()
#outputResult = list()

for line in infile1.readlines():
   if line == '\n':
      break
   lines = line.split(',')
   lines[1] = lines[1][:-1]
#   print lines
   instances_regdb.append(Seq(lines[1].upper()))
#   outputResult.append([float(lines[3])])
'''
'''for count, line in enumerate(infile1):
   if line == '\n':
      break
   lines = line.split(',')
   lines[count] = lines[count][0:-1]
#   print (lines)
   instances_regdb.append(Seq(lines[count].upper()))
#   outputResult.append([float(lines[3])])
'''
'''
##for line in infile2.readlines():
##   if line == '\n':
##      break
##   lines = line.split(',')
##   lines[1] = lines[1][:-1]
###   print lines
##   instances2_regdb.append(Seq(lines[1].upper()))
    '''
#infile1.close()
##infile2.close()
##instances, instances2 and outputResult -- all are instantiated for use in rest of the program



