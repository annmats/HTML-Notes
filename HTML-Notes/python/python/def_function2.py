lang=input(f"Preferred language(en, es, fr):")
name=input("Your name:")
def greet(lang):
    if lang == 'en':
        return "Hello"
    elif lang == 'es':
        return "Hola"
    elif lang == 'fr':
        return "Bonjour"
    else:
        return "Hello"

print (greet(lang), name)
