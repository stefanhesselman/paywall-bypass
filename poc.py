import sys, requests, time, re, urllib3
from bs4 import BeautifulSoup
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# proxies = {
#     'http': 'http://127.0.0.1:8080',
#     'https': 'http://127.0.0.1:8080',
# }

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/110.0"
}

def getArchivedUrl(url):
    archiveUrl = "https://archive.is/"
    resp = requests.get(archiveUrl + url, headers=headers, verify=False)
    print("[!] Querying archive.is...")
    time.sleep(1)
    if resp.status_code == 200 and "Newest" in resp.text:
        print("[!] Target URL found in cache!")
        time.sleep(0.5)
    else:
        print("[X] Something went wrong :(")
        print("[X] The URL has not been cached yet or the website isn't reachable.")
        sys.exit(-1)
    time.sleep(1)
    print("[!] Fetching cached URL..." + "\n")
    time.sleep(1)
    soup = BeautifulSoup(resp.text, "html.parser")
    for link in soup.findAll('a', attrs={'href': re.compile("^https://archive\.is/[A-Za-z0-9]+$", re.IGNORECASE)}):
        print(link.get('href'))
    sys.exit(-1)

def main():
    if len(sys.argv) != 2:
            print("[*] Paywall bypass: a proof-of-concept.")
            print("[*] For educational purposes only.")
            print("[+] Usage: %s <URL>" % sys.argv[0])
            print("[+] e.g.: %s https://news-website.nl/article" % sys.argv[0])
            sys.exit(-1)
    
    url = sys.argv[1]
    getArchivedUrl(url)

if __name__ == "__main__": 
    main() 
