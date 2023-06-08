import re
import sys
import os.path
from biblereftokens import TokenizeLine
from bgwrequests import BGWRequests

def GetReferences(filename, default_version='NIV'):
    output = ''

    file = open(filename, 'r')
    for line in file:
        output = output + line.rstrip()
        # Pass lines to logic
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
                    output = output + req + '\n'
                    output = output + '--------------------'
            req = BGWRequests(reference, default_version)
            if req:
                output = output + req + '\n'
        output = output + '\n=========================' + '\n'

    return output

def main():
    if len(sys.argv) > 3:
        print('Usage: textrefdoc.py filename [version]')
        return
    if not os.path.isfile(sys.argv[1]):
        print('Please use a valid filename')
        return
    if len(sys.argv) == 3:
        print(GetReferences(sys.argv[1], sys.argv[2]))
    elif len(sys.argv) == 2:
        print(GetReferences(sys.argv[1]))

if __name__ == '__main__':
    main()