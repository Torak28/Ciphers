import random
import sys
import trans
import decryptTrans
import argparse

def main():
    seed, length, how_many = None, None, None
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--seed', help='Just a random seed number', default=42, type=int)
    parser.add_argument('-l', '--length', help='Length of random msg to check', default=40, type=int)
    parser.add_argument('-hm', '--how_many', help='How many test should be run', default=20, type=int)

    args = parser.parse_args()

    seed = args.seed
    length = args.length
    how_many = args.how_many

    if seed == None or length == None or how_many == None:
        print('Argument error. See --help')
        sys.exit(2)

    test(seed, length, how_many)


def test(s, l, h_m):
    random.seed(s)

    for i in range(h_m):
        msg = 'ABCDEFGHIJKLMNOPQRSTUWXYZ' * random.randint(4, l)

        msg = list(msg)
        random.shuffle(msg)
        msg = ''.join(msg)

        print(f'Test #{str(i + 1)}: {str(msg[:50])}...')

        for key in range(1, int(len(msg)/2)):
            enc = trans.trans(msg, key)
            dec = decryptTrans.trans(enc, key)

            if msg != dec:
                print(f'Missmatch with key: {key} and message: {msg}')
                print(f'Decrypted as: {dec}')
                sys.exit()

    print(f'All Test Passed!')

if __name__ == '__main__':
    main()
