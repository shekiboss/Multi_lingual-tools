import os
import re
def ff():
    path='/home/naman/ace-0.9.24/output'
    srr=r'_human_dmrs.txt'
    ans_fil=[]
#get user input for checking in regex.
    
    print("1- check for lemma relations\n2-check for gpred-x\n3-check for gpred-e\n4-check for realpred-x\n5-check for realpred-e")
    que=eval(raw_input())
# for lemma relation check

    if que is 1:
        print "Enter one number from the following:"
        print"1.lemma-lemma:R\n 2.feat-lemma:R\n3.feat-feat:R\n4.lemma-feat:R"
        inp_1=eval(raw_input())
        if inp_1 is 1:
            print"Enter the two lemma's whose relation to be checked:"
            lem_1=raw_input()
            lem_2=raw_input()
            reg= r'\"%s\"\s+to=\"\d+"\s+\"%s\"><rargname>' %(lem_1,lem_2)
        elif inp_1 is 2:
            print"Enter the feat and lemma whose relation to be checked:"
            lem_1=raw_input()
            lem_2=raw_input()
            reg= r'%s\s+to=\"\d+"\s+\"%s\"><rargname>' %(lem_1,lem_2)
        elif inp_1 is 3:
            print"Enter the two feat's whose relation to be checked:"
            lem_1=raw_input()
            lem_2=raw_input()
            reg= r'%s\s+to=\"\d+"\s+%s><rargname>' %(lem_1,lem_2)
        elif inp_1 is 4:
            print"Enter the lemma and feat whose relation to be checked:"
            lem_1=raw_input()
            lem_2=raw_input()
            reg= r'\"%s\"\s+to=\"\d+"\s+%s><rargname>' %(lem_1,lem_2)
                
# for gpred-x checking.

    elif que is 2:
        print "enter the feature whose value is to be checked:"
        lem_1=raw_input()
        print "Cvarsort :x"
        print"num:"
        lem_2=raw_input()
        print"pers:"
        lem_3=eval(raw_input())
        print"pt:"
        lem_4=raw_input()

        reg=r'<gpred>%s</gpred><sortinfo\s+cvarsort=\"x\"\s+num=\"%s\"\s+pers=\"%u\"\s+pt=\"%s\"' %(lem_1,lem_2,lem_3,lem_4)
        
# for gpred-e checking.

    elif que is 3:
        print "enter the feature whose value is to be checked:"
        lem_1=raw_input()
        print "Cvarsort :e"
        print"mood:"
        lem_2=raw_input()
        print"perf:"
        lem_3=raw_input()
        print"prog:"
        lem_4=raw_input()
        print"sf:"
        lem_5=raw_input()
        print"tense:"
        lem_6=raw_input()

        reg=r'<gpred>%s</gpred><sortinfo\s+cvarsort=\"e\"\s+mood=\"%s\"\s+perf=\"%s\"\s+prog=\"%s\"\s+sf=\"%s\"\s+tense=\"%s\"' %(lem_1,lem_2,lem_3,lem_4,lem_5,lem_6)
# for realpred-x checking

    elif que is 4:
        print "Cvarsort :x"
        print "Enter the lemma whose value is to be checked:"
        lem_1=raw_input()
        print"pos:"
        lem_2=raw_input()
        print"sense:"
        lem_3=raw_input()
        print"num:"
        lem_5=raw_input()
        print"pers:"
        lem_6=eval(raw_input())
        if lem_3.isdigit():
             lem_3=int(lem_3)
             reg=r'<realpred\s+lemma=\"%s\"\s+pos=\"%s\"\s+sense=\"%u\"\s+/><sortinfo\s+cvarsort=\"[a-z]\"\s+ind=\"\+|-"\s+num=\"%s\"\s+pers=\"%u\"' %(lem_1,lem_2,lem_3,lem_5,lem_6)
        else:
             reg=r'<realpred\s+lemma=\"%s\"\s+pos=\"%s\"\s+sense=\"%s\"\s+/><sortinfo\s+cvarsort=\"[a-z]\"\s+num=\"%s\"\s+pers=\"%u\"' %(lem_1,lem_2,lem_3,lem_5,lem_6)

# for realpred-e checking

    elif que is 5:
        print "Cvarsort :e"
        print"Check for lemma :\n1- With sense,\n2-without sense"
        inp=eval(raw_input())
        if inp is 1:
            print "Enter the lemma whose value is to be checked:"
            lem_1=raw_input()
            print"pos:"
            lem_2=raw_input()
            print"sense:"
            lem_3=raw_input()
            print"mood:"
            lem_4=raw_input()
            print"perf:"
            lem_5=raw_input()
            print"prog:"
            lem_6=raw_input()
            print"sf:"
            lem_7=raw_input()
            print"tense:"
            lem_8=raw_input()
            if lem_3.isdigit():
                lem_3=int(lem_3)
                reg=r'<realpred\s+lemma=\"%s\"\s+pos=\"%s\"\s+sense=\"%u\"\s+/><sortinfo\s+cvarsort=\"[a-z]\"\s+mood=\"%s\"\s+perf=\"%s\"\s+prog=\"%s\"\s+sf=\"%s\"\s+tense=\"%s\"' %(lem_1,lem_2,lem_3,lem_4,lem_5,lem_6,lem_7,lem_8)
            else:
                reg=r'<realpred\s+lemma=\"%s\"\s+pos=\"%s\"\s+sense=\"%s\"\s+/><sortinfo\s+cvarsort=\"[a-z]\"\s+mood=\"%s\"\s+perf=\"%s\"\s+prog=\"%s\"\s+sf=\"%s\"\s+tense=\"%s\"' %(lem_1,lem_2,lem_3,lem_4,lem_5,lem_6,lem_7,lem_8)
        elif inp is 2:
            print "lemma:"
            lem_1=raw_input()
            print"pos:"
            lem_2=raw_input()
            print"mood:"
            lem_3=raw_input()
            print"perf:"
            lem_4=raw_input()
            print"prog:"
            lem_5=raw_input()
            print"sf:"
            lem_6=raw_input()
            print"tense:"
            lem_7=raw_input()
            reg=r'<realpred\s+lemma=\"%s\"\s+pos=\"%s\"\s+/><sortinfo\s+cvarsort=\"[a-z]\"\s+mood=\"%s\"\s+perf=\"%s\"\s+prog=\"%s\"\s+sf=\"%s\"\s+tense=\"%s\"' %(lem_1,lem_2,lem_3,lem_4,lem_5,lem_6,lem_7)

#general search/match space for all cases.
        
    for filename in sorted(os.listdir(path)):
        matches = re.search(srr,filename)
        if matches: 
            
#change directory to dmrs files direct.
            
            os.chdir('/home/naman/ace-0.9.24/output')
            fil=open(filename,"r")
            test_str=fil.read()
            
#check for match in the current dmrs file
            
            matches = re.search(reg,test_str,re.IGNORECASE)
            if matches:
                ans_fil.append(fil.name)

            fil.close
    for a in ans_fil:
        print a
    if not ans_fil:
        print "No DMRS FILE WITH DESIRED CHARACTERS."
ff()
