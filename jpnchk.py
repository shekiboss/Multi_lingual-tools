
#### Program for checking the attributes with/without  inverted comma's in japanese sentences from ACE gnerated MRS.
#### Add your sentence in japanese in path/srr and change the path at other places in the program.
#### Multiple sentences can be added to path/srr also, but they should be seperated by line spaces i.e, each should begin on a new line.
#### Output of this program is the ACE generated MRS of all the sentences along with list of attributes with/out inverted comma's among these sentences.
#############---------------------------------------------------------------------------------------###############







import os
import re
lis=[]
wit=[]
without=[]
otop=[]
def ff():
    path='path_to_ace/ace-0.9.24/'
    srr='examplejp'
    
    for filename in sorted(os.listdir(path)):
        matches = re.search(srr,filename)
        if matches:
            os.chdir(path)
            with open(filename) as fil:
                for lint in fil:
                        ifil=open('path/newjap.txt',"w+")
                        ifil.write(lint+"\n")
                        ifil.close()
                        os.chdir('path')
                        os.system('cat newjap.txt | python path/jacy/utils/jpn2yy.py >inp1.txt')
                        os.system('./ace -g jacy.dat -1yTf inp1.txt > out1.mrs')
                        lis=open('path/out1.mrs','r+')
                        otop=lis.readlines()
                        for p in otop:
                            print p           # can be deleted if MRS is not needed to be displayed.
                            
                            if '[' in p and '"' in p:
                                m=re.search('\[\s+\"(.+?)\"<\w+',p)                                
                                if m:
                                    found = m.group(1)
                                    if found in wit:
                                        break
                                    else:
                                        wit.append(found)
                            else:
                              n=re.search('\[\s+(.+?)<\w+',p)
                              if n:
                                    found = n.group(1)
                                    if found in without:
                                        break
                                    else:
                                        without.append(found)
    for a in wit:
        print '"'+a+'"'
    print '\n'
    for a in without:
        print a
ff()
