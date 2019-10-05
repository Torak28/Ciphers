import sys, getopt


def main():
    try:
        msg, key, mode = None, None, None

        opts, args = getopt.getopt(sys.argv[1:], "hedm:k:", ['help', 'encrypt', 'decrypt', 'msg=', 'key='])
        if len(args) > 0 or len(opts) != 3:
            print('Argument error')
            sys.exit(2)
        for o, a in opts:
            if o in ('-h', '--help'):
                print('casear.py\n\t-e to encrypt\n\t-d to decrypt\n\t-m to pass message\n\t-k to pass key')
            elif o in ('-m', '--msg'):
                msg = a
            elif o in ('-k', '--key'):
                key = int(a)
            elif o in ('-e', '--encrypt'):
                mode = 'encrypt'
            elif o in ('-d', '--decrypt'):
                mode = 'decrypt'
        if msg is not None and key is not None and mode is not None:
            casear(msg, key, mode)
        else:
            print(f'Argument error\n\tmsg: {msg},\n\tkey: {key},\n\tmode: {mode}')
    except getopt.GetoptError as err:
        print(err)
        sys.exit(2)

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
