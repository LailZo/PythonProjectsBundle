import PyPDF2
import sys
import os 

merger = PyPDF2.PdfMerger()

for file in os.listdir(os.curdir):
    if file.endswith(".pdf"):
        merger.append(file)
    merger.write("/Users/lailazoabi/3 python projects/Project3/combinedUniDosc.pdf")
    
