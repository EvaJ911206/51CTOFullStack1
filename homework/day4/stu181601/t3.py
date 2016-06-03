#! /usr/bin/env python
#-*- coding:utf-8 -*-

'''def vesselLen(strtest):
    strlen = len(strtest)
    a = 'greater5' if strlen > 5 else 'less5'  ###练习三目运算
    print ('lenrth strtest is %d'%(strlen))      
    return a

while True:
    a = raw_input('please input command q:exit,other:test:')
    if a == 'q':
        break
    else:
        strt = raw_input('please input vessel:')
        justr = vesselLen(strt)
        print justr'''

print '************************* function2 **********************************'
'''while True:
    a = raw_input('please input command q:exit,other:test:')
    if a == 'q':
        break
    else:
        strt = raw_input('please input vessel:')
        vlen = lambda strtest: len(strtest)>5    ###练习lambda函数
        print vlen(strt)'''


print '************************* function3 **********************************'
# 以上只能输入字符串，3中会尝试使用一种输入序列（实际py识别也是字符串），
#方法3将其转化为真正的序列在程序中执行。
print '#','****************************************************************'
import os

def vesselLen(strtest):
    if strtest[0].isalnum() == False:
        filehandle = open(r'C:\testliuxiao.py','w+')
        writeCont = ['b =                                                                                                                           \n','''a = 'greater5' if len(b) > 5 else 'less5'\n''','''print ('lenrth strtest is %s'%(a))''']
        filehandle.writelines(writeCont)
        filehandle.flush()
        #strtest = raw_input('please input vel')
        filehandle.seek(4)
        filehandle.write(strtest)
        filehandle.close()
        a = os.popen(r'python C:\testliuxiao.py')
        t = a.read()
        print t
    else:
        strlen = len(strtest)
        at = 'greater5' if strlen > 5 else 'less5'  ###练习三目运算
        print ('lenrth strtest is %d'%(strlen))      
        return at
while True:
    a = raw_input('please input command q:exit,other:test:')
    if a == 'q':
        break
    else:
        strtest = raw_input('please input vessel:')
        justr = vesselLen(strtest)
        print justr
        

