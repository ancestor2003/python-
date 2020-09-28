#功能：复制粘贴
#url：https://www.jb51.net/article/14052.htm
#-*- coding:utf-8 -*-
import sys
import os
def readFile(filename):
  file=open(filename,'r')
  s=file.read().strip()
  file.close()
  return s
def writeFile(filename,files)
  content=[]
  for f in files:
    print('reading file')
    s=readFile(f)
    print('reading file completed')
    contend.append(s)
  print('writing file')
  file=open(file,'w')
  file.write('\n/*-----This is a seperating line.-----*/\n'.join(content))
  file.close()
  print('write file completed')
filters=['.txt']
fullpath=os.getcwd()
print('opening directory',fullpath)
sys.path.append(fullpath)
files=[f for f in files if os.path.splitext(f)[1].lower() in filters]
writeFile('beaunet_be_card.sql',files)


  
