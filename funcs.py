from requests import Request, Session
import json 


# fear and greed index
def fng():
        
    url = 'https://pro-api.coinmarketcap.com/v3/fear-and-greed/latest'

  

    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY' : 'YOUR_CMC_API'
    }

    session = Session()
    session.headers.update(headers)

    try:
        res = session.get(url)
        data = res.json()['data']
        msg = f"{data['value_classification']} : {data['value']}"

        # print(msg)
        return msg
    except:
        print("Something went wrong")



# info , price / mcap 
def get(coin_symbol , dtl):
        
    url = 'https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest'

    para = {
        'symbol':coin_symbol.lower()
    }

    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY' : 'YOUR_CMC_API'
    }

    session = Session()
    session.headers.update(headers)

    try:
        res = session.get(url,params=para)
        data = res.json()
        # print(data)
        our_coin = data['data'][coin_symbol.upper()][0]
        quote = our_coin['quote']['USD']
        # print(quote)
        if dtl == "price":
            return quote['price']
            
        elif dtl == "mcap":
            return quote['market_cap']
        
        elif dtl == "info":
            msg = f'''
Price : {quote['price']:.2f}
Market Cap : {quote['market_cap']:.2f}
CMC Rank: {our_coin['cmc_rank']}
Market Pairs: {our_coin['num_market_pairs']}
Market_cap_dominance : {quote['market_cap_dominance']}
volume_24h : {quote['volume_24h']}
volume_change_24h: {quote['volume_change_24h']}
percent_change_1h: {quote['percent_change_1h']}
percent_change_24h: {quote['percent_change_24h']}
percent_change_7d: {quote['percent_change_7d']}
percent_change_30d: {quote['percent_change_30d']}
percent_change_60d: {quote['percent_change_60d']}
percent_change_90d: {quote['percent_change_90d']}

'''

            return msg

        # print(data)


    except:
        print("Something went wrong")
    
    
def calc(amount,token):
    price = get(token,'price')
    amount = float(amount)
    return price*amount
    




# fng()
# print(get('btc','price'))
# 
# print(get('btc','info'))


# print(calc('.2','eth'))
