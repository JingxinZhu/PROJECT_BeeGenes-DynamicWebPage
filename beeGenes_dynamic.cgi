#!/usr/bin/env python
'''
File: beeGenes_dynamic.cgi
-------------------------------------------------
This part will query into Orable table beeGenes, 
fetch the results, and make a new webpage showing 
the results.

By   : Jingxin Zhu 
Date : 04/12/2014
-------------------------------------------------
'''
import scipy as sp
import cgi
import cx_Oracle

def main():
    contents = processInput()
    print contents

def processInput():
    QUERY_SIZE = 4		# number of queries against Oracle table by webpage
	# assume oracle username = python, password = welcome
    con = cx_Oracle.connect('python/welcome')
    cur = con.cursor()
    aaList = ['A', 'C', 'G', 'T']
    fList = [() for t in range(QUERY_SIZE)]
    for i in range(QUERY_SIZE):
        myDict = {'aa': aaList[i]}
        obj = cur.execute('''select gi, freq_%(aa)s from beeGenes, 
                            (select max(freq_%(aa)s) as max%(aa)s from 
                          beeGenes) where freq_%(aa)s = max%(aa)s''' % myDict)
        for x in obj:
            fList[i] = x

    myTuple=()
    for t in range(QUERY_SIZE):
        myTuple = myTuple + fList[t]

    cur.close()
    con.close()
	return makePage('see_result_template.html', myTuple)

def fileToStr(fileName):
    fin = open(fileName);
    contents = fin.read();
    fin.close()
    return contents

def makePage(templateFileName, substitution):
    pageTemplate = fileToStr(templateFileName)
    return pageTemplate % substitution

# -------------------#
#    Main Function   #
# -------------------#
try:
    print 'Content-type: text/html\n\n'
    main()
except:
    cgi.print_exception()
