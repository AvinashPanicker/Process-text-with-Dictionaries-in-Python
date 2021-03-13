#! /usr/bin/env python3
import os
import requests

list_of_files = os.listdir('/data/feedback')
#the text files are placed in data/feedback


#Traverse over each file and, from the contents of these text files, create a dictionary by keeping title, name, date, and feedback as keys for the content value, respectively.
for file in list_of_files:
        fp = open('/data/feedback/'+file)
        data = fp.read()
        data = data.split('\n')
        dic = {"title":data[0], "name":data[1], "date":data[2], "feedback":data[3]}
        
        #requests module utilised to post the dictionary to the company's website
        response = requests.post('http://http://34.122.209.226//feedback/', json=dic)
        print(response.status_code)
