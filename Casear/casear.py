import sys, argparse


def main():
    msg, key, mode = None, None, None
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--msg', help='Pass message to encrypt, decrypt', default='Ala ma kota', type=str)
    parser.add_argument('-k', '--key', help='Pass key to encrypt, decrypt message', default=3, type=int)
    parser.add_argument('-e', '--encrypt', help='Set the mode to encryption', action='store_true', default=False)
    parser.add_argument('-d', '--decrypt', help='Set the mode to decryption',action='store_true', default=False)
    args = parser.parse_args()

    msg = args.msg
    key = args.key
    if args.decrypt == True:
        mode = 'decrypt'
    elif args.encrypt == True:
        mode = 'encrypt'
    else:
        mode = None

    if msg == None or key == None or mode == None:
        print('Argument error. See --help')
        sys.exit(2)

    print(f'\tmsg: {msg}\n\tkey: {key}\n\tmode: {mode}')
    casear(msg, key, mode)

def casear(msg, key, mode):
    SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijkllmnopqrstuvwxyz1234567890 !?.,'
    translated = ''

    for symbol in msg:
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)

            if mode == 'encrypt':
                translatedIndex = symbolIndex + key
            elif mode == 'decrypt':
                translatedIndex = symbolIndex - key

            if translatedIndex >= len(SYMBOLS):
                translatedIndex = translatedIndex - len(SYMBOLS)
            elif translatedIndex < 0:
                translatedIndex = translatedIndex + len(SYMBOLS)

            translated = translated + SYMBOLS[translatedIndex]
        else:
            translated = translated + symbol

    print(translated)

if __name__ == '__main__':
    main()
