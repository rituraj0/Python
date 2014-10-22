#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Additional basic list exercises

# D. Given a list of numbers, return a list where
# all adjacent == elements have been reduced to a single element,
# so [1, 2, 2, 3] returns [1, 2, 3]. You may create a new list or
# modify the passed in list.
def remove_adjacent(nums):
  n=len(nums);
  i=0;
  j=0;
  for i in range(1,n):
    if(nums[i]==nums[j]):
      continue;
    else:
      j+=1;
      nums[j]=nums[i];
      
  while(len(nums) > j+1): # can use del 
    nums.pop();  
     
  return nums;


# E. Given two lists sorted in increasing order, create and return a merged
# list of all the elements in sorted order. You may modify the passed in lists.
# Ideally, the solution should work in "linear" time, making a single
# pass of both lists.
def linear_merge(list1, list2):
  #lis1=remove_adjacent(list1); // no need to do this
  #lis2=remove_adjacent(list2); // no need to do this
  ans=[];
  i=0;
  j=0;
  k=0;
  n=len(list1);
  m=len(list2);
  
  while( (i<n) and (j<m) ):
    if( list1[i] < list2[j] ):
      ans.append(list1[i]);
      i+=1;
    else:
      ans.append(list2[j]);
      j+=1;

  while( i < n ):
    ans.append(list1[i]);
    i+=1;
  
  while( j < m ):
    ans.append(list2[j]);
    j+=1;
          
  return ans;


# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print ('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


# Calls the above functions with interesting inputs.
def main():
  print ('remove_adjacent')
  test(remove_adjacent([1, 2, 2, 3]), [1, 2, 3])
  test(remove_adjacent([2, 2, 3, 3, 3]), [2, 3])
  test(remove_adjacent([]), [])

  print
  print ('linear_merge')
  test(linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']),
       ['aa', 'bb', 'cc', 'xx', 'zz'])
  test(linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']),
       ['aa', 'bb', 'cc', 'xx', 'zz'])
  test(linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']),
       ['aa', 'aa', 'aa', 'bb', 'bb'])


if __name__ == '__main__':
  main()
