import os, sys

DEBUG = True

# WRONG: IT DOES NOT MATTER WHETHER append or insert is used here, all what makes difference is how this module is being inserted for reuse
# CORRECT: IT DOES MATTER to use insert at the first location here, so that when this module tries to use some module that exists in the caller's modules && the caller has already inserted his absolute name-clashing "src" path into the first position, we don't receive a name clashing with a resolution to the user's src modules
#          Be careful that one needs to use the full path name of the module, otherwise the module name for example "src" would be resolved to the first based on the directory of the caller instead of the callee (in our case it would be resolved to beta instead of alpha)
#####sys.path.append("src")
srcpath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "src")
sys.path.insert(0, srcpath)
# Note: we used the abspath as __file__ "sometimes" returns only the basename and thus the dirname is returned as empty

# GENERALLY: always PREPEND own packages using the ABSOLUTE PATHS
#            and after importing clean up the path again

import data_provider as dp
sys.path.remove(srcpath)

# If we used
#import src.data_provider as dp
# Then we will be relatively importing data_provider which allows us to import without appending the correct "src" to the PYTHONPATH
# Even though that has following cons:
#   1. Clutter the view
#   2. We have to relatively import all the modules, otherwise when a module is mistakenly absolutely imported it, and its name clashed we would be hardly surviving the debug process
#   3. If a folder got renamed we have to search for all the imports and rename this folder, which is counter-productive

# VERDICT: 
# - Use relative imports to avoid causing side effects to caller modules
# - When it's a neccesity to use absolute imports
#       1. PREPEND own packages using the ABSOLUTE PATHS
#       2. After importing clean up the sys.path again

if DEBUG:
	print("Printing from beta.py")
	print(sys.path)
	print(dp.__file__)
	print("----------------------")

def main():
	tests = dp.get_tests()

	print("Available tests are:")

	for t in tests:
		print("- " + t.name)

if __name__ == '__main__':
	main()

