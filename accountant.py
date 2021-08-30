import sys

ALLOWED_MODE = ('saldo', 'sprzedaz', 'zakup', 'konto', 'magazyn', 'przeglad')  # dozwolone komendy wejścia
ALLOWED_COMMANDS = ('saldo', 'zakup', 'sprzedaz', 'stop')  # dozwolone komendy w programie
mode = ALLOWED_MODE
saldo = 1000.0  # poczatkowe saldo
store = {
    'chleb': {'count': 2, 'price': 10.0},
    'mleko': {'count': 12, 'price': 4.0}
}  # MAGAZYN
mode = sys.argv[1]
logs = []  # historia operacji
# saldo_history = []  # historia operacji salda
# sales_history = []  # historia sprzedaży
# purchase_history = []  # historia zakupu


while True:
    command = input("Wpisz rodzaj operacji (saldo, sprzedaz, zakup, stop): ")

    if command not in ALLOWED_COMMANDS:
        print("Niedozwolona komenda!")
        continue
    if command == 'stop':
        print("Koniec programu!")
        break

    if command == 'saldo':
        amount = float(input("Kwota wpłaty/wypłaty: "))
        if (amount < 0) and (saldo + amount < 0):
            print("Nie masz środków na koncie!")
            continue
        saldo += amount
        # if amount > 0:
        #     cash_deposit = f'{amount} WPŁATA'
        #     saldo_history.append(cash_deposit)
        # elif amount < 0:
        #     cash_withdrawal = f'{amount} WYPŁATA'
        #     saldo_history.append(cash_withdrawal)

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
        # purchase = f"Zakupiono: {product_name}, w cenie {product_price} zł, w ilości {product_count} szt."
        # purchase_history.append(purchase)
        log = f"Dokonano zakupu produktu: {product_name} w ilości {product_count} sztuk, w cenie jednostkowej {product_price} zł."
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
        # sales = f"Sprzedano: {product_name}, w cenie {product_price} zł, w ilości {product_count} szt."
        # sales_history.append(sales)
        log = f"Dokonano sprzedaży produktu: {product_name} w ilości {product_count} sztuk, o cenie jednostkowej {product_price}."
        logs.append(log)

if mode == 'sprzedaz':
    print(f'Historia sprzedaży:{sales_history}.')
elif mode == 'zakup':
    product_name = input(("Nazwa produktu: "))
    product_price = float(input("Cena za sztukę: "))
    product_count = int(input("Ilość sztuk: "))
    product_total_price = product_count * product_price
    if product_total_price > saldo:
        print(f"Cena za towary ({product_total_price}) przekracza wartość salda {saldo}")
    else:
        saldo -= product_total_price
        if not store.get(product_name):
            store[product_name] = {'count': product_count, 'price': product_price}
        else:
            store_product_count = store[product_name]['count']
            store[product_name] = {
                'count': store_product_count + product_count,
                'price': product_price}
    print(f'Nazwa produktu:{product_name}, cena: {product_price}, ilość: {product_count}.')
elif mode == 'saldo':
    amount = float(input("Kwota wpłaty/wypłaty: "))
    comment = input('Komentarz: ')
    if (amount < 0) and (saldo + amount < 0):
        print("Nie masz środków na koncie!")
    saldo += amount
    print(f'Kwota:{amount} {comment}.')
elif mode == 'konto':
    print(f'SALDO: {saldo}')
elif mode == 'magazyn':
    print(f'MAGAZYN: {store}')
elif mode == 'przeglad':
    print(f'Historia operacji: {logs}.')

