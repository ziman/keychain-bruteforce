# keychain-bruteforce

Bruteforce master passwords of the MAC OS X password manager.

Usage:
```bash
$ ./bruteforce -w words.txt
```

You can generate various typos using
```bash
$ ./mkwordlist > words.txt
```

For `mkwordlist`, you need `substs.py`:
```python
SUBSTS = {'s': 'ad', 'h': 'jg', ...}
PWD = 'my secret password without typos'
```
