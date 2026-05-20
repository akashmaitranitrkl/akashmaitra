import os
import glob

files = glob.glob('*.html')

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Navbar replacements
    content = content.replace('<a href="gallery.html" class="nav-link">Gallery</a>', '<a href="fieldwork.html" class="nav-link">Fieldwork</a>')
    content = content.replace('<a href="gallery.html" class="nav-link active">Gallery</a>', '<a href="fieldwork.html" class="nav-link active">Fieldwork</a>')
    
    # Hero text replacement (only in index.html, but replace will just skip if not found)
    content = content.replace('<h4>Ph.D. Researcher in Paleobiology • IISER Kolkata</h4>', '<h4>PhD Research Scholar in Paleobiology</h4>\n                <h4 style="margin-top: 0; font-weight: 500; color: var(--text-secondary);">IISER Kolkata</h4>')
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updates completed successfully.")
