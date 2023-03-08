from encodings import utf_8
from genericpath import isdir
from glob import glob

import os
import shutil

if os.path.isdir("novel\script"):
    shutil.rmtree("novel\script", ignore_errors=False, onerror=None)

os.mkdir("novel\script")

letters = {'Α': 'A',
    'Β': 'B',
    'Γ': 'C',
    'Δ': 'D',
    'Ε': 'E',
    'Ζ': 'F',
    'Η': 'G',
    'Θ': 'H',
    'Ι': 'I',
    'Κ': 'J',
    'Λ': 'K',
    'Μ': 'L',
    'Ν': 'M',
    'Ξ': 'N',
    'Ο': 'O',
    'Π': 'P',
    'Ρ': 'Q',
    'Σ': 'R',
    'Τ': 'S',
    'Υ': 'T',
    'Φ': 'U',
    'Χ': 'V',
    'Ψ': 'W',
    'Ω': 'X',
    'α': 'a',
    'β': 'b',
    'γ': 'c',
    'δ': 'd',
    'ε': 'e',
    'ζ': 'f',
    'η': 'g',
    'θ': 'h',
    'ι': 'i',
    'κ': 'j',
    'λ': 'k',
    'μ': 'l',
    'ν': 'm',
    'ξ': 'n',
    'ο': 'o',
    'π': 'p',
    'ρ': 'q',
    'σ': 'r',
    'τ': 's',
    'υ': 't',
    'φ': 'u',
    'χ': 'v',
    'ψ': 'w',
    'ω': 'x',
    'ά': 'Y',
    'έ': 'Z',
    'ή': '^',
    'ί': '_',
    'ϊ': '`',
    'ΐ': '{',
    'ό': 'y',
    'ύ': 'z',
    'ώ': '?',
    'ς': '&',

    'Ά': 'A',
    'Έ': 'E',
    'Ή': 'G',
    'Ί': 'I',
    'Ό': 'O',
    'Ύ': 'T',
    'Ώ': 'X',

    '“': '"',
    '”': '"',
    '’': "'"
    
}


def greek_convert():
    for gr_file in glob('novel/grscript/**/*.scr', recursive=True):
        out = open(gr_file.replace("grscript", "script"), 'w', encoding="UTF-8")
        file = open(gr_file, 'r', encoding="UTF-8")
        lines = file.readlines()
        for line in lines:
            #print(line)
            line = line.lstrip()
            if len(line) == 0:
                continue
            com = line.split(' ')
            if com[0] == "γ" or com[0] == "γράμματα" or com[0] == "γράμ" or com[0] == "γραμ":
                line = line.replace(com[0], "text", 1)
            elif com[0] == "επέλεξε":
                line = line.replace(com[0], "choice", 1)

            for key in letters.keys():
                line = line.replace(key, letters[key])
            out.write(line)
            #print(line)

    return line
    pass

grres = open("res/grres.res", 'w')

grres.write("TILESET greek_font font_greek.png BEST NONE\n")
grres.close()
greek_convert()