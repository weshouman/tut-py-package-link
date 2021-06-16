
from models.Product	import Product

import utils

def get_products():
	products = []

	products.append(Product(0, utils.decorate("PC")))
	products.append(Product(1, utils.decorate("HDD")))

	return products

def get_tests():
	products = []

	products.append(Product(0, utils.decorate("PC")))
	products.append(Product(1, utils.decorate("HDD")))

	return products

