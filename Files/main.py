from time import sleep
print('Welcome to Iron Bank or Bravoos ATM')

restart = ('y') # set restart to not exit the loop
chances = 3 # attempt limits
balance = 100.15 # set a balance

# functioning loop
while chances > 0:
    pin = int(input('Please Enter Your 4 Digit Pin: '))
    # check for pin
    if pin == 8879:
        print('You entered your pin correctly\n')
        # restart should be yes to use the atm service.
        while restart not in ('n', 'no', 'NO', 'N'):
            '''
             1 -> check user balance
             2 -> do withdrawal
             3 -> deposit money
             4 -> return card and end the process
            '''
            print('Please Press 1 For Your Balance\n')
            print('Please Press 2 To Make a Withdrawal\n')
            print('Please Press 3 To Deposit your Money\n')
            print('Please Press 4 To Return Card\n')
            option = int(input('What would you like to choose? '))

            # display balance amount
            if option == 1:
                print(f'Your Balance is {balance} $')
                restart = input('Would you like to go back? ')
                if restart in ('n', 'no', 'NO', 'N'): # end process
                    chances = 0
                    print('Thank You')
                    break

            # make a withdrawal
            elif option == 2:
                withdrawal = float(input(f'How much would you like to withdraw? \n'
                                         f'10$ \t 20$ \n40$ \t 50$ \n70$ \t90$ \n100$ \t 120$ \n'
                                         )
                                   )
                # condition to enter validate amount
                if withdrawal in list(x for x in range(0, 121, 10)):
                    balance = balance - withdrawal
                    print('Processing amount...')
                    sleep(0.4)
                    print(f'Your balance is now {balance}\n')
                    restart = input('Would you like to go back?: ')
                    if restart in ('n', 'no', 'NO', 'N'):
                        chances = 0
                        print('Thank You')
                        break
                # retry for invalid amount
                elif withdrawal not in list(x for x in range(0, 121, 10)):
                    print('Invalid amount, Please retry\n')
                    restart = ('y')
                elif withdrawal == 1:
                    withdrawal = float(input('Please Enter a Desired amount: '))

            # to deposit money.
            elif option == 3:
                deposit = float(input('How much would you like to deposit?\n'))
                balance = balance + deposit
                print(f'\nYour Balance is now {balance}$')
                restart  = input('Would you like to go back? ')
                if restart in ('n', 'no', 'NO', 'N'): # end process
                    chances = 0
                    print('Thank You')
                    break

            # to return the card and end the process
            elif option == 4:
                print('Please wait whilst you card is returned...\n')
                print('Thank you for you service')
                chances = 0
                break
            else:
                print('Please Enter a correct number.\n') # re-check pin
                restart = ('y')

    # break the process if pin is incorrectly enter for 3 times.
    elif pin!= 8879:
        print('Incorrect Pin!')
        chances = chances - 1
        if chances == 0:
            print('\nNo more tries.')
            break