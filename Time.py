import re
from collections import OrderedDict

entries = OrderedDict()

# Positive cases
entries["1:10PM"] = True
entries["6:05PM"] = True
entries["10:55AM"] = True
entries["09:01 pm"] = True
entries["01:09pm"] = True
entries["2:12am"] = True
entries["5:55 am"] = True
entries["5:25 pm"] = True
entries["12:00 PM"] = True
entries["11:11 am"] = True

# Negative cases
entries["I:AM PM"] = False
entries["111:11PM"] = False
entries["13:05PM"] = False
entries["2:61PM"] = False
entries["55:00 pm"] = False
entries["0:00PM"] = False
entries["00:00PM"] = False
entries["10:10pM"] = False
entries["1:1PM"] = False
entries["01:23PMA"] = False

TP_count = 0
FP_count = 0
TN_count = 0
FN_count = 0

print("NOT MATCHED\tMATCHED\n")
for entry in entries.keys():
    
    ############### WRITE YOUR REGEX HERE #####################
    if re.search(r"WRITE YOUR REGEX HERE",entry):
    ###########################################################
        
        if entries[entry] == True:
            TP_count = TP_count+1
            print("\t\t"+entry)
        else:
            FP_count = FP_count+1
            print("\t\t"+entry)
    elif entries[entry] == False:
        TN_count = TN_count+1
        print(entry)
    else:
        FN_count = FN_count+1
        print(entry)

precision = TP_count/(TP_count+FP_count)
recall = TP_count/(TP_count+FN_count)

print("\nPrecision: "+str(precision))
print("Recall: "+str(recall))