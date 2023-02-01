# -*- coding: utf-8 -*-
import sys
import os
sys.path.append("C:/fadi/github codes/DataProfiler")
from convert_pdf_to_TEXT import *
from convert_docx_to_txt import *
from convert_excel_to_txt import *
from convert_csv_to_txt import *
from deeplearning_test import *
from regex_test import *
from readtext import*
original_path = input("entre original file directory ")
#"C:/fadi/github codes/rdp.pdf" # pdf file path
text_path = input("entre converted file directory ")
#"C:/fadi/github codes/datataaa.txt" # converted file path
name, extension = os.path.splitext(original_path)

if extension == '.docx':
    text = convert_docx_to_txt(original_path,text_path)
elif extension == '.csv':
    text = convert_csv_to_txt(original_path,text_path)
elif extension == '.xlsx' or extension == '.xls':
    text = convert_excel_to_txt(original_path,text_path)
elif extension == '.pdf':
    text = convert_pdf_to_txt(original_path,text_path)
else:
    text = readtext(original_path)
#regex_test(text)  
result = deeplearning_test(text_path) and regex_test(text)# sensitive info result, False = Sensitive info detected !
print("REGEX RESULT")
regex_test(text)
print("FINAL RESULT",result)

#python "C:/fadi/github codes/DataProfiler/try1.py"