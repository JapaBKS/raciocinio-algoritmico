cardapio = {
    'Bebidas': {
        'Refrigerantes': [
            {'Nome': 'Coca-Cola', 'Preço': 6},
            {'Nome': 'Pepsi', 'Preço': 6},
            {'Nome': 'Guaraná Jesus', 'Preço': 6},
            {'Nome': 'Fanta Uva', 'Preço': 6}
        ],
        'Alcoólicos': [
            {'Nome': 'Vinho', 'Preço': 60},
            {'Nome': 'Whiskey', 'Preço': 35},
            {'Nome': 'Gin Tônica', 'Preço': 35},
            {'Nome': 'Drinks', 'Preço': 30}
        ],
        'Sucos': [
            {'Nome': 'Abacaxi', 'Preço': 15},
            {'Nome': 'Maracujá', 'Preço': 15},
            {'Nome': 'Limão', 'Preço': 15},
            {'Nome': 'Laranja', 'Preço': 15},
            {'Nome': 'Manga', 'Preço': 15}
        ],
        'Quentes': [
            {'Nome': 'Expresso', 'Preço': 5},
            {'Nome': 'Capuccino', 'Preço': 10},
            {'Nome': 'Mocaccino', 'Preço': 12},
            {'Nome': 'Café com Leite', 'Preço': 7},
            {'Nome': 'Achocolatado', 'Preço': 10},
            {'Nome': 'Chá', 'Preço': 7}
        ]
    },
    'Entradas': {
        'Vegetarianas': [
            {'Nome': 'Salada', 'Preço': 30},
            {'Nome': 'Batatas Fritas', 'Preço': 30},
            {'Nome': 'Polenta', 'Preço': 25}
        ],
        'Com Derivados De Animais': [
            {'Nome': 'Carpaccio', 'Preço': 50},
            {'Nome': 'Creme de Aipim com Bacon', 'Preço': 35},
            {'Nome': 'Iscas de Peixe', 'Preço': 40},
            {'Nome': 'Carne de Onça', 'Preço': 35}
        ]
    },
    'Pratos Principais': {
        'Vegetarianas': [
            {'Nome': 'Macarrão Alho e Óleo', 'Preço': 45},
            {'Nome': 'Ratatouille', 'Preço': 60},
            {'Nome': 'Macarrão ao Molho 4 Queijos', 'Preço': 45},
            {'Nome': 'Lasanha com Carne de Soja', 'Preço': 50}
        ],
        'Com Derivados De Animais': [
            {'Nome': 'Carré de Cordeiro', 'Preço': 85},
            {'Nome': 'Bife à Parmegiana', 'Preço': 65},
            {'Nome': 'Estrogonofe', 'Preço': 45},
            {'Nome': 'Costelinha Barbecue', 'Preço': 70}
        ]
    },
    'Sobremesas': {
        'Com Lactose': [
            {'Nome': 'Petit Gâteau', 'Preço': 28},
            {'Nome': 'Pudim', 'Preço': 22},
            {'Nome': 'Banana Split', 'Preço': 25},
            {'Nome': 'Torta de Limão', 'Preço': 15}
        ],
        'Sem Lactose': [
            {'Nome': 'Gelatina', 'Preço': 10},
            {'Nome': 'Salada de Frutas', 'Preço': 25},
            {'Nome': 'Crumble de Maçã', 'Preço': 35},
            {'Nome': 'Brigadeiro Vegano', 'Preço': 15}
        ]
    }
}

def adicionar_item_cardapio():
    categoria = input("Digite a categoria (Bebidas/Entradas/Pratos Principais/Sobremesas): ").capitalize()
    
    if categoria == 'Bebidas':
        subcategoria = input("Digite a subcategoria (Refrigerantes/Alcoólicos/Sucos/Quentes): ").capitalize()
        nome = input("Digite o nome da bebida: ")
        preco = float(input("Digite o preço da bebida: "))
        
        if subcategoria in cardapio[categoria]:
            cardapio[categoria][subcategoria].append({'Nome': nome, 'Preço': preco})
        else:
            cardapio[categoria][subcategoria] = [{'Nome': nome, 'Preço': preco}]

    elif categoria == 'Entradas':
        subcategoria = input("Digite a subcategoria (Vegetarianas/Com Derivados De Animais): ").capitalize()
        nome = input("Digite o nome da entrada: ")
        preco = float(input("Digite o preço da entrada: "))
        
        if subcategoria in cardapio[categoria]:
            cardapio[categoria][subcategoria].append({'Nome': nome, 'Preço': preco})
        else:
            cardapio[categoria][subcategoria] = [{'Nome': nome, 'Preço': preco}]

    elif categoria == 'Pratos Principais':
        subcategoria = input("Digite a subcategoria (Vegetarianas/Com Derivados De Animais): ").capitalize()
        nome = input("Digite o nome do prato principal: ")
        preco = float(input("Digite o preço do prato principal: "))
        
        if subcategoria in cardapio[categoria]:
            cardapio[categoria][subcategoria].append({'Nome': nome, 'Preço': preco})
        else:
            cardapio[categoria][subcategoria] = [{'Nome': nome, 'Preço': preco}]

    elif categoria == 'Sobremesas':
        subcategoria = input("Digite a subcategoria (Com Lactose/Sem Lactose): ").capitalize()
        nome = input("Digite o nome da sobremesa: ")
        preco = float(input("Digite o preço da sobremesa: "))
        
        if subcategoria in cardapio[categoria]:
            cardapio[categoria][subcategoria].append({'Nome': nome, 'Preço': preco})
        else:
            cardapio[categoria][subcategoria] = [{'Nome': nome, 'Preço': preco}]

    else:
        print("Categoria inválida. Tente novamente.")

# Chamando a função para adicionar item ao cardápio
adicionar_item_cardapio()



def salvar_cardapio_em_arquivo(cardapio, nome_arquivo):
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        for categoria, subcategorias in cardapio.items():
            arquivo.write(f"Categoria: {categoria}\n")
            for subcategoria, itens in subcategorias.items():
                arquivo.write(f"  Subcategoria: {subcategoria}\n")
                for item in itens:
                    arquivo.write(f"    Produto: {item['Nome']}, Preço: R${item['Preço']:.2f}\n")
            arquivo.write("\n")

# Exemplo de uso:
salvar_cardapio_em_arquivo(cardapio, "cardapio.txt")
print("Cardápio salvo em 'cardapio.txt'")