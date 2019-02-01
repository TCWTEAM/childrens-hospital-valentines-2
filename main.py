#i made this in 2 min before i had to go outside i'll make it better later

import requests
import time
import random
import names

def help(amnt):
    for i in range(int(amnt)):
        url = "https://secure1.chla.org/site/SPageNavigator/valentine2018.html?s_src=vday18hps"
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Host': 'secure1.chla.org',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
        }

        s = requests.session()

        r1 = s.get(url, headers=headers)

        url2 = "https://secure1.chla.org/site/SSurvey?2655_1940_2_1861=Pterodactyl&cons_first_name={}&cons_last_name={}&cons_email={}@gmail.com&2655_1940_5_1864=&ACTION_SUBMIT_SURVEY_RESPONSE=Send+my+valentine&cons_info_component=t&SURVEY_ID=1940".format(names.get_first_name(), names.get_last_name(), str(random.randint(111111111, 999999999)))

        h2 = headers

        r2 = s.get(url2, headers=h2)

        if "Donation2" in r2.url:
            print("Gave $1 To Charity And A Card To A Kid")
if __name__ == '__main__':
    print("LA Childrens Hospital Script")
    print("By @ehxohd")
    print("")
    print("For each entry you give $1 to CHLA")
    print("")
    amnt = input("#Of Entries: ")
    help(amnt)
