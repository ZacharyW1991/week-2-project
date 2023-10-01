def shop_cart():
    #dictionary with 'item':'price'*'amount'
    cart = {}
    while True:
        option = input('Enter an item to add to your cart,\n\'list\' to see your items and total do far, \n\'delete\' to remove an item from your list, \nor \'done\' to see your final total: ' )
        #print final receipt
        if option == 'done':
            for goods, total_amount in cart.items():
                print(f'Your total is: ${total_amount}')
            return cart
        #see list of items
        elif option == 'list':
            for goods, total_amount in cart.items():
                print(f'{goods}: ${total_amount}')
        #remove item from list
        elif option == 'delete':
            remove_keys=[]
            for goods, total_amount in cart.items():
                print(f'{goods}: ${total_amount}')
            remove_this = input('Type the name of the item you want to remove: ')
            for goods, total_amount in cart.items():
                if goods == remove_this:
                    remove_keys.append(remove_this)
            for remove in remove_keys:
                del cart[remove]
        #add item to list, then multiply that by the amount of items
        else:
            price = float(input('Enter a dollar amount: '))
            amount = int(input('How many? '))
            final_price=round(price*amount, 2)
            for goods, total_amount in cart.items():
                if option == goods:
                    amount += int(input('How many of this item do you want to add or remove? \nType a positive number to add, a negative one to remove, or a numeral zero to keep it the same: '))
                    if amount <= 0:
                        del cart[goods]
                else:
                    final_price=price*amount
            cart[option]=final_price

shop_cart()