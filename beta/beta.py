import os, sys

sys.path.append("src")

# Method 2 in place
sys.path.insert(0, '../alpha')
import alpha

# It's not necessary to have the src inserted and used at the beginning here unless this package would be reused in another bigger project, thus it's preferrable to be set here
#sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src/data_provider"))
import data_provider as dp

def print_products():
	products = dp.get_products()

	print("Available products are:")

	for p in products:
		print("- " + p.name)

def main():
	print_products()

	print("")
	print("-----------------------")
	print("")

	# Method 1
	# appending DOES NOT work, and it only shows the products instead of software
	# Normally the path is appended at the file beginning
	#sys.path.append('../alpha')
	#import alpha

	# Method 2
	# The only working way
	# Normally the path is inserted at the file beginning
	#sys.path.insert(0, '../alpha')
	#import alpha

	alpha.main()

	# Method 3
	# exec DOES NOT work, and it only shows the products instead of software
	# filename = '../alpha/alpha.py'
	# exec(open(filename).read())

	print("")
	print("-----------------------")
	print("")

	# Even though we've already inserted alpha at the first position, we still the correct data_provider and products being printed here and before
	print_products()

if __name__ == '__main__':
	main()

