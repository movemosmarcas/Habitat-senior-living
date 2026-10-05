import re

def update_gtm(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace in <head>
    content = re.sub(r"'GTM-[A-Z0-9]+'", "'GTM-WFSQ859'", content)
    
    # Replace in <body>
    content = re.sub(r"id=GTM-[A-Z0-9]+", "id=GTM-WFSQ859", content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

update_gtm('index.html')
update_gtm('gracias.html')
print('GTM IDs updated in both files')
