import os
 
with open(os.sep.join(["Text.txt"]), encoding="utf-8") as soubor:
    obsah = soubor.read()
    print(obsah)