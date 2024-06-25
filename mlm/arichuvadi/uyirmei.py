from pprint import pprint, pformat

from arichuvadi.valam import UYIRMEI_MAP_PATH
from arichuvadi import get_letters_coding

UYIRMEI = 'uyirmei'

IMAP = {}
MAP  = {}

def read_uyirmei_map():
    MAP[UYIRMEI] = {}
    IMAP[UYIRMEI]= {}
    with open(UYIRMEI_MAP_PATH) as f:
        for line in f.readlines()[1:]:
            letter, mei, uyir = line.strip().split('|')

            if len(uyir) > 0 and len(mei) > 0:
                MAP[UYIRMEI][letter] = mei + uyir #not fusing just concat
                IMAP[UYIRMEI][mei+uyir] = letter
            elif len(mei) > 0:
                MAP[UYIRMEI][letter] = mei
                IMAP[UYIRMEI][mei] = letter
            else:
                MAP[UYIRMEI][letter] = letter
                IMAP[UYIRMEI][letter] = letter


read_uyirmei_map()

def split_uyirmei(string, join_p=True):
    """
    தமிழ் -> த் அ ம் இ ழ்
    """

    letters = []
    for i in get_letters_coding(string.strip()):
        if i in MAP[ UYIRMEI ]:
            letters.extend(
                get_letters_coding( MAP[ UYIRMEI ][i] ))
        else:
            letters.append(i)

    if join_p:
        return ''.join(letters)
    return letters

def split_uyirmei2(string, join_p=True):
    """
    தமிழ் -> த ம் இ ழ்
    """
    letters = []
    inletters = get_letters_coding(string.strip())

    letters.append(inletters[0])
    for i in inletters[1:-1]:
        if i in MAP[ UYIRMEI ]:
            letters.extend(
                get_letters_coding( MAP[ UYIRMEI ][i] ))
        else:
            letters.append(i)

    letters.append(inletters[-1])

    if join_p:
        return ''.join(letters)
    return letters


def merge_uyirmei(instring):
    if len(instring) < 2:
        return ''.join(instring)

    string = list(instring[:])
    i = 0
    while i < len(string) - 1:
        couplet = string[i]+string[i+1]
        #print(couplet, string)
        if couplet in IMAP[ UYIRMEI ]:
            # print(''.join(string[:i]), '#',
            #       ''.join([IMAP[ UYIRMEI ][couplet]]), '#',
            #       ''.join(string[i+1:]))
            string = string[:i] + [(IMAP[ UYIRMEI ][couplet])] + string[i+2:]


        i += 1

    return ''.join(string)

if __name__ == '__main__':
    print(split_uyirmei('உயர் தனிச் செம் மொழி'))
    print(merge_uyirmei(list(split_uyirmei('உயர் தனிச் செம் மொழி'))))
