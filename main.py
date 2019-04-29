from ATM import ATM

atm1 = ATM(500, "Smart Bank")
atm1.withdraw(700)
atm1.withdraw(300)
atm1.show_withdrawals()

atm2 = ATM(1000, "Baraka Bank")
atm2.withdraw(500)
atm2.withdraw(250)
atm2.show_withdrawals()