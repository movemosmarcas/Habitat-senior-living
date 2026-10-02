import sys

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update text "Hola, quisiera más información sobre Hábitat Suramérica" -> "... Hábitat Senior Living"
# This applies to the <textarea> and the WhatsApp link
content = content.replace('Hola, quisiera más información sobre Hábitat Suramérica', 'Hola, quisiera más información sobre Hábitat Senior Living')
content = content.replace('Hola,%20quisiera%20m%C3%A1s%20informaci%C3%B3n%20sobre%20H%C3%A1bitat%20Suram%C3%A9rica', 'Hola,%20quisiera%20m%C3%A1s%20informaci%C3%B3n%20sobre%20H%C3%A1bitat%20Senior%20Living')

# 2. Fix the title "Nuestros servicios de cuidado especializado" position
old_overlay = '''            <!-- Overlay and Title -->
            <div class="absolute inset-0 bg-black/40 flex justify-center items-center pb-24 md:pb-32">
                <h2 class="text-3xl md:text-4xl font-serif text-white text-center drop-shadow-md px-4">
                    Nuestros servicios de cuidado especializado
                </h2>
            </div>
        </div>

        <!-- Cards overlapping the background -->
        <div class="w-full px-6 pb-20">
            <div class="max-w-7xl mx-auto -mt-24 md:-mt-32 relative z-20 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">'''

new_overlay = '''            <!-- Overlay and Title -->
            <div class="absolute inset-0 bg-black/40"></div>
        </div>

        <!-- Cards overlapping the background -->
        <div class="w-full px-6 pb-20">
            <div class="max-w-7xl mx-auto -mt-40 md:-mt-48 relative z-20">
                <h2 class="text-3xl md:text-4xl font-serif text-white text-center drop-shadow-lg px-4 mb-8">
                    Nuestros servicios de cuidado especializado
                </h2>
                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">'''

if old_overlay in content:
    content = content.replace(old_overlay, new_overlay)
    
    # We added a wrapping div, so we need to add a closing </div> for it
    # We need to find the end of the cards section. The cards section ends just before:
    # <!-- 5. Ubicación Estratégica -->
    # So we can replace that comment with a closing </div> and the comment.
    
    end_cards = '''        </div>
    </section>

    <!-- 5. Ubicación Estratégica -->'''
    
    new_end_cards = '''            </div>
        </div>
    </section>

    <!-- 5. Ubicación Estratégica -->'''
    
    content = content.replace(end_cards, new_end_cards)
    print('Title layout updated')
else:
    print('Old overlay block not found, skipped layout update')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('File updated successfully')
