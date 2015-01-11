#!/usr/bin/env python2

import subprocess
import argparse

def try_password(keychain, pwd):
    try:
        subprocess.check_output(['/usr/bin/security', 'unlock-keychain', '-p', pwd, keychain])
        return True
    except subprocess.CalledProcessError:
        return False

def main(args):
    pass 

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Bruteforce Keychain master passwords.')
    parser.add_argument('-w', '--wordlist', help='Take wordlist from this file')
    parser.add_argument('keychain', nargs='?', default='login.keychain',
        help='the chain to unlock [login.keychain]')
    main(parser.parse_args())
