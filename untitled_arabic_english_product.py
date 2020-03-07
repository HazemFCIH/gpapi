import re 
import spacy
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
w=extract(res)

api_key = "AIzaSyDBQzzqJz-JF-P-oohpFSlUI7PRHC3_DMs"
from googleapiclient.discovery import build
resource = build("customsearch" , 'v1' ,developerKey=api_key).cse()
type(resource)
#result = resource.list(q='lenovo' , cx='003285143206147685189:sawhrpxepbq' , searchType='image').execute()
#z= ' '.join(w)
for i in w:
    result = resource.list(q=i , cx='003285143206147685189:sawhrpxepbq' ).execute()
    len(result['items'])
    for item in result['items'] :
     # if z in item['title'] :
              print(item['title'] , item['link'])
    item['title']+ item['link']


