import os, sys

# IT DOES NOT MATTER WHETHER append or insert is used here, all what makes difference is how this module is being inserted for reuse
sys.path.append("src")

# sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))
import src.data_provider as dp

def main():
	tests = dp.get_tests()

	print("Available tests are:")

	for t in tests:
		print("- " + t.name)

if __name__ == '__main__':
	main()

