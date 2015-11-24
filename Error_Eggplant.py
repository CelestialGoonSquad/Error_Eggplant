# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 21:05:15 2015

@author: Patrick C. Payne
"""
import sys
import xlrd
from pylab import *


#--------------No Need to Go beyond this point----------------------

def ImportData(filename, sheetnumb):
    global content
    global sheet
    values = []
        
    if filename.endswith('.xlsx') or filename.endswith('.xls'):
        content = xlrd.open_workbook(filename, 'r')
        
        sheet = content.sheet_by_index(sheetnumb)
        column = sheet.ncols
        row = sheet.nrows
        excel = True
    
    elif filename.endswith('.csv') or filename.endswith('.txt') or filename.endswith('.dat'):
        print r'Delimeter:  %r'% delimiter(filename)
        content = genfromtxt(filename, delimiter=delimiter(filename))
        column = len(content[0])        
        row = len(content)
        excel = False
       
    else:
        sys.exit("Wtf, mate?")  
    
           
    print '# of Columns: %d'% column
    print '# of Rows:    %d'% row       
    
    for j in range(column):
        data = []
        counter = 0
        for i in range(0, row):          
                
            try:
                data.append(float(point(i,j, excel)))                
            except:
                if counter == 0:
                    print 'Column %d title:  %s'%(j,point(i,j, excel))
                    counter +=1
                else:
                    break
                
        values.append(data)
    return values 

def delimiter(filename):
    with open(filename, 'r') as content:
        header=content.readline()
        if header.find(";")!=-1:
            return ";"
        if header.find(",")!=-1:
            return ","
        if header.find("\t")!=-1:
            return "\t"
    return "Could not detect column delimiter"

def point(i,j, excel):
    if excel:
        return sheet.cell(i,j).value
    else:
        return content[i,j]   

if __name__ == '__main__':
   main()