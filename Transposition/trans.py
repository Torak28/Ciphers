import sys, argparse


def main():
    msg, key = None, None
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--msg', help='Pass message to encriypt', default='Ala ma kota', type=str)
    parser.add_argument('-k', '--key', help='Pass key to encrypt message', default=3, type=int)
    args = parser.parse_args()

    msg = args.msg
    key = args.key

    if msg == None or key == None:
        print('Argument error. See --help')
        sys.exit(2)

    trans(msg, key)

def trans(msg, key):
    ciphertext = [''] * key

    for column in range(key):
        currentIndex = column

        while currentIndex < len(msg):
            ciphertext[column] += msg[currentIndex]

            currentIndex += key

    print(f'{"".join(ciphertext)}')

if __name__ == '__main__':
    main()
