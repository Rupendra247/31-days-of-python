"""
Day 21: Abstraction
Concept: Abstraction allows us to define a 'template' for classes. 
We use the 'abc' (Abstract Base Class) module to ensure that any 
subclass (like PayPal or CreditCard) MUST implement specific methods.
"""
from abc import ABC, abstractmethod

# The Parent class is now an Abstract Base Class
class PaymentGateway(ABC):
    
    @abstractmethod
    def process_payment(self, amount):
        """
        Any class inheriting from PaymentGateway MUST define 
        this method. If they don't, Python will raise an error.
        This forces consistency across different payment types.
        """
        pass

class PayPal(PaymentGateway):
    def process_payment(self, amount):
        # Implementation for PayPal specifically
        print(f"Processing ${amount} via PayPal secure API.")

if __name__ == "__main__":
    # pp = PaymentGateway() # This would fail! You cannot create an object from an ABC.
    pp = PayPal()
    pp.process_payment(100)