##### Web Brute Force #####
##### CNS-380/597 Advanced Cybersecurity Automation - Ryan Haley####
"""
Dominic Bobak
CNS597 - HW3
4/21/2018
"""


'''
During your pentest you find a website that you believe to be of high value.
You decide to probe it to find any webpages it might be hiding and hopefullly
return a page with that you can use to gather contact information.

Write a script that will take in a list of file paths (you can use the txt
file provided WebPath.txt) and check them against the given website.
The script will then notify the user which link(s) were successful.

You then must scrape the webpage of any directories/files that were found and
return any phone numbers and email addresses you find on the page.

NOTE: This problem is only to be done against the given URL.
'''

from requests import request
import re

"""
This function tries pages that are inputted to it on the URL.
   - Takes the base URL and a string to try as input
   - returns True if the page was valid
   - returns False if the page was invalid
"""
def trypage(url,pageToCheck):
   response = request("GET",url+'/'+pageToCheck,verify=False) #get the webpage
   
   if response.status_code == 200: #if the page is valid return true, else return false
      return True
   else:
      return False

"""
This function scrapes webpages for phone numbers and email addresses.
   - takes the base URL and a list of pages as input
   - Loops through all pages twice, once for Phone Number Regex (regphone) and once for 
     Email Address Regex (regemail)
   - Prints out any phone numbers and email addresses that it finds
"""
def getAndScrub(url,pages):
   regphone = '\d{3}\-\d{3}\-\d{4}|\(\d{3}\)\ \d{3}\-\d{4}' #regex for phone numbers
   regemail = '[\w\.-]+@[\w\.-]+' #taken from stack overflow. Link: https://stackoverflow.com/questions/18119990/finding-email-address-in-a-web-page-using-regular-expression
   
   for page in pages: #perform the regex routine for phone numbers on all good pages
      print('\n')
      print("Phone Numbers Found on "+url+page+":")
      response = request("GET",url+page,verify=False)
      print(re.findall(regphone,response.text)) #print results
   
   for page in pages: #perform the regex routine for email addresses for all good pages
      print ('\n')  
      print("Email Addresses Found on "+url+page+":")
      response = request("GET",url+page,verify=False)
      print(re.findall(regemail,response.text)) #print results
   print('\n')

"""---------------------BEGIN-RUNNING-CODE-BELOW-THIS-LINE---------------------------------"""
   
url = 'https://www.secdaemons.org/'  #the base URL to be tested
goodpages = [] # empty list of known good pages
print("\n\nDominic's Web Scrubber running on "+url)

f = open('WebPath.txt','r') #open the file
line = f.readline()  # read the first line

while line: #loop until there are no more lines
   line = line.split('\n')[0] #split off the new line character
   attempt = trypage(url,line) #try the page by calling the trypage function
   if attempt == True: #if true append the line to the list of good pages
      goodpages.append(line)
   line = f.readline() #get next line
f.close() #close the file

print("\nSuccessful pages:") #print all good pages to the user
for page in goodpages:
   print(url+page)

getAndScrub(url,goodpages) #call getAndScrube to find phone numbers and email addresses



