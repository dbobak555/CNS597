"""
Note: I have both Python2.7 and 3.6 installed on my machine. Flask is weird and refuses to run
      in Python3.6. So my testing for server.py occurred in Python2.7
"""
from flask import Flask, request

app = Flask(__name__)
files = list()

def datareturn():
   return 'OK'

@app.route("/api/add",methods=['POST'])
def api_add():
   req = request.get_json()
   filename = req['filename']
   hsh = req['hash']
   files.append(str(filename)+' '+str(hsh))

   return datareturn()

@app.route("/")
def root():
   return str(files)

if __name__ =='__main__':
   app.run(host='0.0.0.0',port=8080)
