from xlwt import Workbook
import mysql.connector


conn = mysql.connector.connect(host='127.0.0.1',database='MySql',user='root',password='rohit123' )
cursor = conn.cursor()
sql="INSERT INTO my_vcf (Chr,Pos,Id,Ref,Alt,Qual,Filter,info,Sample) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"




wb=Workbook()
sheet1=wb.add_sheet('sheet1')
a=1
sheet1.write(0,0,'CHROM')
sheet1.write(0,1,'POS')
sheet1.write(0,2,'ID')
sheet1.write(0,3,'REF')
sheet1.write(0,4,'ALT')
sheet1.write(0,5,'QUALITY')
sheet1.write(0,6,'FILTER')
sheet1.write(0,7,'INFO')
sheet1.write(0,8,'FORMAT')
sheet1.write(0,9,'.')
sheet1.write(0,10,'SAMPLE')
with open('mutect_immediate.vcf','r') as f:         
       for line in f.readlines():
           li = line.lstrip()
           
           if not li.startswith("#") and '=' in li:
           	columns = line.strip().split('\t')
           	
           	with open('truseq.bed','r') as f2:
           		for line2 in f2.readlines():
           			li = line2.lstrip()
           			columns2 = line2.strip().split('\t')
           			if(columns[1]>=columns2[1] and columns[1]<=columns2[2]):
           				sheet1.write(a,0,columns[0])
           				sheet1.write(a,1,columns[1])
           				sheet1.write(a,2,columns[2])
           				sheet1.write(a,3,columns[3])
           				sheet1.write(a,4,columns[4])
           				sheet1.write(a,5,columns[5])
           				sheet1.write(a,6,columns[6])
           				sheet1.write(a,7,columns[7])
           				sheet1.write(a,8,columns[8])
           				sheet1.write(a,9,columns[9])
           				sheet1.write(a,10,columns[10])
           				wb.save('accepted.xls')
           				cursor.execute(sql,(columns[0], columns[1], columns[2], columns[3], columns[4], columns[7], columns[6], columns[9], columns[10]))
           				conn.commit()
           				a=a+1
conn.close()
           				
           			
               
	       
	       
	       
	       
	       	
	       		
	       		
	       		
	       		
	       			