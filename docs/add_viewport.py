text = '<meta name="viewport" content="width=device-width,initial-scale=1">\n'

with open('index.html', 'r') as f:
    text = text + f.read()

with open('index.html', 'w') as f:
    f.write(text)
