def remove_tags(text):
	track=0
	newtext=""
	newlist=[]
	while track<len(text):
		#print track
		if text[track]=="<":
			track=text.find(">",track+1)+1
			newtext=newtext+" "
		else: 
			newtext=newtext+text[track]
			track=track+1
			
	#return newtext
	return newtext.split()
	
print remove_tags('''<h1>Title</h1><p>This is a <a href="http://www.udacity.com">link</a>.<p>''')

print remove_tags("This is plain text.")
