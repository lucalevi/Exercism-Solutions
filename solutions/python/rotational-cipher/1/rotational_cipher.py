import string

def rotate(text, key):

    alphabet = list(string.ascii_letters[:26])
    
    cypher = alphabet[key:] + alphabet[:key]

    translated_letters = []

    for char in text:
        if char == " ":
            translated_letters.append(" ")
        elif char.isalpha():
            letter_index = alphabet.index(char.lower())
            translated_letter = cypher[letter_index]
            
            if char.isupper():
                translated_letter = translated_letter.upper()
                
            translated_letters.append(translated_letter)
        else:
            translated_letters.append(char)
            

    return "".join(translated_letters)