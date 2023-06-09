import markdown


with open('EntryPoints.md', 'r', encoding='utf-8') as file:
    markdown_content = file.read()



html = markdown.markdown(markdown_content)

template = f'''
<!DOCTYPE html>
<html>
<head>
  <title>{'EntryPoints.md'}</title>
</head>
<body>
  {html}
</body>
</html>
'''

with open('outputnew1.html', 'w', encoding='utf-8') as file:
    file.write(template)
