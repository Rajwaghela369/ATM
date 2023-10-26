#### ATM FUNCTION CLASS

class Function():
    def __init__(self, Iban, Pin):
        self.Iban = Iban
        self.Pin = Pin

    def verify_detials(self):
        flag = False
        if self.Iban == 'BB7890' and self.Pin == 8879:
            flag = True
            return flag
        else:
            print('Incorrect details')

    def check_Balance(self):
        Balance = 50000
        return Balance

    def withdrawal(self):
        amount = int(input('Enter Amount for Withdrawal: '))
        return amount

    def depsoit(self):
        amount = int(input('Enter Deposit amount: '))
        return amount

    def transaction(self):
        past_duration = int(input('Enter the date from where you want transaction: '))
        value = 500
        print(f'{past_duration} value: {value}')