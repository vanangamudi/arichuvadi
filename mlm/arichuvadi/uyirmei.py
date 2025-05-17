from pprint import pprint, pformat

from .valam import UYIRMEI_MAP_PATH

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
