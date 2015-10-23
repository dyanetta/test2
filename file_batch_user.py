#!/usr/bin/python

# Again, not a fully fleshed out script - there should be some enforcement
# on the account names - e.g. capital letters are not standard. There should
# also be notification or handling if the username already exists.
#
# Unfortunately, I dont have time to add exception handling. Should be watching
# for OS errors from the os.system call, from reading the config file and should
# be some bounds checking on reading the file, which currently reads the entirely
# file regardless of how big or how many entries it has.

import os
import re
import sys
import crypt
import string
import argparse

parser = argparse.ArgumentParser(description='Batch User Creation')
parser.add_argument('-f', action='store', dest="dataFile", 
                    help="Filename containing the list of users to create", required=True)
args = parser.parse_args()

def createUser(userName):
   userPassword = userName[::-1]
   encryptedPassword = crypt.crypt(userPassword, "22")
   cmd = "useradd -p " + encryptedPassword + " " + userName
   return os.system( cmd )

with open(args.dataFile) as f:
   line = f.readlines()
   for i in line:
      #skip empty lines
      if i == '\n':
         continue
      #semi-colons, commas and whitespace - followed by any whitespace
      #separate the usernames
      for n in re.split(r'[;,\s]\s*', i.rstrip('\n')):
         createUser(n)
















