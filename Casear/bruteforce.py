import sys, argparse


def main():
    msg= None
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--msg', help='Pass message to encrypt, decrypt', default='Ala ma kota', type=str)
    args = parser.parse_args()

    msg = args.msg
    if msg == None:
        print('Argument error. See --help')
        sys.exit(2)

    casear(msg)

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
