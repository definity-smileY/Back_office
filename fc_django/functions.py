import requests
import datetime

def get_exchange():
    today = datetime.datetime.now()
    if today.weekday() >= 5:
        diff = today.weekday() - 4
        today = today - datetime.timedelta(days=diff)
    #주말에 환율을 조회하려하니 조회가 안되서 오늘날짜에 요일을 확인하고 5이상일때 그 값에서 4를 뺴 평일의 환율을 보여주는것       
    today = today.strftime('%Y%m%d')

    auth = 'p3SB2ZeRHglm7XTAkbDyLxPs9CdNtLzY'
    url = 'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey={}&searchdate={}&data=AP01'
    url = url.format(auth, today)
    res = requests.get(url)
    data = res.json()

    
    for d in data:
        if d['cur_unit'] == 'USD':
            return d['tts']
    return
