def shop_cart():
    #dictionary with 'item':'price'*'amount'
    cart = {}
    while True:
        option = input('Enter an item to add to your cart,\n\'list\' to see your items and total do far, \n\'delete\' to remove an item from your list, \nor \'done\' to see your final total: ' )
        #print final receipt
        if option == 'done':
            final_total = 0
            for goods, total_amount in cart.items():
                final_total+=total_amount
                round(final_total, 2)
            print(f'Your total is: ${final_total}')
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
            cart[option]=final_price

shop_cart()