import os, sys

# it is not necessary here
# sys.path.insert(0, os.path.join(os.path.dirname(__file__), "models"))
from models.Test	import Test

def get_tests():
	tests = []

	tests.append(Test(0, "Main"))
	tests.append(Test(1, "Secondary"))

	return tests

