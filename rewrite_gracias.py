import sys

with open('index.html', 'r', encoding='utf-8') as f:
    idx_content = f.read()

# Extract Tailwind config from index.html
start_tw = idx_content.find('<script src="https://cdn.tailwindcss.com"></script>')
end_tw = idx_content.find('</script>', start_tw + 50) + 9
tailwind_script = idx_content[start_tw:end_tw]

new_gracias = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <!-- Google Tag Manager -->
    <script>(function(w,d,s,l,i){{w[l]=w[l]||[];w[l].push({{'gtm.start':
    new Date().getTime(),event:'gtm.js'}});var f=d.getElementsByTagName(s)[0],
    j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
    'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
    }})(window,document,'script','dataLayer','GTM-M3RSPCSP');</script>
    <!-- End Google Tag Manager -->
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gracias - Hábitat Senior Living</title>
    
    <link rel="icon" href="habitat_favicon.png" type="image/png">
    
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&family=Playfair+Display:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500;1,600;1,700&display=swap" rel="stylesheet">
    
    {tailwind_script}
</head>
<body class="font-sans text-gray-800 bg-karu-claro antialiased flex flex-col min-h-screen">
    <!-- Google Tag Manager (noscript) -->
    <noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-M3RSPCSP"
    height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
    <!-- End Google Tag Manager (noscript) -->

    <!-- Header -->
    <header class="bg-karu-verde py-4 shadow-md w-full relative z-20">
        <div class="max-w-6xl mx-auto px-6 flex justify-center">
            <a href="index.html">
                <img src="habitat_logo.png" alt="Hábitat Senior Living" class="h-12 md:h-16 object-contain">
            </a>
        </div>
    </header>

    <!-- Main Content -->
    <main class="flex-grow flex flex-col items-center justify-center py-16 px-6 relative z-10">
        <div class="max-w-5xl w-full bg-white shadow-2xl overflow-hidden rounded-2xl flex flex-col md:flex-row relative z-10 border border-karu-marfil">
            
            <!-- Image Left -->
            <div class="w-full md:w-1/2 h-64 md:h-auto min-h-[300px]">
                <img src="habitat_gallery/_MER0311.webp" alt="Hábitat Suramérica" class="w-full h-full object-cover">
            </div>

            <!-- Content Right -->
            <div class="w-full md:w-1/2 p-10 md:p-16 flex flex-col justify-center text-center md:text-left bg-karu-claro">
                <h1 class="text-4xl md:text-5xl font-serif text-karu-verde mb-6">¡Gracias por<br>escribirnos!</h1>
                <p class="text-lg text-gray-700 mb-10 leading-relaxed">
                    Hemos recibido tus datos correctamente. Muy pronto uno de nuestros asesores se pondrá en contacto contigo para brindarte toda la información que necesitas.
                </p>
                <div class="text-center md:text-left">
                    <a href="index.html" class="inline-block bg-[#D4A843] text-[#2C3E2D] font-bold px-8 py-3 rounded uppercase tracking-widest text-sm hover:bg-[#c29633] transition duration-300 shadow-md">
                        VOLVER AL INICIO
                    </a>
                </div>
            </div>
            
        </div>
    </main>

    <!-- Footer -->
    <footer class="bg-karu-verde text-karu-marfil py-4 px-6 md:px-12 w-full mt-auto relative z-20">
        <div class="w-full flex items-center justify-center min-h-[40px]">
            <div class="text-xs md:text-sm text-gray-200 opacity-90 text-center">
                &copy; 2026 Hábitat Suramérica. Todos los derechos reservados. | <a href="politica.html" class="underline hover:text-white transition">Política de tratamiento de datos</a>
            </div>
        </div>
    </footer>
</body>
</html>
"""

with open('gracias.html', 'w', encoding='utf-8') as f:
    f.write(new_gracias)

print('gracias.html updated')
