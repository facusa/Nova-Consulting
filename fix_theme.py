import re

with open('styles.css', 'r') as f:
    css = f.read()

# Variables definition
css = css.replace('--bg-dark: #0f172a;', '--bg-light: #f8fafc;')
css = css.replace('--bg-darker: #020617;', '--bg-light-alt: #f1f5f9;')
css = css.replace('--text-main: #f8fafc;', '--text-main: #0f172a;')
css = css.replace('--text-muted: #94a3b8;', '--text-muted: #475569;')
css = css.replace('--glass-bg: rgba(30, 41, 59, 0.7);', '--glass-bg: rgba(255, 255, 255, 0.7);')
css = css.replace('--glass-border: rgba(255, 255, 255, 0.08);', '--glass-border: rgba(0, 0, 0, 0.08);')
css = css.replace('--glass-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3);', '--glass-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.05);')

# Usage replacements
css = css.replace('var(--bg-dark)', 'var(--bg-light)')
css = css.replace('var(--bg-darker)', 'var(--bg-light-alt)')

# Specific color replacements
css = css.replace('rgba(15, 23, 42, 0.9)', 'rgba(255, 255, 255, 0.9)')
css = css.replace('rgba(15, 23, 42, 0.6)', 'rgba(255, 255, 255, 0.6)')

# Gradients
css = css.replace('rgba(15, 23, 42, 0)', 'rgba(255, 255, 255, 0)')
css = css.replace('rgba(30, 41, 59, 0.8), rgba(2, 6, 23, 0.9)', 'rgba(255, 255, 255, 0.8), rgba(241, 245, 249, 0.9)')
css = css.replace('rgba(30, 41, 59, 0.7), rgba(16, 185, 129, 0.05)', 'rgba(255, 255, 255, 0.7), rgba(16, 185, 129, 0.05)')
css = css.replace('background-color: rgba(15, 23, 42);', '')
css = css.replace('background-color: #2A2E3A;', 'background-color: #ffffff;')

# Translucent white to translucent black
css = css.replace('rgba(255, 255, 255, 0.05)', 'rgba(0, 0, 0, 0.05)')
css = css.replace('rgba(255, 255, 255, 0.03)', 'rgba(0, 0, 0, 0.03)')
css = css.replace('rgba(255, 255, 255, 0.02)', 'rgba(0, 0, 0, 0.02)')
css = css.replace('rgba(255, 255, 255, 0.1)', 'rgba(0, 0, 0, 0.1)')

with open('styles.css', 'w') as f:
    f.write(css)

with open('script.js', 'r') as f:
    js = f.read()

js = js.replace('rgba(15, 23, 42, 0.95)', 'rgba(255, 255, 255, 0.95)')
js = js.replace('rgba(255, 255, 255, 0.08)', 'rgba(0, 0, 0, 0.08)')

with open('script.js', 'w') as f:
    f.write(js)
