import re

booksfile = open('books_with_abbrevs.txt', 'r')
versionsfile = open('versions_with_alts.txt', 'r')

books = []
versions = []

for line in booksfile:
    books.append(line)

for line in versionsfile:
    versions.append(line)

booksRE = ''
for line in books:
    line = line.replace(', ', '|').replace('\n', '').replace(' ', '\\ ')
    booksRE = booksRE + line + '|'
booksRE = booksRE[:-1]

versionsRE = ''
for line in versions:
    line = line.replace(', ', '|').replace('\n', '')
    versionsRE = versionsRE + line + '|'
versionsRE = versionsRE[:-1]

verseRE = re.compile(
    r"""
        (
            (?:
            # Handles 17:4, 16:28, 26:20, 25:9, 20:19, 3:2-5, 4:8, 10-12
            # 3:2-5, 4:8, 10-12
            # 24:22-24, 55b-63, 90a
                (?:\d+)
                :
                (?:\d+[a-z]?-\d+[a-z]?|\d+[a-z]?)
                (?:
                    (?:,\s*)
                    (?:
                        (?:\d+[a-z]?-\d+[a-z]?)
                        |
                        (?:\d+[a-z]+)
                        |
                        (?:\d+)
                        :
                        (?:\d+[a-z]?-\d+[a-z]?|\d+[a-z]?)
                    )
                )
            )
            |
            (?: # A range of verses across multiple chapters i.e. 18:2-19:3
                (?:\d+):(?:(?:\d+[a-z]?))
                (?:-)
                (?:\d+):(?:(?:\d+[a-z]?))
            )
            |
            (?: # A range of verses within a chapter i.e. 3:2-5,8,10-12
                (?:\d+)
                :
                (?:
                    (?:\d+[a-z]?-\d+[a-z]?|\d+[a-z]?)
                    (?:
                        (?:,\s*)
                        (?:\d+[a-z]?-\d+[a-z]?|\d+[a-z]?)?
                    )*
                )?
            )
            |
            (?: # A chapter range i.e. 5-6, or chapters 5 and 6
                \d+-\d+|\d+
            )
        )
    """
, re.X)

def TokenizeLine(line):
    tokens = re.findall(re.compile('(' + booksRE + ')\.?\s+' +
                                   verseRE.pattern +
                                   '(?:\s+\((' + versionsRE + ')\))?'
                                   , re.X | re.I), line)

    return tokens

def tests():
    assert TokenizeLine('Genesis 9 Exodus 10-12 Leviticus 3:1  Numbers 1:1a') == [('Genesis', '9', ''), ('Exodus', '10-12', ''), ('Leviticus', '3:1', ''), ('Numbers', '1:1a', '')]
    assert TokenizeLine('Deuteronomy 22:5678 (ncv) Joshua 127:12 Judges 9:11-13 Ruth  7:2b-6, 7b') == [('Deuteronomy', '22:5678', 'ncv'), ('Joshua', '127:12', ''), ('Judges', '9:11-13', ''), ('Ruth', '7:2b-6, 7b', '')]
    assert TokenizeLine('1 Samuel 4:1a-2b 2 Samuel 3:3,5,7 (esv) 1 Kings 4:5,  8-9 2 Kings 24:22-24, 55b-63, 90a') == [('1 Samuel', '4:1a-2b', ''), ('2 Samuel', '3:3,5,7', 'esv'), ('1 Kings', '4:5,  8-9', ''), ('2 Kings', '24:22-24, 55b-63', '')]
    assert TokenizeLine('1 chronicles 3:3-4:1 (NIV)') == [('1 chronicles', '3:3-4:1', 'NIV')]
    assert TokenizeLine('10. Matthew 25:40 (NRSV).') == [('Matthew', '25:40', 'NRSV')]
    assert TokenizeLine('Matt. 3:2-5, 4:8, 10-12') == [('Matt', '3:2-5, 4:8', '')]
    assert TokenizeLine('Proverbs. 17:4, 16:28, 26:20, 25:9, 20:19.') == [('Proverbs', '17:4, 16:28', '')]
    assert TokenizeLine('Proverbs. 18:2-19:3') == [('Proverbs', '18:2-19:3', '')]
    # TODO: Cover this test case: print(TokenizeLine('Titus 2:15-3:2, 10-11'))
# tests()