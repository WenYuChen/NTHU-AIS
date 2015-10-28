import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup
# import lxml.html
from secret import user_info
from requests_tools import *

class NTHU_AIS():
    params = {
        'account': user_info['account'],
        'passwd': user_info['password'],
        'passwd2': '848737',
        'Submit': u'登入',
        'fnstr': '20151023-917160844180'
    }
    url_index = 'https://www.ccxp.nthu.edu.tw/ccxp/INQUIRE/'
    url_login = urljoin(url_index, 'pre_select_entry.php')

    def __init__(self):
        pass

    def get_index_page(self):
        # get html of index page
        resp = requests.get('https://www.ccxp.nthu.edu.tw/ccxp/INQUIRE/')
        resp.encoding = 'big5'
        # get the parameters needed to get access token
        soup = BeautifulSoup(resp.text, "html.parser")
        soup_login_table = soup.find('table', attrs={'background':'images/login_mid.png'})
        url_passwd2_img = soup_login_table.find('input', attrs={'name':'passwd2'}).find('img')['src']
        url_passwd2_img = urljoin(self.url_index, url_passwd2_img)
        param_Submit = soup_login_table.find('input', attrs={'name':'Submit'})['value']
        param_fnstr = soup_login_table.find('input', attrs={'name':'fnstr'})['value']

        print(soup.encode('big5'), file=open('get_index_page.out', 'w'))
        print('url_passwd2_img = ' + url_passwd2_img)
        print('Submit = '+param_Submit)
        print('fnstr = '+param_fnstr)
        
        img = requests.get(url_passwd2_img)
        print(img)

    def get_access_token(self):
        resp = requests.post(self.url_login, self.params)
        resp.encoding = 'big5'
        ACIXSTORE = resp.text
        print_to_file('ACIXSTORE', ACIXSTORE, 'get_access_token.out')

    def login(self):
        pass


def main():
    nthu_ais = NTHU_AIS()
    nthu_ais.get_index_page()
    nthu_ais.get_access_token()


if __name__ == '__main__':
    main()
