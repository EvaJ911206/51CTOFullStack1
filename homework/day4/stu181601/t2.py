#! /usr/bin/env python
#-*- 'coding:utf-8' -*-
def strNum(strtest):
    digiNum = 0
    alpNum = 0
    spcNum = 0
    othNum = 0
    for i in strtest:
        if i.isdigit() == True:
            digiNum += 1
        elif i.isalpha() == True:
            alpNum += 1
        elif i.isspace() == True:
            spcNum += 1
        else:
            othNum += 1
    print ('string digitl are %d'%(digiNum))
    print ('string alpNum are %d'%(alpNum))
    print ('string spcNum are %d'%(spcNum))
    print ('string othNum are %d'%(othNum))
    dictstr = dict((('digiNum',digiNum),('alpNum',alpNum),('spcNum',spcNum),('othNum',othNum)))
    return dictstr

while True:
    a = raw_input('please input command q:exit,other:test:')
    if a == 'q':
        break
    else:
        strt = raw_input('please input string:')
        dicstr = strNum(strt)
        print dicstr
        
                
