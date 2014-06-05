#!/usr/bin/env python
'''
File: dataInput_dynamic.cgi
--------------------------------------------------
This part reads in datafile acquired from webpage,
process data, store results into Oracle table,
and make a new webpage indicating the finish of
all above work.

By   : Jingxin Zhu 
Date : 04/10/2014
--------------------------------------------------
'''
import cgi
import cx_Oracle

def main(): 
    form = cgi.FieldStorage()   # cgi script line
    # correspond to the name of text field of 'fileInput.html' file
    theStr = form.getfirst('thePath', '') 
    contents = processInput(theStr)
    print contents

def processInput(theFile):

    # 1. Read in the contents of the data file.
    with open(theFile, 'r') as f:
        # substring which will be inserted as starting position
        # of a gene sequence
        START_STRING = '_**gene_seq_starts_here**_'  
        strL = '' 
        for line in f:
            strL += line.strip('\r\n')

    # 2. Insert starting string right before the 
    #    nucleotide sequence of every bee gene.
            if '>' in line:
                strL += START_STRING 

    # 3. Extract the gi number and nucleotide seq of each gene
    totalLength = len(strL)
    end     = 0
    nGene   = strL.count('>gi')
    giList  = [] # list of all gi number
    seqList = [] # list of all gene seq 
    freq_A_List  = [] # list of all freq_A
    freq_C_List  = []
    freq_G_List  = []
    freq_T_List  = []
    freq_GC_List = []
	
    for i in range(nGene):
        # extract gi number 
        start = strL.find('>gi|',end) + 4
        end   = strL.find('|', start) 
        gi = strL[start : end]
        giList.append(gi)

    	# extract gene seq
    	start = strL.find(START_STRING, end) + len(START_STRING)
    	end = strL.find('>gi|', start)
    	if end == -1:
      	    end = totalLength
    	seq = strL[start : end]
	seqList.append(seq)

    # 4. Calculate the relative frequencies of each nucleotide in every gene.
        seqLength = len(seq)
        freq_A = seq.count('A') / float(seqLength)
        freq_C = seq.count('C') / float(seqLength)
        freq_G = seq.count('G') / float(seqLength)
        freq_T = seq.count('T') / float(seqLength)
        freq_A_List.append(freq_A)
        freq_C_List.append(freq_C)
        freq_G_List.append(freq_G)
        freq_T_List.append(freq_T)

    # 5. Calculate the combined relative frequencies of the nucleotides G and C.
    	freq_GC = freq_C + freq_G
	freq_GC_List.append(freq_GC)

    # 6. Connect Python to the Oracle database system.
    # assume oracle username = python, password = welcome
    con = cx_Oracle.connect('python/welcome')
    cur = con.cursor()

    # 7. Create an Oracle table called beeGenes.
    # This table stores gi(gene id), sequence(nucleotide seq), freq_A(relative
    # frequencies of nucleotide A), freq_C, freq_G, freq_T, and
    # freq_GC_combined(combined relative frequencies of G and C),
    # sevem columns in total.
    cur.execute('drop table beeGenes')
    cur.execute('''create table beeGenes (
                   gi varchar2(10),
                   sequence clob,
                   freq_A number, 
                   freq_C number,
                   freq_G number,
                   freq_T number,
                   freq_GC number
                   )''')

    # 8. Find appropriate number for the sequence input size.
    maxGene   = max(map(len,seqList)) # 14440
    tableSize = len(giList)
    
    cur.bindarraysize = tableSize
    cur.setinputsizes(10, maxGene, float, float, float, float, float)
	
    # 9. Write the data into database table using bind variable approach
    #    and the batch writing method.
    for i in range(len(giList)):
        cur.execute('''insert into beeGenes (gi, sequence, 
                    freq_A, freq_C, freq_G, freq_T, freq_GC) values(
                    :v1, :v2, :v3, :v4, :v5, :v6, :v7)''', (giList[i], 
                    seqList[i], freq_A_List[i], freq_C_List[i], 
                    freq_G_List[i], freq_T_List[i], freq_GC_List[i]))

    con.commit()

    cur.close()
    con.close()

    return makePage('done_submission_Template.html', ('Uploading finished!'))

def fileToStr(fileName):
    ''' return a string '''
    fin = open(fileName);
    contents = fin.read();
    fin.close()
    return contents

def makePage(templateFileName, substitution):
    pageTemplate = fileToStr(templateFileName)
    return pageTemplate % substitution


# --------------------#
#    Main Function    #
# --------------------#
try:
    print 'Content-type: text/html\n\n'
    main()
except:
    cgi.print_exception()
