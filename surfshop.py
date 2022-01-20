import datetime

class TooManyBoardsError(Exception):
    pass

class CheckoutDateError(Exception):
    pass

class ShoppingCart:
    def __init__(self):
        self.num_surfboards = 0
        self.checkout_date = None
        self.locals_discount = False

    def add_surfboards(self, quantity=1):
        if self.num_surfboards + quantity > 4:
            raise TooManyBoardsError('Cart cannot have more than 4 surfboards in it!')
        else:
            self.num_surfboards += quantity
            suffix = '' if quantity == 1 else 's'
            return f'Successfully added {quantity} surfboard{suffix} to cart!'

    def set_checkout_date(self, date):
      if date <= datetime.datetime.today():
          raise CheckoutDateError
      else:
          self.checkout_date = date

    def apply_locals_discount(self):
        return True