libname final oracle user='python' password='welcome';
proc cluster data=final.beeGenes 
method=ward ccc pseudo
outtree=tree;
var freq_A freq_T freq_CG;
run;
