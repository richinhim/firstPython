#coding: euc-kr
#! /usr/bin/env python
# helloworld.py

print ("�̼���")
print()
print ('����')

for i in range(1,10,3):
 print("{} dan".format(i).center(10), end="\t");
 print("{} dan".format(i+1).center(10), end="\t");
 print("{} dan".format(i+2).center(10));
 print("="*10, end="\t");
 print("="*10, end="\t");
 print("="*10);

 for j in range(1,10):
  for k in range(3):
   print("{} x {} = {}".format(i+k, j, j*(i+k)).center(10), end="\t")
  print()
 print("")
