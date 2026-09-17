import os
 
with open(os.sep.join(["P:/2.B-Pro/soubor", "Text.txt"]), encoding="utf-8") as soubor:
    obsah = soubor.read()
    print(obsah)