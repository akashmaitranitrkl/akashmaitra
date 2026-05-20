import os
import glob

html_files = glob.glob('*.html')

navbar_addition = '<a href="outreach.html" class="nav-link">Outreach</a>'
theme_toggle_btn = '<button class="theme-toggle" id="theme-toggle" aria-label="Toggle dark mode" style="background: none; border: none; cursor: pointer; font-size: 1.1rem; margin-left: 1rem;">🌙</button>'
script_tag = '<script src="theme.js"></script>\n</body>'

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Add Outreach tab before CV
    if 'outreach.html' not in content:
        content = content.replace('<a href="cv.html" class="nav-link">CV</a>', f'{navbar_addition}\n                <a href="cv.html" class="nav-link">CV</a>')
        content = content.replace('<a href="cv.html" class="nav-link active">CV</a>', f'{navbar_addition}\n                <a href="cv.html" class="nav-link active">CV</a>')
    
    # 2. Add Theme Toggle button to navbar
    if 'theme-toggle' not in content:
        content = content.replace('</div>\n        </div>\n    </nav>', f'    {theme_toggle_btn}\n            </div>\n        </div>\n    </nav>')
        
    # 3. Add script tag
    if 'theme.js' not in content:
        content = content.replace('</body>', script_tag)
        
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Batch HTML updates completed.")
