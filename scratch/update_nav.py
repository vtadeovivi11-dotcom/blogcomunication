import os
import glob

files = glob.glob('c:/Users/OMAR/Downloads/blogcomunicacion/*.html')

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Change Artículos to Artículo
    content = content.replace('>Artículos</a>', '>Artículo</a>')
    content = content.replace('>Ver Artículos</a>', '>Ver Artículo</a>')
    
    # Add Recursos tab
    lines = content.split('\n')
    new_lines = []
    for line in lines:
        new_lines.append(line)
        if '<a href="essays.html"' in line:
            new_line = line.replace('essays.html', 'resources.html').replace('>Ensayos<', '>Recursos<')
            if 'text-white' in new_line:
                new_line = new_line.replace('text-white', 'text-gray-300').replace('text-gray-300 block', 'text-gray-300 hover:text-white block')
            new_lines.append(new_line)
            
    content = '\n'.join(new_lines)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print('Nav updated successfully.')
