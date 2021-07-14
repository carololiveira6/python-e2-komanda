menu = [
    {'id': 1, 'name': 'ADICIONAL FRANGO 50G', 'price': 4.0},
    {'id': 2, 'name': 'SALADA', 'price': 18.0},
    {'id': 3, 'name': 'ADICIONAL DE LEITE', 'price': 1.0},
    {'id': 4, 'name': 'AMERICANO', 'price': 5.0},
    {'id': 5, 'name': 'CAPUCCINO', 'price': 7.0},
    {'id': 6, 'name': 'CARIOCA', 'price': 5.0},
    {'id': 7, 'name': 'COADO', 'price': 6.0},
    {'id': 8, 'name': 'COADO PEQUENO', 'price': 3.0},
    {'id': 9, 'name': 'DUPLO MACCHIATO', 'price': 9.0},
    {'id': 10, 'name': 'ESPRESSO', 'price': 5.0},
    {'id': 11, 'name': 'ESPRESSO DUPLO', 'price': 8.0},
    {'id': 12, 'name': 'FRENCH PRESS 300ML', 'price': 8.0},
    {'id': 13, 'name': 'FRENCH PRESS 600ML', 'price': 14.0},
    {'id': 14, 'name': 'LATTE', 'price': 7.0},
    {'id': 15, 'name': 'MACCHIATO', 'price': 6.0},
    {'id': 16, 'name': 'MOCCHA', 'price': 9.0},
    {'id': 17, 'name': 'AFFOGATO', 'price': 8.0},
    {'id': 18, 'name': 'COLD BREW', 'price': 8.0},
    {'id': 19, 'name': 'LATTE GELADO', 'price': 7.0},
    {'id': 20, 'name': 'MOCCHA GELADO', 'price': 10.0},
    {'id': 21, 'name': 'STELLA ARTOIS 310ML', 'price': 6.0},
    {'id': 22, 'name': 'CHÁ GELADO', 'price': 7.0},
    {'id': 23, 'name': 'CHÁ QUENTE', 'price': 5.0},
    {'id': 24, 'name': 'MATE BATIDO', 'price': 7.0},
    {'id': 25, 'name': 'CHOCOLATE QUENTE', 'price': 8.0},
    {'id': 26, 'name': 'DESAYUNO', 'price': 18.0},
    {'id': 27, 'name': 'ADICIONAL GRANOLA', 'price': 1.0},
    {'id': 28, 'name': 'BOLO FATIA', 'price': 5.0},
    {'id': 29, 'name': 'BOLO NO POTE', 'price': 8.0},
    {'id': 30, 'name': 'BRIGADEIRO', 'price': 2.0},
    {'id': 31, 'name': 'BROWNIE CHOCOLATE', 'price': 5.0},
    {'id': 32, 'name': 'COOKIE', 'price': 5.0},
    {'id': 33, 'name': 'FOLHADO DOCE', 'price': 5.0},
    {'id': 34, 'name': 'FRENCH TOAST', 'price': 5.0},
]

''' 
------------------------- Exemplo -------------------------
table_1 = [{'id': 1, 'amount': 5}, {'id': 19, 'amount': 5}]
total = calculate_tab(table_1)
print(total)
'''

def calculate_tab(table):

    result = 0
    for table_current in table:
        id_table, amount_table = table_current.values()

        for menu_item in menu:
            id_menu, name, price = menu_item.values()
            
            if id_menu == id_table:
                result += amount_table * price
    
    return result

if __name__ == "__main__":
    table_1 = [{'id': 1, 'amount': 5}, {'id': 19, 'amount': 5}]
    total = calculate_tab(table_1)
    print(total)


'''
Jeitos diferentes de fazer:

def calculate_tab(table):

    result = 0
    for table_current in table:
        id_table, amount_table = table_current.items()

        for menu_item in menu:
            id_menu, name, price = menu_item.items()
            
            if id_menu[1] == id_table[1]:
                result += amount_table[1] * price[1]
    
    return result

--------------------------------------------------

def calculate_tab(table):
    value = 0
    for i in table_1:
            for j in menu:
                if j['id'] == i['id']:
                    value = value + i['amount'] * j['price']
    return value
'''