from bs4 import BeautifulSoup

import requests
import urllib.request


def get_year(filename):
  print("in get Year");
  #data=filename.text;
  #page = urllib.request.urlopen("file://");
  
  filepath="C:/Users/Rituraj/Documents/GitHub/Python/Google/babynames/baby1992.html";
   #r  = requests.get("file:///C:/Users/Rituraj/Documents/GitHub/Python/Google/babynames/baby1990.html").decode("utf8")
   #http://C:/Users/Rituraj/Documents/GitHub/Python/Google/babynames/baby1990.html
  file=open(filepath,'rb');
  text=file.read();
  #print(text);
  print("done");  
  soup = BeautifulSoup(text)

  for link in soup.find_all('input'):
    if( link.get('id')=="yob"):
      print(link.get('value'))
	  
  for link in soup.find_all('tr'):
      print(link)	  
  return

def main():
  print("In main");
  get_year("baby1990.html");
  
if __name__ == '__main__':
  main()