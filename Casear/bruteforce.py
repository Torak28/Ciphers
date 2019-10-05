import sys, getopt


def main():
    try:
        msg= None

        opts, args = getopt.getopt(sys.argv[1:], "hm:", ['help', 'msg='])
        if len(args) > 0 or len(opts) != 1:
            print('Argument error')
            sys.exit(2)
        for o, a in opts:
            if o in ('-h', '--help'):
                print('bruteforce.py\n\t-m to pass message')
            elif o in ('-m', '--msg'):
                msg = a
        if msg is not None:
            casear(msg)
        else:
            print(f'Argument error\n\tmsg: {msg}')
    except getopt.GetoptError as err:
        print(err)
        sys.exit(2)

def casear(msg):
    SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijkllmnopqrstuvwxyz1234567890 !?.,'

    for key in range(len(SYMBOLS)):
        translated = ''
        for symbol in msg:
            if symbol in SYMBOLS:
                symbolIndex = SYMBOLS.find(symbol)
                translatedIndex = symbolIndex - key

                if translatedIndex < 0:
                    translatedIndex = translatedIndex + len(SYMBOLS)

                translated = translated + SYMBOLS[translatedIndex]
            else:
                translated = translated + symbol

        print(f'Key #{key}: {translated}')

if __name__ == '__main__':
    main()
