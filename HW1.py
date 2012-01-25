print "it worked"

def shout(txt):
  new_txt = txt.upper()
  new_txt = new_txt.replace(". ", "! ")
  if new_txt[len(new_txt) - 1] != ".":
    new_txt = new_txt + "!"
  new_txt = new_txt.replace("?", "!")
  return new_txt
  
def reverse(txt):
  if isinstance(txt, str) == False:
    return ""
      
  return txt[::-1]
  
def reversewords(txt):
  if isinstance(txt, str) == False:
    return ""
  
  new_text = ""
  reversed_sentences = []
    
  tmp = txt.replace("?", ".")
  tmp = tmp.replace("!", ".")
  sentences = tmp.split(". ")
  sentences = [s.strip() for s in sentences if len(s.strip()) > 0]
  
  last_sentence = sentences[len(sentences) - 1]
  if last_sentence[len(last_sentence) - 1] == ".":
    sentences[len(sentences) - 1] = last_sentence[0:len(last_sentence)-1]
  
  for sentence in sentences:
    words = sentence.split()
    words.reverse()
    reversed_sentence = ""
    for word in words:
      reversed_sentence += word
      reversed_sentence += " "
    reversed_sentences.append(reversed_sentence[0:(len(reversed_sentence)-1)])
  
  for sentence in reversed_sentences:
    if len(sentence) > 0:
      new_text += sentence
      new_text += ". "
    
  return new_text
  
def reversewordletters(txt):
  if isinstance(txt, str) == False:
    return ""
  
  tmp_text = ""
  
  back_pointer = 0
  front_pointer = 0
  stop_chars = [" ", ".", "?", "!", ",", ":", ";"]
  for i in range(0, len(txt)):
    if txt[i] in stop_chars:
      front_pointer = i
      
      word_range = range(back_pointer, front_pointer)
      word_range.reverse()
      for j in word_range:
        tmp_text += txt[j]
      tmp_text += txt[i]
      
      back_pointer = i+1
      
  return tmp_text
  
def piglatin(txt):
  if isinstance(txt, str) == False:
    return "Not a string, try again."
  if txt.isalpha() == False:
    return "Letters only, please!"
 
  vowels = "aeiou"
  lowertxt = txt.lower()
  initialvalue = []
  
  foundvowels = []
  
  for vv in vowels:
    if lowertxt.find(vv) > -1:
      foundvowels = foundvowels + [vv]
  
  
  for vv in foundvowels:
    initialvalue = initialvalue + [lowertxt.index(vv)]
    
  firstvowel = min(initialvalue)
  out = txt[firstvowel:] + txt[:firstvowel] + "ay"
  
  if firstvowel == 0:
    out = txt + "way"
  
  if txt[0:2] == "qu":
    out = txt[2:] + "quay"
  
  if txt[0:2] == "Qu":
    out = txt[2:] + "Quay"
  
  return out


  
print "End of script"
print "This is just a minor change to let me know if I'm commiting right"