
#coding:Utf-8
import markdown
import sys

import os



output = [ """<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <link href="demo.css" type="text/css" rel="stylesheet" />
    <title>%(title)s</title>
  </head>

<body>
""" % { 'title' : "TEST" }]
#---------------------------------------#fichier ent suivie en entreprise#---------------------------------------

lolo = os.listdir(sys.argv[1])

for i in lolo:
	liste = i
	extension = os.path.splitext(liste)
	if ".md" in extension[1]:		
		with open(i, "r", encoding="utf-8") as input_file:
			text = input_file.read()
		html = markdown.markdown(text)
		output.append( html )
		output.append( """</body></html>""" )
		with open("toto.html", "w", encoding="utf-8", errors="xmlcharrefreplace") as output_file:
			toto = output_file.write(''.join(output))				
	else :
		pass



