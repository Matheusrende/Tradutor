from deep_translator import GoogleTranslator

Texto= input('Informe para qual lingua deseja traduzir: ').title()

match Texto:
    case "Alemao":
        Texto_traduzir= input('O que deseja traduzir? ')
        translated = GoogleTranslator(source='auto', target='de').translate(Texto_traduzir)
        print("A tradução ficou:",translated)
    case "Ingles":
        Texto_traduzir= input('O que deseja traduzir? ')
        translated = GoogleTranslator(source='auto', target='en').translate(Texto_traduzir)
        print("A tradução ficou:",translated)
    case "Japones":
        Texto_traduzir= input('O que deseja traduzir? ')
        translated = GoogleTranslator(source='auto', target='ja').translate(Texto_traduzir)
        print("A tradução ficou:",translated)
    case "italiano":
        Texto_traduzir= input('O que deseja traduzir? ')
        translated = GoogleTranslator(source='auto', target='it').translate(Texto_traduzir)
        print("A tradução ficou:",translated)
    
    
    

       