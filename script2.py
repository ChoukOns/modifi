import os
from deep_translator import GoogleTranslator

def translate_text_file(input_file, output_file, target_language):
    try:
        with open(input_file, "r", encoding='utf-8', errors='ignore') as f:
            text = f.read()
    except FileNotFoundError:
        print(f"Le fichier {input_file} n'existe pas.")
        return

    translated_text = GoogleTranslator(source='auto', target=target_language).translate(text)

    try:
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
    except OSError as e:
        print(f"Erreur lors de la création du répertoire : {e}")

    with open(output_file, "w", encoding='utf-8', errors='ignore') as f:
        f.write(translated_text)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 4:
        print("Usage: python translate_text_file.py <input_file> <output_file> <target_language>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    target_language = sys.argv[3]

    translate_text_file(input_file, output_file, target_language)

