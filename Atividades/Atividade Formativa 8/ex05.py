dragonball_transformacoes = {
    'Goku': ['Super Saiyajin', 'Super Saiyajin Deus'],
    'Vegeta': ['Super Saiyajin'],
    'Gohan': ['Super Saiyajin', 'Ultimate Gohan'],
    'Piccolo': ['Namekian Fusion', 'Super Namekian'],
    'Freeza': ['Final Form', 'Golden Freeza'],
    'Cell': ['Imperfect Form', 'Perfect Form'],
    'Bills': ['God of Destruction'],
    'Whis': ['Angel']
}

transformacoes_unicas = set()
for transformacao in dragonball_transformacoes.values():
    transformacoes_unicas.update(transformacao)

print(transformacoes_unicas)