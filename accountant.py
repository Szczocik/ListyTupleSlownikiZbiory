import sys

ALLOWED_COMMANDS = ('saldo', 'zakup', 'sprzedaz', 'stop')  # dozwolone komendy
ALLOWED_MODE = ('saldo', 'sprzedaz', 'zakup', 'konto', 'magazyn', 'przeglad')
mode = ALLOWED_MODE
saldo = 1000.0  # poczatkowe saldo
store = {
    'chleb': {'count': 2, 'price': 10.0},
    'mleko': {'count': 12, 'price': 4.0}
}  # MAGAZYN
mode = sys.argv[1]
logs = []  # historia operacji
history_saldo = []

while True:
    command = input("Wpisz rodzaj operacji (saldo, sprzedaz, zakup, stop): ")

    if command not in ALLOWED_COMMANDS:
        print("Niedozwolona komenda!")
        continue
    if command == 'stop':
        print("Koniec programu!")
        # print(f'LISTA OPERACJI: {logs},')
        # print(f'MAGAZYN: {store},')
        # print(f'WARTOŚC SALDA: {saldo}')  # Dorota
        break

    if command == 'saldo':
        amount = float(input("Kwota wpłaty/wypłaty: "))
        if (amount < 0) and (saldo + amount < 0):
            print("Nie masz środków na koncie!")
            continue
        saldo += amount
        if amount > 0:
            cash_deposit = f'{amount} WPŁATA'
            history_saldo.append(cash_deposit)
        else:
            cash_withdrawal = f'{amount} WYPŁATA'
            history_saldo.append(cash_withdrawal)

        log = f"Zmiana saldo o: {amount}"
        logs.append(log)
    elif command == 'zakup':
        product_name = input(("Nazwa produktu: "))
        product_count = int(input("Ilość sztuk: "))
        product_price = float(input("Cena za sztukę: "))
        product_total_price = product_count * product_price
        if product_total_price > saldo:
            print(f"Cena za towary ({product_total_price}) przekracza wartość salda {saldo}")
            continue
        else:
            saldo -= product_total_price
            if not store.get(product_name):
                store[product_name] = {'count': product_count, 'price': product_price}
            else:
                store_product_count = store[product_name]['count']
                store[product_name] = {
                    'count': store_product_count+product_count,
                    'price': product_price}
        log = f"Dokonano zakupu produktu: {product_name} w ilości {product_count} sztuk, o cenie jednostkowej {product_price}."
        logs.append(log)
    elif command == 'sprzedaz':
        product_name = input(("Nazwa produktu: "))
        product_count = int(input("Ilość sztuk: "))
        product_price = float(input("Cena za sztukę: "))
        if not store.get(product_name):
            print("Produktu nie ma w magazynie!")
            continue
        if store.get(product_name)['count'] < product_count:
            print("Brak wystarczającej ilości towaru!")
            continue
        store[product_name] = {
            'count': store.get(product_name)['count'] - product_count,
            'price': product_price
        }
        saldo += product_count * product_price
        if not store.get(product_name)['count']:
            del store[product_name]
        log = f"Dokonano sprzedaży produktu: {product_name} w ilości {product_count} sztuk, o cenie jednostkowej {product_price}."
        logs.append(log)


if mode == 'saldo':
    print(history_saldo)
elif mode == 'konto':
    print(f'SALDO: {saldo}')
elif mode == 'magazyn':
    print(f'MAGAZYN: {store}')
elif mode == 'przeglad':
    print(logs)

print(logs)