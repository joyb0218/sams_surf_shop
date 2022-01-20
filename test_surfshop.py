import surfshop, unittest
import datetime

today = datetime.datetime.today()
yesterday = today.replace(day=today.day - 1)

class test_surfshop(unittest.TestCase):
  def setUp(self):
    self.cart = surfshop.ShoppingCart()
    self.discount = surfshop.ShoppingCart()

  def test_add1_surfboard(self):
    message = self.cart.add_surfboards(1)
    self.assertEqual(message, 'Successfully added 1 surfboard to cart!')

  def test_add_more_surfboards(self):
    num_surfboards = [2, 3, 4]
    for board in num_surfboards:
      self.cart = surfshop.ShoppingCart()
      with self.subTest(board):
        self.assertEqual(self.cart.add_surfboards(board), f'Successfully added {board} surfboards to cart!')

  def test_too_many_surfboards(self):
    self.assertRaises(surfshop.TooManyBoardsError, self.cart.add_surfboards, 5)

  def test_locals_discount(self):
    discount = self.discount.apply_locals_discount()
    self.assertTrue(discount)

  def test_checkout_date(self):
    self.assertRaises(surfshop.CheckoutDateError, self.cart.set_checkout_date, yesterday)

unittest.main()