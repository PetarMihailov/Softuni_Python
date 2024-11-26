def morse_to_text(morse_code):
    # Morse code dictionary
    morse_dict = {
        '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F',
        '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
        '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R',
        '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
        '-.--': 'Y', '--..': 'Z', '-----': '0', '.----': '1', '..---': '2',
        '...--': '3', '....-': '4', '.....': '5', '-....': '6', '--...': '7',
        '---..': '8', '----.': '9'
    }

    words = morse_code.split(' | ')
    decoded_words = []

    for word in words:
        letters = word.split(' ')
        decoded_word = ''.join(morse_dict[letter] for letter in letters if letter in morse_dict)
        decoded_words.append(decoded_word)

    return ' '.join(decoded_words)


morse_code = input()

result = morse_to_text(morse_code)
print(result)
