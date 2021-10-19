# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 00:49:57 2021

@author: Sukma Julia Nada
"""

masuk = list(map(int, input("Isi list angka (integer): ").strip().split()))
panjang = len(masuk)

genap = 0

for angka in masuk:
    if angka % 2 == 0:
        genap += 1

if genap > 0:
    print("List angka memiliki angka genap")
else:
    print("List angka tidak memiliki angka genap")