text = '<meta name="viewport" content="width=device-width,initial-scale=1">\n'

with open('index.html', 'r') as f:
    text1 = text + f.read()

with open('index.html', 'w') as f:
    f.write(text1)

with open('wil.html', 'r') as f:
	text2 = text + f.read()

with open('wil.html', 'w') as f:
	f.write(text2)
