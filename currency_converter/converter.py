import currencyapicom

def converter():
    client = currencyapicom.Client('cur_live_oniUSptASlxtC824jATV726IjZar13PbjWPqBlaI')
    result = client.latest(currencies=['GBP'])
    print(result)
    
converter()
