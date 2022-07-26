
from .valam import (
    VER_ADAIVU,
    THARAVU_ADAIVU,
    ADAIYALAMITTA_ARI_PATH,
    ARI_PATH,
    ARI_UNI_PATH
)

def yes_or_no(prompt):
     return True if input('{}:[y/N]? '.format(prompt)).lower() == 'y' else False

print(f"""
This script is used to extract tamil alphabet and unicode level representation
from {ADAIYALAMITTA_ARI_PATH} which is at this point the canonical source of truth.
The files produced by this script are {ARI_PATH} and {ARI_UNI_PATH}. {ARI_PATH} is not sorted
according to the native tamil script order. The {ARI_PATH} in repo is manually edited
to has to be kept safe :)
""")

if yes_or_no('are you sure you wanna run this'):
    if yes_or_no('are you really really sure you wanna run this'):
        if not yes_or_no('think real hard about this dude!!!'):
            exit(0)
    else:
        exit(0)
else:
    exit(0)

    
print(f'reading {ADAIYALAMITTA_ARI_PATH}... ', end='')

with open(ADAIYALAMITTA_ARI_PATH) as f:
    letters = []
    for vari in f:
        vari = vari.strip()
        if not vari or vari.startswith('#'):
            continue

        _, vari =  vari.split(':=')
        vari = [i for i in vari.split('\t') if i and i != '_']
        letters.extend(vari)

print('DONE')
count = Counter()
count.update(letters)
pprint(count)

letters = sorted(list(set(letters)))

OFILEPATH=ARI_PATH
print(f'writing to {OFILEPATH}...')
with open(OFILEPATH, 'w') as  of:
    of.write('\n'.join(letters))
    of.write('\n')
    
print(f'reading {ARI_PATH}... ', end='')
with open(ARI_PATH) as f:
    letters = [i.strip() for i in f.readlines()]

print('DONE')
    
letters = [i for i in letters if i.strip()]
letters = ''.join(letters)
letters = sorted(list(set(letters)))

OFILEPATH=ARI_UNI_PATH
print(f'writing to {OFILEPATH}...')
with open(OFILEPATH, 'w') as  of:
    of.write('\n'.join(letters))
    of.write('\n')
