# -*- coding: utf-8 -*-
#simple function for converting docx into txt
def convert_pdf_to_txt(file_path,path) :
    from PyPDF2 import PdfFileReader, PdfFileWriter
    pdf = PdfFileReader(file_path) 
    with open(path, 'w') as f:
        for page_num in range(pdf.numPages):
            # print('Page: {0}'.format(page_num))
            pageObj = pdf.getPage(page_num)
            try: 
                txt = pageObj.extractText()
                print(''.center(100, '-'))
            except:
                pass
            else:
                f.write('Page {0}\n'.format(page_num+1))
                f.write(''.center(100, '-'))
                f.write(txt)
        f.close()
        return(txt)