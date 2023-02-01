# -*- coding: utf-8 -*-
#simple function for converting docx into txt
def convert_doc_to_txt(filepath,path):
    import docx2txt
    
    # Passing docx file to process function
    text = docx2txt.process(filepath)
    
    # Saving content inside docx file into output.txt file
    with open(path, "w") as txt:
    	print(text, file=txt)
    return(txt)