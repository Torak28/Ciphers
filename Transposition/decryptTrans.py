import sys, argparse, math


def main():
    msg, key = None, None
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--msg', help='Pass message to encriypt', default='A  tlmkaaao', type=str)
    parser.add_argument('-k', '--key', help='Pass key to encrypt message', default=3, type=int)
    args = parser.parse_args()

    msg = args.msg
    key = args.key

    if msg == None or key == None:
        print('Argument error. See --help')
        sys.exit(2)

    trans(msg, key)

def trans(msg, key):
    numOfColumns = math.ceil(len(msg)/ key)
    numOfRows = key
    numOfShadedBoxes = (numOfColumns * numOfRows) - len(msg)

    plaintext = [''] * numOfColumns

    column, row = 0, 0

    for symbol in msg:
        plaintext[column] += symbol
        column += 1

        if (column == numOfColumns) or (column == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
            column = 0
            row += 1

    print(f'{"".join(plaintext)}')

if __name__ == '__main__':
    main()
