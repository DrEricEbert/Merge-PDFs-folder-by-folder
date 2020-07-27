# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 13:00:29 2020

@author: Dr Eric Ebert
"""
import os
#import pathlib
import timeit
import glob
from PyPDF2 import PdfFileMerger, PdfFileReader

path = r"c:\RootFolder"



def ScanForPDFsAndMergeByFolder():
    list_subfolders_with_paths = [f.path for f in os.scandir(path) if f.is_dir()]
    for folder in list_subfolders_with_paths:
        #if os.path.isdir(folder):
        print(folder)
        os.chdir(folder)
        pdfFiles = glob.glob("*.pdf")
        merger = PdfFileMerger()
        for file in pdfFiles:
            print(file)
            merger.append(PdfFileReader(file, 'rb'))
        
        merger.write(folder+".pdf")


print(f"Scandir:          {timeit.timeit(ScanForPDFsAndMergeByFolder, number=1000):.3f}")
