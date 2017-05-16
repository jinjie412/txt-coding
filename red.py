
import re
import glob
from WinTxtReader import readTxt
import os
def rwfun(filename):
    filename = filename.replace('\\','/')
    print(filename)
    newfile = os.path.splitext(os.path.basename(filename))[0]+'.txt'
    print(newfile)
    f = open(newfile,'w', encoding='utf-8')

    ss = readTxt(filename)
    ht = ''
    pt = re.compile(r'<tr style="">(.*?)</td><td></td><tr>')
    for i in pt.findall(ss):
        strs = i.replace('</td><td>',',')
        strs = strs.replace('<td>','')
        ht += strs
        ht += '\n'
    f.write(ht)
    f.close()

def run(text):    
    for filename in glob.glob(text):
        rwfun(filename)
        
if __name__ == '__main__':
    # run(r'E:\FeigeDownload\所有的数据库\*.html')
    rwfun(r'E:\FeigeDownload\所有的数据库\20000.html')
    print('over ... ')
