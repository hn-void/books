import glob


text = '<meta name="viewport" content="width=device-width,initial-scale=1">\n'
html_list = glob.glob('*.html')

for html_file in html_list:
	content = ''
	with open(html_file, 'r') as f:
		content = text + f.read()
	with open(html_file, 'w') as f:
		f.write(content)
