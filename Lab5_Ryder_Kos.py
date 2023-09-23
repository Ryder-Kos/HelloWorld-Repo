def main():
    encodedWord = "WBLARF8TTS"
	
    print(DecodeWord(encodedWord))
    encodedWord = "L8KAOUL"
    print(DecodeWord(encodedWord))
    encodedWord = "E8N8N8"
    print(DecodeWord(encodedWord))
    encodedWord = "8TRA8DY T8LA"
    print(DecodeWord(encodedWord))
    encodedWord = "8TT LHA TILLTA LIMAS"
    print(DecodeWord(encodedWord))
    encodedWord = "LHA GRAAN FIATD GTA8MS IN LHA W8RM SUNEABMS"
    print(DecodeWord(encodedWord))
    encodedWord = "TONG T8E T8CKS L8SLY L8CO LIMA 8L TA8SL T8LATY"
    print(DecodeWord(encodedWord))

def DecodeWord(encodedWord):
    decode_dict = {
        'T': 'L',
        'L': 'T',
        'A': '8',
        'A': 'E',
        '8': 'A',
        'B': 'A',
        'E': 'B',
    }

    decoded_word = ''

    for char in encodedWord:
        decoded_word += decode_dict.get(char, char)

    return decoded_word

if __name__ == "__main__":
    main()
