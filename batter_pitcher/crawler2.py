from bs4 import BeautifulSoup
import urllib2

output_folder = 'output/'

def get_text(my_url):
  try:
    soup = BeautifulSoup(urllib2.urlopen(my_url).read(), 'html.parser')
    my_pre = soup.find_all('pre')[2]
    my_text = my_pre.get_text().strip()
    return my_text
  except Exception as ex:
    return None

def main():
  my_url = "http://www.retrosheet.org/retroID.htm"

  soup = BeautifulSoup(urllib2.urlopen(my_url).read(), 'html.parser')

  my_pre = soup.find_all('pre')[0]
  my_text = my_pre.get_text().strip()

  lines = my_text.split('\n')[1:]
  ids = [line.split(',')[2] for line in lines]
  firstnames = [line.split(',')[1] for line in lines]
  lastnames = [line.split(',')[0] for line in lines]
  
  with open('playerinfo.txt','w') as f:
    f.write("Player ID \tlname fname\n")
    for i in range(0,len(ids)-1):
        f.write(ids[i] + "\t" + lastnames[i] + " " + firstnames[i] + "\n")
    

  for my_id in ids:
    letter = my_id[0].upper()
    my_url = "http://www.retrosheet.org/boxesetc/" + letter + "/MU0_" + my_id + ".htm"
    my_text = get_text(my_url)

    if my_text:
      with open(output_folder + '/' + my_id + '_pitcher_matchup.txt', 'w') as f:
        f.write(my_text)

main()
