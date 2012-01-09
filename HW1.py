def shout(txt):
  new_txt = txt.upper()
  new_txt = new_txt.replace(". ", "! ")
  if new_txt[len(new_txt) - 1] != ".":
    new_txt = new_txt + "!"
  new_txt = new_txt.replace("?", "!")
  return new_txt
  
def reverse(txt):
  return txt
  
def reversewords(txt):
  return txt
  
def reversewordletters(txt):
  return txt
  
def piglatin(txt):
  return txt