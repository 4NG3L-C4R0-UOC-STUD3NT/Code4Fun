import site

print("******************************************")
print("package location")
print("******************************************")
print(site.getsitepackages())
print("******************************************")
print(site.getusersitepackages())
print("******************************************")

print("...")
print("...")
print("...")
print("...")


import sysconfig
import struct


print("******************************************")
print("config information")
print("******************************************")
print(sysconfig.get_platform())
print("******************************************")
# what windows platform  32 or 64
print( 8 * struct.calcsize('P'))
print("******************************************")
print(sysconfig.get_python_version())
print("******************************************")
print(sysconfig.get_config_vars())
print("******************************************")


print("...")
print("...")
print("...")
print("...")

import sys
import pprint
import os
import re

print("******************************************")
# prints a list of existing modules
#print( help('modules') )
print("******************************************")
# print all names exported by the module
pprint.pprint(dir(re))
print("******************************************")
# pretty print loaded modules
pprint.pprint(sys.modules)
#print(sys.modules)
print("******************************************")


