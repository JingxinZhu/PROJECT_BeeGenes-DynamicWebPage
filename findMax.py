'''
File: findMax.py 
--------------------------------
Part of STSCI 4060 Final Project.

This file finds the maximum number
of nucleotides in a range sequence.

By   : Yan Gao
Date : 05/04/2014
---------------------------------
'''

def find_max_gene(theFile):
    with open(theFile, 'r') as f:
        START_STRING = '_**gene_seq_starts_here**_'  
        strL = '' 
        for line in f:
            strL += line.strip('\r\n')
            if '>' in line:
                strL += START_STRING 

        totalLength = len(strL)
        end     = 0
        nGene   = strL.count('>gi')
        seqList = [] # list of all gene seq 

        for i in range(nGene):
            # extract gi number 
            start = strL.find('>gi|',end) + 4
            end   = strL.find('|', start) 

            # extract gene seq
            start = strL.find(START_STRING, end) + len(START_STRING)
            end = strL.find('>gi|', start)
            if end == -1:
                end = totalLength
            seq = strL[start : end]
            seqList.append(seq)
        return max(map(len, seqList))


# Main Function #
filename = 'honeybee_gene_sequences.txt'
maxGene = find_max_gene(filename)
print 'max number is', maxGene
