import os
os.chdir('C:\Python27\Lib\site-packages\Orange\datasets')
infile=open('test-input-file.txt','r')
outfile0=open('outfile0.txt','w')
outfile1=open('outfile1.txt','w')
outfile2=open('outfile2.txt','w')
outfile3=open('outfile3.txt','w')
outfile4=open('outfile4.txt','w')
outfile5=open('outfile5.txt','w')
outfile6=open('outfile6.txt','w')

aline=infile.readline()
while aline:
    items=aline.split()
    if items[11]=='0':
        items[11]='0'
    if items[11]=='1' or items[11]=='2' or items[11]=='3' or items[11]=='4' or items[11]=='5' or items[11]=='6' or items[11]=='7':
        items[11]='1'
    if items[0]=='x':
        items[0]='\t'
    if items[1]=='x':
        items[1]='\t'
    if items[2]=='x':
        items[2]='\t'
    if items[3]=='x':
        items[3]='\t'
    if items[4]=='x':
        items[4]='\t'
    if items[5]=='x':
        items[5]='\t'
    if items[6]=='x':
        items[6]='\t'
    if items[7]=='x':
        items[7]='\t'
    if items[8]=='x':
        items[8]='\t'
    if items[9]=='x':
        items[9]='\t'
    if items[10]=='x':
        items[10]='\t'
    datalinef0=items[0]+'\t'+items[1]+'\t'+items[2]+'\t'+items[3]+'\t'+items[4]+'\t'+items[5]+'\t'+items[6]+'\t'+items[7]+'\t'+items[8]+'\t'+items[9]+'\t'+items[10]+'\t'+items[11]
    outfile0.write(datalinef0+'\n')
    
    aline=infile.readline()
   

infile.close()
outfile0.close()
outfile1.close()
outfile2.close()
outfile3.close()
outfile4.close()
outfile5.close()
outfile6.close()
