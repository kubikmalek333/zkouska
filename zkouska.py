import os
 
with open(os.sep.join(["C:/Users/malek_jakub/Documents/Pro/soubor","Text.txt"]), encoding="utf-8") as soubor:
    obsah = soubor.read()
    print(obsah)