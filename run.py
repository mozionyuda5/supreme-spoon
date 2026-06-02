import subprocess

morse = "-... .- ... .... / .-. --- -.-. -.-"

MORSE_REV = {
    '.-':'A','-...':'B','-.-.':'C','-..':'D','.':'E','..-.':'F',
    '--.':'G','....':'H','..':'I','.---':'J','-.-':'K','.-..':'L',
    '--':'M','-.':'N','---':'O','.--.':'P','--.-':'Q','.-.':'R',
    '...':'S','-':'T','..-':'U','...-':'V','.--':'W','-..-':'X',
    '-.--':'Y','--..':'Z',
    '-....-':'-'
}

def decode(m):
    words = m.split(' / ')
    decoded = []

    for w in words:
        letters = w.split()
        decoded.append(
            ''.join(MORSE_REV.get(l, '') for l in letters)
        )

    return ' '.join(decoded).lower()

cmd = decode(morse)

print("[+] Decoded:")
print(cmd)

print("\n[+] Running...\n")

subprocess.run(cmd, shell=True)