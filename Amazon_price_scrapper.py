import bs4, requests

def getAmazonPrice(productURL):
    res = requests.get(productURL)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('#site-footer > nav > ul > li:nth-child(3) > ul > li:nth-child(2) > ul > li:nth-child(3) > span:nth-child(2)')
    return elems[0].text.strip()



price = getAmazonPrice('https://www.goldcu.org/')
print('Gold address is ' + price)
