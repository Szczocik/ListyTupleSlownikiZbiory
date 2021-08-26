import sys

ALLOWED_COMMANDS = ('saldo', 'zakup', 'sprzedaz', 'stop') # dozwolone komendy

saldo = 1000.0 # poczatkowe saldo
store = {
    'chleb': {'count': 2, 'price': 10.0},
    'mleko': {'count': 12, 'price': 4.0}
} # MAGAZYN
mode = sys.argv[1]
logs = [] # historia operacji

while True:
    command = input("Wpisz komendę: ")

    if command not in ALLOWED_COMMANDS:
        print("Niedozwolona komenda!")
        continue
    if command == 'stop':
        print("Koniec programu!")
        break