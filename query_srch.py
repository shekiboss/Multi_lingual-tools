import os
import re
from collections import Counter
path='/home/naman/ace-0.9.24/output'
srr=r'_human_dmrs.txt'
ans_fil=[]
sans_fil=[]
tans_fil=[]

def srch():
    for filename in sorted(os.listdir(path)):
         matched = re.search(srr,filename)
         if matched:                
              os.chdir('/home/naman/ace-0.9.24/output')
              fil= open(filename,'r')
              ans_fil.append(fil.name)
    tans_fil=ans_fil
    while 1:
         ab=raw_input()
         if ab=="e":
               break
         else:
               tr_fil=[]
               for filename in sorted(os.listdir(path)):
                  matches = re.search(srr,filename)
                  if matches:                
                      os.chdir('/home/naman/ace-0.9.24/output')
                      fil= open(filename,'r')
                      inF=fil.read()
                      qwe_1 = re.search('(.+?) (?:is|not) present',ab,re.I)
                      found=qwe_1.group(1)
                      qwe_2=re.search('%s\s+(.+?) present' %re.escape(found),ab,re.I)
                      found_1=qwe_2.group(1)
                      if chk(found,found_1,inF):
                         tr_fil.append(fil.name)
         sans_fil=set(tans_fil)&set(tr_fil)
         tans_fil=sans_fil
    for a in sans_fil:
         print a
    if not sans_fil:
         print"No file found with such combinations."

    
def chk(fond,fund,inF):
     if fund=="not":
          if fond not in inF:
               return True
          else:
               return False
     elif fund=="is":
          if fond in inF:
               return True
          else:
               return False                             
                          

srch()
