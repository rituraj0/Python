#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import zipfile


"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them

#Gather a list of the absolute paths of the special files in all the directories

def get_special_paths(direc):
  filenames = os.listdir(direc);
  ans=[];
  for files in filenames:
    match = re.search(r'__\w*__',files);
    if(match):
      ans.append(os.path.abspath(os.path.join(direc,files)));

  #print(ans);
  return ans;


def copy_to(paths , todir):

  if(not os.path.exists(todir) ):
    os.mkdir(todir);
     
  for files in paths:
    shutil.copy(files,todir);

  return;  
    
      
def make_zip(paths , zipname ):
# tp=zipfile.ZipFile( "yzx.zip",'w');
  zp=zipfile.ZipFile( zipname,'w');
  for files in paths:
    zp.write(files);
  return;


def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print ("usage: [--todir dir][--tozip zipfile] dir [dir ...]");
    sys.exit(1)
 
  # copyspecial.py --todir test .
  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print ("error: must specify one or more dirs");
    sys.exit(1)

  # +++your code here+++
  # Call your functions

    # Gather all the special files
  paths = []
  for dirname in args:
    paths.extend(get_special_paths(dirname))

  if todir:
    copy_to(paths, todir)
  elif tozip:
    make_zip(paths, tozip)
  else:
    print ('\n'.join(paths));
  
if __name__ == "__main__":
  main()
