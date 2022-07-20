from pprint import pprint, pformat
from collections import OrderedDict, defaultdict, namedtuple

AAYTHAM_NEELAM = 1   # ஃ
UYIR_NEELAM = 12 # அஆஇஈஉஊஎஏஐஒஓஔ
MEI_NEELAM = 18 # க்ங்ச்ஞ்ட்ண் த்ந்ப்ம்ய்ர் ல்வ்ழ்ள்ற்ன்
GRANTHAM_NEELAM = 6  # ஶ்ஜ்ஷ்ஸ்ஹ்க்ஷ்
KURIGAL_NEELAM = 7  # ௳௴௵௶௷௹௺
YENGAL_NEELAM = 13 # ௦௧௨௩௪௫௬௭௮௯௰௱௲

ARICHUVADI_NEELAM = \
    AAYTHAM_NEELAM + UYIR_NEELAM + MEI_NEELAM + GRANTHAM_NEELAM \
    + KURIGAL_NEELAM + YENGAL_NEELAM \
    + (MEI_NEELAM + GRANTHAM_NEELAM) * UYIR_NEELAM

ARICHUVADI_MAP = defaultdict(list)

ARICHUVADI = []


with open('adaiyalamitta-ari.txt') as f:
    for vari in f:
        vari = vari.strip()
        if not vari or vari.startswith('#'):
            continue

        adaiyalam, vari =  vari.split(':=')
        adaiyalam = adaiyalam.strip().split(':')

        vari = [i for i in vari.split('\t') if i]

        for i in vari:
            if i == '_':
                i = ''
                
            if i not in ARICHUVADI_MAP[adaiyalam[0]]:
                ARICHUVADI_MAP[adaiyalam[0]].append(i)

ARICHUVADI_MAP = dict(ARICHUVADI_MAP)
##############################################

with open('ari.txt') as f:
    for vari in f:
        vari = vari.strip()
        if vari:
            ARICHUVADI.append(vari)

#pprint(ARICHUVADI)
#print(len(ARICHUVADI))
assert len(ARICHUVADI) == ARICHUVADI_NEELAM, \
    f'len(ARICHUVADI):{len(ARICHUVADI)} but should be {ARICHUVADI_NEELAM}'


##############################################

UNICODE_MAP = dict()

ippo = None
with open('ari-uni.txt') as f:
    for vari in f:
        vari = vari.strip()
        if vari == '':
            continue
        
        if vari.startswith('*'):
            vari = vari.strip('* ')
            ippo = vari
            UNICODE_MAP[ippo] = []

        else:
            UNICODE_MAP[ippo].append(vari)

            
UNICODE_LIST = []
UNICODE_LIST = \
    UNICODE_MAP['எண்கள்'] \
    + UNICODE_MAP['உயிர்'] \
    + UNICODE_MAP['மெய்:தமிழ்'] \
    + UNICODE_MAP['மெய்:கிரந்தம்'] \
    + UNICODE_MAP['உயிர்க்குறிகள்'] \
    + UNICODE_MAP['குறிகள்']


# I have no idea why I wrote two functions
# for this, the following line makes all the differece
#      munp = mun if GLYPH_OR_CODING == 0 else mun[-1]
# need to test with lot of string to figure why I did this
# I should have documented this
# I thought I might have wrote this for 'க்ஷா' as in பக்ஷாசி
# that letter/glyph is evidently 4 codepoints =  'க', '்', 'ஷ', 'ா' long
# I am pretty sure I did this for letter that is 3 codepoints long
def _get_letters(saram, GLYPH_OR_CODING=1):
    puthusaram = []
    for i in saram:
        if i in UNICODE_MAP['உயிர்க்குறிகள்']:
            mun = puthusaram.pop(-1)
            munp = mun if GLYPH_OR_CODING == 0 else mun[-1]
            if munp in UNICODE_MAP['உயிர்க்குறிகள்']:
                puthusaram.append( mun )
                puthusaram.append( i )
            else:
                puthusaram.append( mun + i )
        else:
            puthusaram.append( i )
            
    return puthusaram

def get_letters_glyph(saram):
    return _get_letters(saram, 0)

def get_letters_coding(saram):
    return _get_letters(saram, 1)


# predicates
def yezhutha_aa(ezhuthu):
    return ezhuthu in ARICHUVADI_MAP['எழுத்து']

def yenna_aa(ezhuthu):
    return ezhuthu in ARICHUVADI_MAP['எண்கள்']


if __name__ == '__main__':
    pprint(ARICHUVADI_MAP)
    saram = 'The Great உயர்தனிச்செம்மொழி தமிழ்!!!'
    print(saram)
    print(list([i for i in saram]))
    print(get_letters_coding(saram))
    print(get_letters_glyph(saram))


