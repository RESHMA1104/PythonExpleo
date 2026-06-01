from typing import Protocol
class PayMethod(Protocol):
    def authorize_payment(self, amount : float)-> bool:
        ...
    def process_payment(self, amount : float)-> bool:
        ...
class CreditCardPayment:
    def authorize_payment(self,amount:float)->bool:
        print(f"Authorizing Credit amount:{amount}")
        return True
    def process_payment(self,amount:float)->bool:
        print(f"Processing Credit Card payment:{amount}")
        return True
class PayPalPayment:
    def authorize_payment(self, amount:float)-> bool:
        print(f"Authorizing PayPal payment of ${amount}")
        return True
    def process_payment(self, amount:float)-> bool:
        print(f"Processing PayPal payment of ${amount}")
        return True
def process_order(payment : PayMethod, amount:float):
    if payment.authorize_payment(amount):
        payment.process_Payment(amount)
        print("Payment Successful")
    else:
        print("Payment Authorization failed")
creditCardPayment = CreditCardPayment()
payPalPayment = PayPalPayment()
process_order(creditCardPayment, 100.0)
process_order(payPalPayment, 200.0)