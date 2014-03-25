alaf=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
ALAF=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

def rot13(text):
  ntext=""
  for each in text:
    if each in alaf:
      lc=alaf[(((alaf.index(each))+13)%26)]
      ntext=ntext+lc
    elif each in ALAF:
      lz=ALAF[(((ALAF.index(each))+13)%26)]
      ntext=ntext+lz
    elif each not in alaf:
      ntext=ntext+each
    elif each not in ALAF:
      ntext=ntext+each
  return ntext
  
print(rot13("abaabAA1232 ,!"))
