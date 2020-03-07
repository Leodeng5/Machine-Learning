import os
os.chdir('C:\Python27\Lib\site-packages\Orange\datasets')
infile=open('test-input.txt','r')
outfile0=open('outfile0.txt','w')
outfile1=open('outfile1.txt','w')
outfile2=open('outfile2.txt','w')
outfile3=open('outfile3.txt','w')
outfile4=open('outfile4.txt','w')
outfile5=open('outfile5.txt','w')
outfile6=open('outfile6.txt','w')
#0/1
aline=infile.readline()
while aline:
    items=aline.split()
    if items[11]=='0':
        items[11]='0'
    if items[11]=='1' or items[11]=='2' or items[11]=='3' or items[11]=='4' or items[11]=='5' or items[11]=='6' or items[11]=='7':
        items[11]='1'
    if items[0]=='x':
        items[0]=''; items[1]=''; items[2]=''; items[3]=''; items[4]=''; items[5]=''
        items[6]=''; items[7]=''; items[8]=''; items[9]=''; items[10]=''
    datalinef0=items[0]+'\t'+items[1]+'\t'+items[2]+'\t'+items[3]+'\t'+items[4]+'\t'+items[5]+'\t'+items[6]+'\t'+items[7]+'\t'+items[8]+'\t'+items[9]+'\t'+items[10]+'\t'+items[11]
    outfile0.write(datalinef0+'\n')
    
    aline=infile.readline()

infile.close()

#1/2
infile=open('test-input.txt','r')
aline=infile.readline()
while aline:
    y=aline.split()
    items=aline.split()
    if items[11]=='0' or items[11]=='1':
        items[11]='1'
    if items[11]=='2' or items[11]=='3' or items[11]=='4' or items[11]=='5' or items[11]=='6' or items[11]=='7':
        items[11]='2'
    if items[0]=='x':
        items[0]=''; items[1]=''; items[2]=''; items[3]=''; items[4]=''; items[5]=''
        items[6]=''; items[7]=''; items[8]=''; items[9]=''; items[10]=''
    datalinef1=items[0]+'\t'+items[1]+'\t'+items[2]+'\t'+items[3]+'\t'+items[4]+'\t'+items[5]+'\t'+items[6]+'\t'+items[7]+'\t'+items[8]+'\t'+items[9]+'\t'+items[10]+'\t'+items[11]
    outfile1.write(datalinef1+'\n')
    aline=infile.readline()
    
infile.close()

#2/3
infile=open('test-input.txt','r')
aline=infile.readline()
while aline:
    y=aline.split()
    items=aline.split()
    if items[11]=='0' or items[11]=='1' or items[11]=='2':
        items[11]='2'
    if items[11]=='3' or items[11]=='4' or items[11]=='5' or items[11]=='6' or items[11]=='7':
        items[11]='3'
    if items[0]=='x':
        items[0]=''; items[1]=''; items[2]=''; items[3]=''; items[4]=''; items[5]=''
        items[6]=''; items[7]=''; items[8]=''; items[9]=''; items[10]=''
    datalinef2=items[0]+'\t'+items[1]+'\t'+items[2]+'\t'+items[3]+'\t'+items[4]+'\t'+items[5]+'\t'+items[6]+'\t'+items[7]+'\t'+items[8]+'\t'+items[9]+'\t'+items[10]+'\t'+items[11]
    outfile2.write(datalinef2+'\n')
    aline=infile.readline()

infile.close()

#3/4
infile=open('test-input.txt','r')
aline=infile.readline()
while aline:
    y=aline.split()
    items=aline.split()
    if items[11]=='0' or items[11]=='1' or items[11]=='2' or items[11]=='3':
        items[11]='3'
    if items[11]=='4' or items[11]=='5' or items[11]=='6' or items[11]=='7':
        items[11]='4'
    if items[0]=='x':
        items[0]=''; items[1]=''; items[2]=''; items[3]=''; items[4]=''; items[5]=''
        items[6]=''; items[7]=''; items[8]=''; items[9]=''; items[10]=''
    datalinef3=items[0]+'\t'+items[1]+'\t'+items[2]+'\t'+items[3]+'\t'+items[4]+'\t'+items[5]+'\t'+items[6]+'\t'+items[7]+'\t'+items[8]+'\t'+items[9]+'\t'+items[10]+'\t'+items[11]
    outfile3.write(datalinef3+'\n')
    aline=infile.readline()

infile.close()

#4/5
infile=open('test-input.txt','r')
aline=infile.readline()
while aline:
    y=aline.split()
    items=aline.split()
    if items[11]=='0' or items[11]=='1' or items[11]=='2' or items[11]=='3' or items[11]=='4':
        items[11]='4'
    if items[11]=='5' or items[11]=='6' or items[11]=='7':
        items[11]='5'
    if items[0]=='x':
        items[0]=''; items[1]=''; items[2]=''; items[3]=''; items[4]=''; items[5]=''
        items[6]=''; items[7]=''; items[8]=''; items[9]=''; items[10]=''
    datalinef4=items[0]+'\t'+items[1]+'\t'+items[2]+'\t'+items[3]+'\t'+items[4]+'\t'+items[5]+'\t'+items[6]+'\t'+items[7]+'\t'+items[8]+'\t'+items[9]+'\t'+items[10]+'\t'+items[11]
    outfile4.write(datalinef4+'\n')
    aline=infile.readline()

infile.close()

#5/6
infile=open('test-input.txt','r')
aline=infile.readline()
while aline:
    y=aline.split()
    items=aline.split()
    if items[11]=='0' or items[11]=='1' or items[11]=='2' or items[11]=='3' or items[11]=='4' or items[11]=='5':
        items[11]='5'
    if items[11]=='6' or items[11]=='7':
        items[11]='6'
    if items[0]=='x':
        items[0]=''; items[1]=''; items[2]=''; items[3]=''; items[4]=''; items[5]=''
        items[6]=''; items[7]=''; items[8]=''; items[9]=''; items[10]=''
    datalinef5=items[0]+'\t'+items[1]+'\t'+items[2]+'\t'+items[3]+'\t'+items[4]+'\t'+items[5]+'\t'+items[6]+'\t'+items[7]+'\t'+items[8]+'\t'+items[9]+'\t'+items[10]+'\t'+items[11]
    outfile5.write(datalinef5+'\n')
    aline=infile.readline()

infile.close()

#6/7
infile=open('test-input.txt','r')
aline=infile.readline()
while aline:
    y=aline.split()
    items=aline.split()
    if items[11]=='0' or items[11]=='1' or items[11]=='2' or items[11]=='3' or items[11]=='4' or items[11]=='5' or items[11]=='6':
        items[11]='6'
    if items[11]=='7':
        items[11]='7'
    if items[0]=='x':
        items[0]=''; items[1]=''; items[2]=''; items[3]=''; items[4]=''; items[5]=''
        items[6]=''; items[7]=''; items[8]=''; items[9]=''; items[10]=''
    datalinef6=items[0]+'\t'+items[1]+'\t'+items[2]+'\t'+items[3]+'\t'+items[4]+'\t'+items[5]+'\t'+items[6]+'\t'+items[7]+'\t'+items[8]+'\t'+items[9]+'\t'+items[10]+'\t'+items[11]
    outfile6.write(datalinef6+'\n')
    aline=infile.readline()

infile.close()

outfile0.close()
outfile1.close()
outfile2.close()
outfile3.close()
outfile4.close()
outfile5.close()
outfile6.close()

