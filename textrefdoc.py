import re
import sys
import os.path
from biblereftokens import TokenizeLine
from bgwrequests import BGWRequests

def GetReferences(filename, default_version='NIV'):
    file = open(filename, 'r')
    for line in file:
        print(line.rstrip(), end='')
        # pass lines to logic
        tokens = TokenizeLine(line)
        for book, verses, version in tokens:

            # Rick Warren's The Purpose Driven Life uses alternate names for
            # versions that Bible Gateway uses, so replace them with
            # the Bible Gateway names
            if version == 'GWT':
                version = 'GW'
            elif version == 'TEV':
                version = 'GNT'
            elif version == 'LB':
                version = 'TLB'

            reference = book + ' ' + re.sub(r'\s*', '', verses)
            if version and version != default_version:
                req = BGWRequests(reference, version)
                if req:
                    print(req)
                    print('--------------------', end='')
            req = BGWRequests(reference, default_version)
            if req:
                print(req)
        print('\n=========================')

def main():
    if len(sys.argv) > 3:
        print('Usage: textrefdoc.py filename [version]')
        exit()
    if not os.path.isfile(sys.argv[1]):
        exit()
    if len(sys.argv) == 3:
        GetReferences(sys.argv[1], sys.argv[2])
    elif len(sys.argv) == 2:
        GetReferences(sys.argv[1])

if __name__ == '__main__':
    main()