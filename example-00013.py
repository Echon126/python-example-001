# coding: utf8
import re
import time
import requests
from html.parser import HTMLParser


class Myparser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.values = 0

    def handle_starttag(self, tag, attrs):
        def _attr(attrlist, attrname):
            for each in attrlist:
                if attrname == each[0]:
                    return each[1]
            return None

        if tag == 'input' and _attr(attrs, 'name') == '_csrf':
            self.values = _attr(attrs, 'value')


def get_csrf(login):
    data = login.text
    par = Myparser()
    par.feed(data)

    return par.values


def run():
    print("Press 'Ctrl+C' to exit...")

    rule1 = r'http://www\.shicheng\.one/s1/\d+'
    pattern1 = re.compile(rule1)
    pattern2 = re.compile(r'\d+')

    login_url = 'https://www.shicheng.one/user/login'
    home = 'https://www.shicheng.one/member/index?id=16973'

    headers1 = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://www.shicheng.one',
        'Referer': 'https://www.shicheng.one/user/login',
        'Upgrade-Insecure-Requests': '1'
    }

    headers2 = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Referer': '',
        'Upgrade-Insecure-Requests': '1'
    }

    payload = {
        "LoginForm[username]": "1352970608@qq.com",
        "LoginForm[password]": "qwer19900206423",
        "LoginForm[rememberMe]": 0,
        "_csrf": ""
    }

    session_requests = requests.Session()

    login = session_requests.get(login_url)
    csrf = get_csrf(login)
    payload["_csrf"] = csrf
    login = session_requests.post(login_url, data=payload, headers=headers1)
    print(login.status_code)
    getstat = session_requests.get(home)

    urls = list(set(re.findall(pattern1, getstat.text)))
    ids = [re.findall(pattern2, url)[1] for url in urls]
    refresh = ["https://www.shicheng.one/node/refresh?id=" + i for i in ids]

    while True:
        for r, url in zip(refresh, urls):
            headers2['Referer'] = url
            getstat = session_requests.get(r, headers=headers2)

        print('Refresh at ' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        time.sleep(10)


if __name__ == '__main__':
    run()
