from deep_translator import GoogleTranslator

# Dicionário que mapeia o idioma solicitado para seu código ISO
idiomas = {
    "Alemao": "de",
    "Ingles": "en",
    "Japones": "ja",
    "Italiano": "it",
    "Portugues":"pt"
}

# Entrada do idioma com tratamento de espaços e case-insensitive
idioma_escolhido = input('Informe para qual língua deseja traduzir: ').strip().title()

# Verifica se o idioma está no dicionário
while(True):
    if idioma_escolhido in idiomas:
        texto_traduzir = input('O que deseja traduzir? ')
        codigo_idioma = idiomas[idioma_escolhido]  # Obtém o código do idioma
    # Realiza a tradução
    traducao = GoogleTranslator(source='auto', target=codigo_idioma).translate(texto_traduzir)
    print("A tradução ficou:", traducao)
