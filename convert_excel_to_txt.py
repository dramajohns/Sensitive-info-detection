# -*- coding: utf-8 -*-
#simple function for converting excel into txt
def convert_excel_to_txt(filepath,path) :
    import pandas as pd
    df = pd.read_excel(filepath)
    with open(path,"w") as txt:
        df.to_string(txt)
    return(txt)