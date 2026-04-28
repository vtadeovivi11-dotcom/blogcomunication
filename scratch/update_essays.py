import os

files_data = [
    ('essay1.html', 'EnsayoDaiana.pdf', 'Ensayo_Daiana.pdf'),
    ('essay2.html', 'EnsayoHannia.pdf', 'Ensayo_Hannia.pdf'),
    ('essay3.html', 'EnsayoVictorTadeo.pdf', 'Ensayo_VictorTadeo.pdf'),
    ('essay4.html', '#', 'Ensayo_Lizeth.pdf')
]

for filename, pdf_file, download_name in files_data:
    filepath = os.path.join('c:/Users/OMAR/Downloads/blogcomunicacion', filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    download_html = f'''
                <div class="mt-12 p-6 bg-white/5 border border-white/10 rounded-2xl flex flex-col sm:flex-row items-center justify-between gap-4">
                    <div>
                        <h3 class="text-xl font-bold text-white mb-1">Documento Original</h3>
                        <p class="text-gray-400 text-sm">Visualiza o descarga el ensayo en formato PDF.</p>
                    </div>
                    <a href="documentos_com/{pdf_file}" download="{download_name}" target="_blank" class="px-6 py-3 rounded-xl bg-accent hover:bg-accentHover text-white font-semibold transition-all shadow-[0_0_15px_rgba(139,92,246,0.3)] flex items-center gap-2">
                        <svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" /></svg>
                        Ver PDF
                    </a>
                </div>
            </div>
        </article>
'''
    
    if '<h3 class="text-xl font-bold text-white mb-1">Documento Original</h3>' not in content:
        # replace the closing tags of the prose block
        content = content.replace('            </div>\n        </article>', download_html)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

print('Added download links to essays.')
