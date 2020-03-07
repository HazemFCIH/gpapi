

    
#from moviepy.editor import * 
#import pyrebase
def listToString(s):  
    
    # initialize an empty string 
    str1 = ""  
    
    # traverse in the string   
    for ele in s:  
        str1 += ele   
    
    # return string   
    return str1 


import re 
import spacy
import os
os.system("python -m spacy download en")
nlp = spacy.load("en") 
def extract(sentence):
  doc = nlp(sentence)
  list_words = sentence.split() #to catch next word(part1)
  results = []

  for ent in doc.ents:    #for loop to catch ORG
    target =""
    if(ent.label_ == "ORG"):
      if (list_words.index(ent.text) != len(list_words)-1 ): #to catch next word(part2)
        next_word = list_words[list_words.index(ent.text) + 1]
        target = ent.text +' '+ next_word
        results.append(target)
  for word in doc:          #for loop to catch urls
    if(word.like_url):
      results.append(word)

  return results

sentence="New York product with collaboration with samsung a71 on Lenovo ideapad".lower()

regex= re.compile('[أ-ي]')
w=regex.sub('',sentence)
res=" ".join(w.split())



from flask import Flask, request
app = Flask(__name__)
import logging
handler = logging.StreamHandler()
handler.setLevel(logging.ERROR)
app.logger.addHandler(handler)
@app.route("/data", methods=['GET', 'POST'])
def helloJson():
    import json
    data =str(request.values)
    with open('data.json','w') as f:
        json.dump(data,f)
    
    
    
    return "hello", 200  
@app.route("/gproduct", methods=['GET', 'POST'])
def helloProduct():

    w=extract(res)
    z=str(w[0])
    return z, 200
@app.route("/")
def helloFirst():
    return "This is python test number 70!"
if __name__ == "__main__":
    app.run()

