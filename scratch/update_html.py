import os
import glob

directory = "../"
html_files = glob.glob(os.path.join(directory, "*.html"))

replacements = {
    "<title>IAnova | El Futuro del Aprendizaje</title>": "<title>IA + educación: el combo del aprendizaje del futuro</title>",
    '<span class="font-bold text-xl tracking-tight">IA<span class="text-accent">nova</span></span>': '<span class="font-bold text-xl tracking-tight">IA<span class="text-accent">+</span>educación</span>',
    '<span class="font-bold text-lg tracking-tight">IA<span class="text-accent">nova</span></span>': '<span class="font-bold text-lg tracking-tight">IA<span class="text-accent">+</span>educación</span>',
    '<p class="text-gray-500 text-sm">© 2026 Proyecto Universitario. Diseño con fines académicos.</p>': '<p class="text-gray-500 text-sm">© 2026 Proyecto Universitario por Victor Tadeo, Hannia, Lizeth y Wendy Daiana.</p>'
}

for file_path in html_files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    modified = False
    for old_text, new_text in replacements.items():
        if old_text in content:
            content = content.replace(old_text, new_text)
            modified = True
            
    if modified:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated {file_path}")
