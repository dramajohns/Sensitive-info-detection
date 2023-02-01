# -*- coding: utf-8 -*-
def deeplearning_test(text_path) :
    
    import json
    from dataprofiler import Data, Profiler
    
    data = Data(text_path) # Auto-Detect & Load: CSV, AVRO, Parquet, JSON, Text, URL
    
    #print(data.data.head(5)) # Access data directly via a compatible Pandas DataFrame
    
    profile = Profiler(data) # Calculate Statistics, Entity Recognition, etc
    
    readable_report = profile.report(report_options={"output_format": "compact"})
    
    print(json.dumps(readable_report, indent=4))
    
    
    labels=["ADDRESS","BAN","CREDIT_CARD","EMAIL_ADDRESS","UUID","HASH_OR_KEY","IPV4","IPV6","MAC_ADDRESS","PHONE_NUMBER","SSN","URL","DRIVERS_LICENSE"]
    # list containing all possible sensitive info the model can detect
    doc=readable_report.get("data_stats").get("data_label").get("entity_counts").get("postprocess_char_level").keys()
    # list for all the sensitive info the model has detected in the file
    status=True# True = no sensitive info / False = sensitive info detected
    print("MODEL RESULT")
    for i in labels:# check for relevent sensitive info in the report
        if i in doc :
            print (i)
            status = False  
        else :
            status = status and True
    return(status)# return False or True