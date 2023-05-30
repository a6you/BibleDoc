# BibleDoc
A tool to help make Bible reading, Christian book studies, and the like easier.
Write out all the Bible verse references you want to use in one file, and get them all in either a text file or a Google Doc so you can share it with others.
Text File Tool: textrefdoc.py
Google Docs Tool: bibledoc.py

# Installation
1. Install python for your machine.

At this point, you can use the Text File tool. If you wish to use the Google Docs tool, do the following:

2. Install the following modules with ./module_install.sh (enabling execute permissions for it as necessary)
3. Set up a Google Cloud Console for this Google API app.
4. Download the credentials.json for the app and place it in the project directory.

Now you should be able to use both tools.
## textrefdoc.py
Takes as input a text file that has lines which may or may not contain Bible verse references, and optionally, a version. See the Input File Structure Example or sample_input.txt for examples on how the file may be formatted.

Produces as output text in the format shown in the Output File Structure Example. See sample_output.txt for the full version of the sample output. Text produced may be redirected to a file for later use.

References are first added in their requested version if applicable, and then the default version, which is currently NIV (i.e. Genesis 3:2 (ESV) will first be requested using ESV, and then NIV). The default version is currently unchangeable from the user's point of view. The requested reference and default reference, if applicable, are separated by a line of dashes, and each line of references is separated with a line of equals signs.
 
Uses:
- python3 textrefdoc.py filename [version]

Input File Structure Example:

<img src="https://github.com/a6you/BibleDoc/assets/53089551/fdbf75f9-d332-47fb-9633-b4fbee8cfdc8">

Output Text Structure Example (cropped):

<img src="https://github.com/a6you/BibleDoc/assets/53089551/d0a83e28-4f6c-463b-8f4c-124497efecb7">


## bibledoc.py
*WIP*
Accepts a file and a desired Google document title (either on the command line or via user input) and creates a Google document.
Each line of the file is added sequentially to the document as the header of a section, and all the Bible verse references in the line are placed directly below it in the same section.

Uses:
- python3 bibledoc.py [filename] [document_title]

## bgwrequests.py
BGWRequests(reference, version)
* Makes requests to www.biblegateway.com with the reference and version requested.
* Returns a string with each of the verses in the reference on separate lines.

## biblereftokens.py
TokenizeLine(line)
* Takes in a string and returns an array of tokens that format each Bible verse reference in the string.

## verse_requests.py
GetRequests(filename)
* Reads a file according to the Output File Structure Example above and formats Google Docs API requests based on the contents read.
* If a line of references is reached, make a request that the text of the line be added as a header
* If a line of reference contents or a line of dashes is reached, request to add those as simple document text
* If a line of equals signs is reached, request to add a page break

## books_with_abbrevs.txt
A text file with accepted names for books of the Bible.

## versions_with_alts.txt
A text file with accepted version names.
