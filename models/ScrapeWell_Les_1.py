import requests #Requests is a Python HTTP library.So, basically with the help of this library we make a request to a web page.
import bs4
from bs4 import BeautifulSoup
import pandas as pd

def go():
    page_url = "https://www.flipkart.com/grocery/~cs-bwfvg4cxsk/pr?sid=73z&marketplace=GROCERY&collection-tab-name=Grocery+Super+Savers&businessZone=bz_luc_bij_wh_g_01&p%5B%5D=facets.brand%255B%255D%3DTata%2BSampann&p%5B%5D=facets.brand%255B%255D%3DPillsbury&p%5B%5D=facets.brand%255B%255D%3DUttam%2BSugar&p%5B%5D=facets.brand%255B%255D%3DPriyagold&p%5B%5D=facets.brand%255B%255D%3DNaturoz&p%5B%5D=facets.brand%255B%255D%3DLipton&wid=6.cartPMU.BASKET_PMU_4&otracker=clp_basket_pmu_Today%2527s%2BOffer_grocery-supermart-store_AGIM02PJHJUZ_4&otracker1=clp_basket_pmu_PINNED_neo%2Fmerchandising_Today%2527s%2BOffer_MULTI_GRID_VIEW_wc_view-all_4&cid=AGIM02PJHJUZ"
    page_sourced = requests.get(page_url).content #we "search" for the website
    html_content = BeautifulSoup(page_sourced,"html.parser")
    items=[]
    prices=[]

    for i in html_content.findAll('div', attrs={'class':'_2gX9pM'}):
        price = i.find('div', attrs={'class':'_30jeq3 _3aGlZL'})
        prices.append(price.text)
        links=i.find('a',href=True)
        item_titles=links.get('title')
        items.append(item_titles)

    df = pd.DataFrame({'Items on Offer':items,'Discounted Price':prices})
    return df.to_html()





#req = Request('https://grofers.com/cn/grocery-staples/cid/16', headers={'User-Agent': 'Mozilla/5.0'})
#webpage = urlopen(req).read()