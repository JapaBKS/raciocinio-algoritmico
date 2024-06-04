tecnicas_personagens = {
    'Goku': ['Kamehameha', 'Spirit Bomb', 'Genki Dama'],
    'Vegeta': ['Final Flash', 'Galick Gun'],
    'Gohan': ['Masenko', 'Father-Son Kamehameha'],
    'Piccolo': ['Special Beam Cannon', 'Light Grenade'],
    'Freeza': ['Death Beam', 'Supernova'],
    'Cell': ['Kamehameha', 'Solar Kamehameha'],
    'Bills': ['Hakai'],
    'Whis': ['Temporal Do-Over', 'Warp'],
}

tecnicas = set()
for tecnica in tecnicas_personagens.values():
    tecnicas.update(tecnica)

print(tecnicas)