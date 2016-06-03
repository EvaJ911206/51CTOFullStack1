#! /usr/bin/env python
#-*- 'coding:utf-8' -*-
import os

def vesselLen(strtest):
    if strtest[0].isalnum() == False:
        filehandle = open(r'C:\t4testliuxiao.py','w+')
        writeCont = ['b =                                                       \n','nlist = []\n','for i in b:\n','\tif type(i) == type(1):#这里怎么优化\n',\
                     '\t\tcontinue\n','''\tif i == '':\n''','\t\tnum = b.index(i)\n','\t\tnlist.append(i)\n','''\t\tprint ('%s is EMPTY'%(num))\n''',\
                     '\tfor j in i:\n','''\t\tif j == ' ':\n''','\t\t\tnum = b.index(i)\n','\t\t\tnlist.append(i)\n','''\t\t\tprint ('%s is EMPTY'%(num))\n''',\
                     'if len(nlist) == 0:\n','''\tprint 'not empty element'\n''']
        
        filehandle.writelines(writeCont)
        filehandle.flush()
        #strtest = raw_input('please input vel')
        filehandle.seek(4)
        filehandle.write(strtest)
        filehandle.close()
        print 'tttttttttttttttttttttttttttttttttaa'
        a = os.popen(r'python C:\t4testliuxiao.py')
        t = a.read()
        print '111111111111111111111111111111111111111'
        return t
    else:
        nlist = []
        for i in strtest:
            for j in i:
                if j == ' ':
                    num = strtest.index(i)
                    nlist.append(i)
                    print ('%s is EMPTY'%(num))
        if len(nlist) == 0:
            return 'not empty element'
while True:
    a = raw_input('please input command q:exit,other:test:')
    if a == 'q':
        break
    else:
        strtest = raw_input('please input vessel:')
        justr = vesselLen(strtest)
        print justr
###问题：已经将子文件单独运行，可以测试通过。但为什么在主程序中就运行时就没有返回值？？？？？？？？？？
