"""
Created by: Dominic Bobak
Date: 5/12/2018

NOTE: -Based on the description in the AV.jpg picture I am NOT testing the initial files
        present in the directory.
"""
from requests import request
import hashlib, time, os
import urllib3,json

def checkFile(fname,key,urls,urlr):
   print("started checking file")
   params = {'apikey':key}
   files = {'file':(fname,open(fname,'rb').read())}
   response = request("POST",urls,files=files,params=params).json()
   resource = response["resource"]
   print(resource)
   
   params = {'apikey':key,'resource':resource}
   response = request("GET",urlr,params=params).json()
   while response['response_code'] == -2: 
      time.sleep(30)
      response = request("GET",urlr,params=params).json()
   
   total = response['total']
   positives = response['positives']
   percentage = positives / total * 100
   print("File was "+percentage+" bad")
   return percentage

def serverSend(fname,hsh,urlse):
   data = {'filename':str(fname),'hash':str(hsh)}
   http = urllib3.PoolManager()
   http.request('POST',urlse,data)   
   return

apikey = ""  # deleted because this is going on github
urlscan = 'https://www.virustotal.com/vtapi/v2/file/scan'
urlreport = 'https://www.virustotal.com/vtapi/v2/file/report'
urlserv = 'http://0.0.0.0:8080/api/add'
   
files = dict()
for f in os.listdir("."):
   if os.path.isfile(f):
      try:
         fhash = hashlib.md5(open(f,'rb').read()).hexdigest()
         files.update({f:fhash}) 
      except:
         pass

print(files)
while(1):
   time.sleep(5)
   for f in os.listdir("."):
      try:
         if os.path.isfile(f):
            fhash = hashlib.md5(open(f,'rb').read()).hexdigest()
            if fhash not in files.values():
               print('New file detected: '+f)
               percent = checkFile(f,apikey,urlscan,urlreport) 
               print('here')
               if percent > 20:
                  print("A File was bad")
                  serverSend(f,fhash,urlserv)
                  os.remove(f)
                  break
               else:
                  print("File is good")
                  files.update({f:fhash})
                  print(files)
                  break 
      except:
         pass
