import urllib.request
import re

try:
    response = urllib.request.urlopen('https://suramerica.servicios-habitat.com/politica.html')
    html = response.read().decode('utf-8')
except Exception as e:
    print('Failed to fetch:', e)
    exit(1)

match = re.search(r'<div class="policy-container">(.*?)</div>\s*</section>', html, re.DOTALL)
if match:
    policy_content = match.group(1)
else:
    policy_content = '<p>No se encontró el contenido de la política.</p>'

with open('index.html', 'r', encoding='utf-8') as f:
    template = f.read()

header_match = re.search(r'(.*?<nav.*?</nav>)\s*</header>', template, re.DOTALL)
if header_match:
    header = header_match.group(1) + '\n</header>'
else:
    header = ''

footer_match = re.search(r'(<footer.*)', template, re.DOTALL)
if footer_match:
    footer = footer_match.group(1)
else:
    footer = ''

head_match = re.search(r'(<head>.*?</head>)', template, re.DOTALL)
head = head_match.group(1) if head_match else ''

new_page = f'''<!DOCTYPE html>
<html lang="es">
{head}
<body class="font-sans text-gray-800 bg-karu-claro antialiased flex flex-col min-h-screen">
{header}

<main class="flex-grow pt-32 pb-24 px-6">
    <div class="max-w-4xl mx-auto bg-white p-8 md:p-12 shadow-xl">
        <h1 class="text-3xl md:text-4xl font-serif text-karu-verde mb-8 text-center">Política de Protección de Datos</h1>
        <div class="prose max-w-none text-gray-700 leading-relaxed space-y-4">
            {policy_content}
        </div>
    </div>
</main>

{footer}
'''

with open('politica-de-privacidad.html', 'w', encoding='utf-8') as f:
    f.write(new_page)

print('Created politica-de-privacidad.html')
