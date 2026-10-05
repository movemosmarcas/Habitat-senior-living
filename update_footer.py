import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

footer_regex = r'<footer class="bg-karu-verde text-karu-marfil py-4 px-6 md:px-12 fixed bottom-0 left-0 w-full z-50.*?</footer>'

new_footer = '''    <!-- Floating CTA Button -->
    <div class="fixed bottom-6 right-6 z-[60] flex flex-col gap-4">
        <a href="#" onclick="openModal(event)" class="inline-flex items-center justify-center gap-2 bg-[#D4A843] text-[#2C3E2D] font-bold px-6 py-4 rounded-full text-sm uppercase tracking-widest hover:bg-[#c29633] transition duration-300 shadow-2xl border border-[#b88f34] hover:-translate-y-1 transform">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" fill="currentColor" viewBox="0 0 16 16">
                <path d="M3.5 0a.5.5 0 0 1 .5.5V1h8V.5a.5.5 0 0 1 1 0V1h1a2 2 0 0 1 2 2v11a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V3a2 2 0 0 1 2-2h1V.5a.5.5 0 0 1 .5-.5zM1 4v10a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1V4H1z"/>
            </svg>
            SOLICITA INFORMACIÓN
        </a>
    </div>

    <!-- Normal Footer -->
    <footer class="bg-karu-verde text-karu-marfil py-8 px-6 md:px-12 w-full relative z-20">
        <div class="w-full flex items-center justify-center">
            <div class="text-sm text-gray-200 opacity-90 text-center">
                &copy; 2026 Hábitat Suramérica. Todos los derechos reservados. | <a href="politica-de-privacidad.html" class="underline hover:text-white transition">Política de tratamiento de datos</a>
            </div>
        </div>
    </footer>'''

content = re.sub(footer_regex, new_footer, content, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Footer replaced successfully')
