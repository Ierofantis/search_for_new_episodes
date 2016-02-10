import requests
from bs4 import BeautifulSoup



def main():    

    
    r6=requests.get("http://www.imdb.com/title/tt0106179/episodes?season=10&ref_=tt_eps_sn_105")
    b6=BeautifulSoup(r6.content, "html.parser")
    titles=b6.find_all("div", {"class":"info"})

    print
    print "X-Files"
    print
    
    for link in titles:
        print link.text
        

if __name__ == "__main__":
    main()
