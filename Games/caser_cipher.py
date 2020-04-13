#! python3
# Caser Cipher
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
MAX_SIZE = len(SYMBOLS)

def getMode():
    while True:
        mode = input('Do you want to Encrypt or Decrypt').lower()
        if mode in ['encrypt','e','decrypt', 'd']:
            return mode
        else:
            print("please enter either Encrypt or Decrypt ")
def getKey():
    key = 0
    while True:
        key = int(input('Please enter the key'))
        if (key>=1 and key<=MAX_SIZE):
            return key
        else:
            print(f'Please enter a proper key which is between 1 - {MAX_SIZE}')
def getMessage():
     return input('Enter your message')

def getTranslatedMessage(mode, msg, key):
    if mode[0] == 'd':
        key = -key
    translated = ''
    for symbol in message:
        symbolIndex = SYMBOLS.find(symbol)
        if symbolIndex == -1:
            translated += symbol
        else:
            symbolIndex += key

            if symbolIndex >= len(SYMBOLS):
                symbolIndex -= len(SYMBOLS)
            elif symbolIndex <= 0:
                symbolIndex += len(SYMBOLS)

            translated += SYMBOLS[symbolIndex]
    return translated



mode = getMode()
message = getMessage()
key = getKey()
print("Your translated text is:")
print(getTranslatedMessage(mode, message, key))

