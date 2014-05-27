#!/usr/bin/env python
'''
File: query.py
----------------------------------------------
This program runs a query against Oracle table
'beeGenes' to show that last entry of the raw
data file, namely, the entry with gi=147907436
`has been successfully extracted.

By   : Jingxin Zhu
Date : 04/15/2014
----------------------------------------------
'''
import cx_Oracle


con = cx_Oracle.connect('Yan/yg329')
cur = con.cursor()
cur.execute('select sequence from beeGenes where gi = 147907436')
res=cur.fetchall()
print res[0][0]

cur.close()
con.close()
