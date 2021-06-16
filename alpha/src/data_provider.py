import os, sys

# The following insertion is both not necessary and discouraged here
# Even if the same model exists in beta application
# sys.path.insert(0, os.path.join(os.path.dirname(__file__), "models"))
from models.Test	import Test

# A. When importing from a relative directory with "import" directive
#    the definitions won't be globally available, so we have to address
#    like: utils.decorate() and u.decorate()
import utils
#import utils as u

# DEBUG PRINT
#print(sys.path)
#print(utils.__file__)

# B. When importing from a relative directory with "from-import" directive
#    the defintions would be globally available, so we could address
#    like: decorate() immediately
#from utils import *

def get_tests():
	tests = []

	tests.append(Test(0, utils.decorate("Main")))
	tests.append(Test(1, utils.decorate("Secondary")))

	return tests

