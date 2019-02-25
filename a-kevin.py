import re

def printArr(arr):
    for x in arr:
        print(x)

try:
    berkas = open("doc-1.txt")
    baca = berkas.read()

    format = re.sub('-', ' s.d ', baca)
    format1 = re.sub(':', '\t', format)
    cari = re.findall(r"\d+ s.d +\w+\s.*", format1)
    printArr(cari)
finally:
    berkas.close()