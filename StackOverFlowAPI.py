def questions_listing(days = 2):
    import requests
    import time
    
    today = round(time.time())
    some_days_ago = today - days*86400
    page = 1
    ask_list = []
    has_more = True

    while has_more == True:       
        url = "https://api.stackexchange.com/2.2/questions"
        querystring = {"order":"desc",
                       "page":page,
                       "pagesize": 100,
                       "sort":"creation",
                       "min": some_days_ago,
                       "todate": today,
                       "fromdate":some_days_ago,
                       "tagged":"Python",
                       "site":"stackoverflow"}
        
        response = requests.get(url, params=querystring)  
        questions_number = len(response.json()['items'])
        for q in range(questions_number):
            ask_list.append((response.json()['items'][q]['title'],
                             response.json()['items'][q]['link']))
                   
        has_more = response.json()['has_more']
        page += 1
        time.sleep(1)
    return print(ask_list)

questions_listing(2)
