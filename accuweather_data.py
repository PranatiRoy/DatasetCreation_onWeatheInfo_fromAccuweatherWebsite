cd="C:\\Users\\Pranati\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe"
import time
import pandas as pd
from bs4 import BeautifulSoup # for the beautiful soup we have to send the source code for the page.
from selenium import webdriver

browser=webdriver.Chrome(cd)

x=input('Enter the month you want to see temp: ').lower()
y=input('Enter The Year you want to see temp: ')

def day_Selection(m,y):
	y=int(y)
	l1=['january','march','may','july','august','october','december']
	l2=['april','june','september','november']
	if m in l1:
		t=31
	elif m in l2:
		t=30
	else:
		if y%4==0:
			t=29
		else:
			t=28
	return t

dy=day_Selection(x,y)
print(dy)

browser.get("https://www.accuweather.com/en/in/mumbai/206690/"+x+"-weather/206690?year="+y)
time.sleep(2)
pgsource=browser.page_source # return the source code
ref=BeautifulSoup(pgsource) #it refers to the soup element /translated element
selection_all=ref.findAll('a',{'class':"monthly-daypanel is-past" })
print(selection_all)
d=[]
ht=[]
lt=[]
for i in selection_all:
	date=i.find('div',{'class':"date"})
	j=date.text
	j=j.split('\t')
	k=j[6].split('\n')
	d.append(int(k[0]))
	high=i.find('div',{'class':"high"})
	k=high.text
	k=k.split('\t')
	l=k[6].split('\n')[0]
	ht.append(int(l[:-1]))
	low=i.find('div',{'class':"low"})
	m=low.text
	m=m.split('\t')
	n=m[6].split('\n')[0]
	lt.append(int(n[:-1]))
	k=j[6].split('\n')
	
for i,j in enumerate(d):
	if j==1:
		start_index=i
		break
#print(start_index)
#end_index=start_index+dy
print(d[start_index:start_index+dy])
print(ht[start_index:start_index+dy])
print(lt[start_index:start_index+dy])

dict1={'Date':d[start_index:start_index+dy],'Highest_Temp':ht[start_index:start_index+dy],'Lowest_Temp':lt[start_index:start_index+dy]}
df=pd.DataFrame(dict1)
df.to_csv("C:\\Users\\Pranati\\mumbai_"+x+"_"+y+"_temp_database.csv",index=False)
print(df)