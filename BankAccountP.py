class BankAccountP:
    def __init__(self, first_name, last_name, number, balance):
        self._first_name = first_name
        self._last_name = last_name
        self._number = number
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        self._balance -= amount

    def get_balance(self):          # NEW - read balance value
        return self._balance

    def print_info(self):
        first = self._first_name; last = self._last_name
        number = self._number; bal = self._balance
        s = f"{first} {last}, {number}, balance: {bal}"
        print(s)

    #method transfer
    def transfer(self, amount, account):
        """
        - Laget mhp. å gi andre penger / betale til en annen konto
        - Ønsker man å kreve penger legges det inn et negativt beløp
        """
        self._balance -= amount
        account._balance += amount


def test_BankAccountP():
    J=BankAccountP("John","Berg",43252032,2000)
    A=BankAccountP("Anders","Bø",35421876,100)
    amount = 100
    J_exp_bal = J._balance - amount     #forventet balanse
    A_exp_bal = A._balance + amount
    J.transfer(amount,A)
    J_cls_bal = J._balance              #balanse gitt fra klassen
    A_cls_bal = A._balance
    diffJ = abs(J_cls_bal - J_exp_bal)
    diffA = abs(A_cls_bal - A_exp_bal)
    successJ = diffJ < 1E-14
    successA = diffA < 1E-14
    msg=f"bug in method transfer in class BankAccountP"
    assert successJ, msg
    assert successA, msg

test_BankAccountP()

