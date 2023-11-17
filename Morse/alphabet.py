# Alpha-morse dictionary
alphabet = {
    'A' :   '.-',
    'B' :   '-...',
    'C' :   '-.-.',
    'D' :   '-..',
    'E' :   '.',
    'F' :   '..-.',
    'G' :   '--.',
    'H' :   '....',
    'I' :   '..',
    'J' :   '.---',
    'K' :   '-.-',
    'L' :   '.-..',
    'M' :   '--',
    'N' :   '-.',
    'O' :   '---',
    'P' :   '.--.',
    'Q' :   '--.-',
    'R' :   '.-.',
    'S' :   '...',
    'T' :   '-',
    'U' :   '..-',
    'V' :   '...-',
    'W' :   '.--',
    'X' :   '-..-',
    'Y' :   '-.--',
    'Z' :   '--..',
    ' ' :   '/',
    0   :   '-----',
    1   :   '.----',
    2   :   '..---',
    3   :   '...--',
    4   :   '....-',
    5   :   '.....',
    6   :   '-....',
    7   :   '--...',
    8   :   '---..',
    9   :   '----.'
}


# Alpha to morse converter
def encrypt(msg):
    li = []

    for i in msg:
        li.append(alphabet[i.upper()])
    
    return ''.join(li)


# Morse to alpha converter
def decrypt(msg):
    li = []

    for i in msg.split(' '):
        for k, v in alphabet.items():
            if i == v:
                li.append(k)
    
    return ''.join(li).upper()