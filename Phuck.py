import os, platform

try:

   import requests

except:

   os.system('pip2 install requests')

bit = platform.architecture()[0]

if bit == '32bit':

    import Phuck

    Phuck.__techq()



