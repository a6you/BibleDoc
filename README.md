# BibleDoc

## textrefdoc.py
Takes in a file and optionally, a version to be used where the user does not provide a version for a reference. Currently uses NIV as the default version if no version is supplied. The program creates a file in the format outlined in the Output File Structure Example. References are first added in their requested version if applicable, and then the default version, which is currently NIV (i.e. Genesis 3:2 (ESV) will first be requested using ESV, and then NIV). The default version is currently unchangeable from the user's point of view. The requested reference and default reference, if applicable, are separated by a line of dashes, and each line of references is separated with a line of equals signs.

Uses:
- python3 textrefdoc.py filename [version]

Output File Structure Example:

Reference 1 (ESV); Reference 2; Reference 3 (NCV); ...

(Contents of Reference 1 in ESV)

\--------------------

(Contents of Reference 1 in NIV)

(Contents of Reference 2)

(Contents of Reference 3 in NCV)

\--------------------

(Contents of Reference 3 in NIV)

\====================

Reference 4; Reference 5 ...

(Contents of Reference 4)

(Contents of Reference 5)

## bibledoc.py
*WIP*
Accepts a file and a desired Google document title (either on the command line or via user input) and creates a Google document.
Each line of the file is added sequentially to the document as the header of a section, and all the Bible verse references in the line are placed directly below it in the same section.

Uses:
- python3 bibledoc.py [filename] [document_title]

## bgwrequests.py
BGWRequests(reference, version)
* Makes requests to www.biblegateway.com with the reference and version requested.

## biblereftokens.py
TokenizeLine(line)
* Takes in a string and returns an array of tokens that format each Bible verse reference in the string.

## verse_requests.py
get_requests(filename)
* Reads a file according to the Output File Structure Example above and formats Google Docs API requests based on the contents read.
* If a line of references is reached, make a request that the text of the line be added as a header
* If a line of reference contents or a line of dashes is reached, request to add those as simple document text
* If a line of equals signs is reached, request to add a page break

## books_with_abbrevs.txt
A text file with accepted names for books of the Bible.

## versions_with_alts.txt
A text file with accepted version names.
