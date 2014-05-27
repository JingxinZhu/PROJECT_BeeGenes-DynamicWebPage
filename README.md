PROJECT_BEEGENES
================
Analysis of Frequencies of Honeybee Genes

A project focusing on the relative frequencies of nucleotides of honeybee's genes.

Introduction:

	Genes are formed with four basic elements: adenine(A), cytosine(C),
	guanine(G) and thymine(T). These building elements are called nucleotides,
	a sequence of which forms a gene. The compositions of the nucleotides
	of genes play a great role of specifying living beings' proteins and 
	functional RNA chains. To be more specific, nucleotides' relative
	frequencies, especially the relative frequencies of C and G together, 
	are of great importance to determine the sequence of proteins and functional
	RNA. Thus, a research on the relative frequencies of nucleotides of genes
	has significant biological and potentially medical meanings.

	This project will study relative frequencies of nucleotides of honeybee's 
	genes, which integrates Python programming, Oracle database, database-driven
	dynamic web pages, and SAS data analysis.
	
Raw Data:

	honeybee_gene_sequences.txt
	
	This file is downloaded from website of National Center for Biotechnology 
	Information (NCBI), which can be accessed by:
	
		http://www.ncbi.nlm.nih.gov/

Roadmap:
	
	1. collect raw data from NCBI
	2. process collected data with Python programming
	3. store results in Oracle database through 
	   Internet featured by Python
	4. access database through internet ant Python, 
	   using database-driven dynamic web pages
	5. analyze data stored in the database with SAS 

Programming Goal: 
    1. Dynamic webpage powered by python
    2. Simple webpage design 
    3. Oracle-integrated webpage

Version info:
	1. Oracle database 11g express
	2. Python 2.7
	3. cx_Oracle module required

Main Implementation :

	1. assume oracle username = python, password = welcome
	2. run ‘localCGIServer.py’ in terminal, which will prompt 
	   ‘Localhost CGI server started’ in terminal to indicate 
	   successful setup
	3. in web browser, like IE, Chrome, Firefox, type in the 
	   following website:   
		
		http://localhost:8081/dataInput.html
	
	4. type in a full path where file ‘honeybee_gene_sequences.txt’
	   is located in computer in the webpage which is created 
	   by last step, then click ‘submit’ button
	5. after clicking ‘click to see result’ button in the new webpage,
	   another webpage will jump out to show analysis result

