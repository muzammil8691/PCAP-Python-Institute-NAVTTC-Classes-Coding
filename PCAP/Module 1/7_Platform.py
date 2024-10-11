'''
The platform module lets you access the underlying platform's data,
i.e., hardware, operating system, and interpreter version information.
'''
print("-------------------Detailed-Platform-Info-------------------")

import platform

print(platform.platform())

print("--------------------Platform-Terse-Aliased------------------")
#By default terse and alaised are both false
#terse if True gives a short info
#aliased if True gives the detailed info


print("When Terse True:    ",platform.platform(terse=True))

print("When Aliased True:  ",platform.platform(aliased=True))



print("-----------------------------------------------")

import platform

print(platform.system())   
print(platform.machine())
print(platform.python_version())
print(platform.processor())
print(platform.version())
print(platform.uname())

print(platform.python_implementation())
print(platform.python_version_tuple()) #the major part of Python's version; the minor part; the patch level number

