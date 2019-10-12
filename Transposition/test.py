import random
import sys
import trans
import decryptTrans

def main():
    random.seed(42)

    for i in range(20):
        msg = 'ABCDEFGHIJKLMNOPQRSTUWXYZ' * random.randint(4, 40)

        msg = list(msg)
        random.shuffle(msg)
        msg = ''.join(msg)

        print(f'Test #{str(i)}: {str(msg[:20])} |')

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
