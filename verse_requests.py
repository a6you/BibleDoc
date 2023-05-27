HORIZONTAL_LINE = "-------------------------------------------------------------------------------------------------------------------------------\n"
'''
Google Docs Python API currently does not have a way to add a horizontal line
with JSON, so a line of dashes will have to do for now
'''

def CreateHeaderStyleRequest(index, length):
    req = {
        "updateParagraphStyle": {
            "range": {
                "startIndex": index,
                "endIndex": index + length - 1
            },
            "paragraphStyle": {
                "namedStyleType": "HEADING_3"
            },
            "fields": "namedStyleType"
        }
    }

    return req

def CreateTextRequest(index, text):
    req = {
        "insertText": {
          "text": text,
          "location": {
              "index": index
          }
        }
    }

    return req

def CreateHorizontalLineRequest(index):
    return CreateTextRequest(index, HORIZONTAL_LINE)

def CreatePageBreakRequest(index):
    req = {
        "insertPageBreak": {
            "location": {
                "index": index
            }
        }
    }

    return req

def GetRequests(filename):
    file = open(filename, 'r')

    index = 1 # Represents index in the Google Document
    requests = [] # An array of Google Docs API requests
    pageStart = True

    # get_requests considers a page to be all the text 
    # in a file until '=========================\n'
    # The first line of a page should be formatted with HEADING_3
    # The rest should not be formatted
    # Once a '====================\n' is reached, add a page break
    # If a '--------------------\n' is reached, add a horizontal line
    for line in file:
        if line == '--------------------\n':
            requests.append(CreateHorizontalLineRequest(index))

            index += 128
        elif line == '=========================\n':
            requests.append(CreatePageBreakRequest(index))
            pageStart = True

            index += 2
        else:
            if pageStart:
                requests.append(CreateTextRequest(index, line))
                requests.append(CreateHeaderStyleRequest(index, len(line)))
                pageStart = False
            else:
                requests.append(CreateTextRequest(index, line))

            index += len(line)


    file.close()

    return requests