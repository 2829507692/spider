import requests
from lxml import etree


class GithubLogin(object):
    def __init__(self):
        self.headers={
            'Host':'github.com',
            'Referer':'https://github.com/',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
        }
        self.user='username'
        self.pwd='password'
        self.session=requests.Session()
        self.loginurl='https://github.com/login'
        self.posturl='https://github.com/session'


    def get_token(self):
        res=self.session.get(self.loginurl,headers=self.headers)
        e=etree.HTML(res.text)
        token=e.xpath("string(//input[@name='authenticity_token']/@value)")
        print(token)
        return token

    def login(self):
        data={
            'commit': 'Sign in',
            'utf8':'✓',
            'webauthn-support':'supported',
            'login':self.user,
            'password':self.pwd,
            'authenticity_token':self.get_token()
        }
        res=self.session.post(self.posturl,data=data,headers=self.headers)
        print(res.text)

lg=GithubLogin()
lg.login()