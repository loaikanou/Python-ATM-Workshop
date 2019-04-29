# ATM Class
class ATM:
    def __init__(self, balance, bank_name):
        self.balance = balance
        self.bank_name = bank_name
        self.withdrawals_list = []

    def withdraw(self, request):
        print('Welcome at ' + self.bank_name + ' ATM')
        print("Your ATM balance is: " + str(self.balance) + "$")
        result = self.balance
        cash_categories = [100, 50, 10, 5, 1]
        currency_unit = { 100:0, 50:0, 10:0 , 5:0, 1:0 }
        def monyCount(key):
            if key == 'print':
                print(currency_unit)
            else:
                value = currency_unit.get(key)
                currency_unit.update({key: value + 1})

        if request > self.balance:
            print("Can't give you all this money !!")
        elif request < 0:
            print("More than zero plz!")
        else:
            result = self.balance - request
            self.withdrawals_list.append(request)
            for note in cash_categories:
                while request >= note:
                    request -= note
                    monyCount(note)
                    print("give ", str(note))
        
        print("Your balance: " + str(result))
        monyCount('print')
        return result
    
    def show_withdrawals(self):
        for withdrawal in self.withdrawals_list:
            print(withdrawal)
