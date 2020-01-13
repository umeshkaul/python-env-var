import os
import pprint
env_var = os.environ
print("This script prints Users environment variables:")

pprint.pprint(dict(env_var),width=1)
print("\n\n Users PATH : ")
print("PATH :"+ env_var['PATH'])
