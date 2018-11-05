import argparse

def read_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', help='this is a option', required=True)
    parser.add_argument('-b', help='this is b option', required=True)
    parser.add_argument('-c', help='this is c option')
    return parser.parse_args()


if __name__ == '__main__':
    args = read_args()
    print '%s is a option' % args.a
    print '%s is b option' % args.b
    if args.c != None:
        print '%s is c option' % args.c
    else:
        print 'c is missing'
