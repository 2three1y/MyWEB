import sys
import os

if len(sys.argv) < 3:
    print("Usage: python3 inject_banner.py <SHA> <MSG>")
    sys.exit(1)

sha = sys.argv[1]
msg = sys.argv[2]

banner_html = f'''
<div id="update-banner" class="update-banner" data-sha="{sha}" hidden>
    <div class="update-content">
        <span class="update-tag">New Update</span>
        <span class="update-text"><strong>{sha}</strong>: {msg}</span>
        <button id="close-update-btn" class="update-close-btn" aria-label="Dismiss update banner">×</button>
    </div>
</div>
'''

if not os.path.exists('index.html'):
    print("index.html not found")
    sys.exit(1)

with open('index.html', 'r') as f:
    content = f.read()

placeholder = '<!-- UPDATE_BANNER_PLACEHOLDER -->'
if placeholder in content:
    new_content = content.replace(placeholder, banner_html)
    with open('index.html', 'w') as f:
        f.write(new_content)
    print(f"Injected banner for commit {sha}")
else:
    print("Placeholder not found in index.html")
    sys.exit(1)
