#!/usr/bin/python

def printdir(dir):
  filenames = os.listdir(dir)
  for filename in filenames:
    print (filename)  ## foo.txt
    print os.path.join(dir, filename) ## dir/foo.txt (relative to current dir)
    print os.path.abspath(os.path.join(dir, filename))