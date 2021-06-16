import os, sys

DEBUG = True

# DO NOT USE only base names while appending,
#   that would result in an unexpected import
#   depending on, from which module this module is called
#sys.path.append("src")

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"src"))

# Method 2 (check the main())
sys.path.insert(0, '../alpha')
import alpha
sys.path.remove('../alpha')

# It's not necessary to have the src inserted and used at the beginning here unless this package would be reused in another bigger project, thus it's preferrable to be set here
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "src/data_provider"))
###
#  unfortunately the following absolute import picks up the alpha module
#  as long as alpha module gets imported.
#  By not importing alpha the correct data_provider is imported, which doesn't make sense
#  as we removed alpha path after importing alpha!!
###
# absolute import using the sys path
import data_provider as dp
# relative import using the sys path
#import src.data_provider as dp

if DEBUG:
	print("Printing from beta.py")
	print(sys.path)
	print(dp.__file__)
	print("----------------------")

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
	#sys.path.remove('../alpha')

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

