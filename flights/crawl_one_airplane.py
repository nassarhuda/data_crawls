from bs4 import BeautifulSoup
import urllib2

def main():
    jetid = "N923DN"
    my_url = "https://flightaware.com/live/flight/"+jetid
    soup = BeautifulSoup(urllib2.urlopen(my_url).read(), 'html.parser')
    my_table = soup.find_all('table')[7]
    rows = my_table.find_all('tr')
    with open(jetid+'.txt','w') as f:
        for i in range(1,len(rows)-2):
            my_row = rows[i]
            rc = my_row.find_all('td')
            for j in range(0,len(rc)):
                f.write(rc[j].get_text().encode('utf-8') + "\t")
            f.write("\n")
        

main()