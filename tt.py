import requests
import re
import time
import random
url1 = "https://wunder.com.tr/sneaker/adidas-sneaker/adidas-yeezy-boost-350-v2-linen-FY5158"
url2 = "https://wunder.com.tr/yeezy-slide-bone-FW6345"
url3 = "https://wunder.com.tr/yeezy-slide-earth-brown-FV8425"
url4 = "https://wunder.com.tr/sneaker/adidas-sneaker/yeezy-slide-resin-FX0494"
url5 = "https://wunder.com.tr/sneaker/adidas-sneaker/yeezy-boost-700-v3-H67799"
url6 = "https://wunder.com.tr/sneaker/adidas-sneaker/yeezy-boost-350-v2-cinder-FY2903"
url7 = "https://wunder.com.tr/sneaker/adidas-sneaker/yeezy-boost-350-v2-desert-sage-FX9035"
url8 = "https://wunder.com.tr/sneaker/adidas-sneaker/yeezy-boost-350-v2-flax-FX9028"
user_agent_list = [
   #Chrome
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    #Firefox
    'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)'
    "Mozilla/5.0 (68K) AppleWebKit/521.0 (KHTML, like Gecko) Chrome/16.0936.508 Safari/521"
    "Mozilla/5.0 (68K) AppleWebKit/521.0 (KHTML, like Gecko) Chrome/17.01053.782 Safari/521"
    "Mozilla/5.0 (68K) AppleWebKit/521.0 (KHTML, like Gecko) Chrome/24.0714.231 Safari/521"
    "Mozilla/5.0 (68K) AppleWebKit/521.0 (KHTML, like Gecko) Chrome/26.0327.719 Safari/521"
    "Mozilla/5.0 (68K) AppleWebKit/521.0 (KHTML, like Gecko) Chrome/9.0729.617 Safari/521"
    "Mozilla/5.0 (68K) AppleWebKit/522.0 (KHTML, like Gecko) Chrome/14.0269.498 Safari/522"
    "Mozilla/5.0 (68K) AppleWebKit/522.0 (KHTML, like Gecko) Chrome/7.01327.563 Safari/522"
    "Mozilla/5.0 (68K) AppleWebKit/523.0 (KHTML, like Gecko) Chrome/9.0788.618 Safari/523"
    "Mozilla/5.0 (68K) AppleWebKit/524.0 (KHTML, like Gecko) Chrome/25.0658.938 Safari/524"
    "Mozilla/5.0 (68K) AppleWebKit/525.0 (KHTML, like Gecko) Chrome/0.01262.553 Safari/525"
    "Mozilla/5.0 (68K) AppleWebKit/525.0 (KHTML, like Gecko) Chrome/10.0937.789 Safari/525"
    "Mozilla/5.0 (68K) AppleWebKit/525.0 (KHTML, like Gecko) Chrome/22.01114.638 Safari/525"
    "Mozilla/5.0 (68K) AppleWebKit/526.0 (KHTML, like Gecko) Chrome/17.0962.194 Safari/526"
    "Mozilla/5.0 (68K) AppleWebKit/526.0 (KHTML, like Gecko) Chrome/6.0444.852 Safari/526"
    "Mozilla/5.0 (68K) AppleWebKit/527.0 (KHTML, like Gecko) Chrome/13.0606.116 Safari/527"
    "Mozilla/5.0 (68K) AppleWebKit/527.0 (KHTML, like Gecko) Chrome/2.0806.98 Safari/527"
    "Mozilla/5.0 (68K) AppleWebKit/529.0 (KHTML, like Gecko) Chrome/28.01472.736 Safari/529"
    "Mozilla/5.0 (68K) AppleWebKit/530.0 (KHTML, like Gecko) Chrome/4.0558.66 Safari/530"
    "Mozilla/5.0 (68K) AppleWebKit/533.0 (KHTML, like Gecko) Chrome/12.01229.396 Safari/533"
    "Mozilla/5.0 (68K) AppleWebKit/533.0 (KHTML, like Gecko) Chrome/3.01435.644 Safari/533"
    "Mozilla/5.0 (68K) AppleWebKit/534.0 (KHTML, like Gecko) Chrome/4.0595.989 Safari/534"
    "Mozilla/5.0 (68K) AppleWebKit/536.0 (KHTML, like Gecko) Chrome/12.0540.717 Safari/536"
    "Mozilla/5.0 (68K) AppleWebKit/536.0 (KHTML, like Gecko) Chrome/22.0505.833 Safari/536"
    "Mozilla/5.0 (68K) AppleWebKit/537.0 (KHTML, like Gecko) Chrome/4.01483.104 Safari/537"
    "Mozilla/5.0 (68K) AppleWebKit/539.0 (KHTML, like Gecko) Chrome/18.01060.380 Safari/539"
    "Mozilla/5.0 (68K) AppleWebKit/540.0 (KHTML, like Gecko) Chrome/15.0432.943 Safari/540"
    "Mozilla/5.0 (68K) AppleWebKit/540.0 (KHTML, like Gecko) Chrome/3.01341.279 Safari/540"
    "Mozilla/5.0 (68K) AppleWebKit/541.0 (KHTML, like Gecko) Chrome/10.0146.474 Safari/541"
    "Mozilla/5.0 (68K) AppleWebKit/542.0 (KHTML, like Gecko) Chrome/12.0368.86 Safari/542"
    "Mozilla/5.0 (68K) AppleWebKit/544.0 (KHTML, like Gecko) Chrome/16.0175.908 Safari/544"
    "Mozilla/5.0 (68K) AppleWebKit/546.0 (KHTML, like Gecko) Chrome/14.0371.123 Safari/546"
    "Mozilla/5.0 (68K) AppleWebKit/548.0 (KHTML, like Gecko) Chrome/21.0800.732 Safari/548"
    "Mozilla/5.0 (68K) AppleWebKit/549.0 (KHTML, like Gecko) Chrome/0.0708.464 Safari/549"
    "Mozilla/5.0 (68K) AppleWebKit/550.0 (KHTML, like Gecko) Chrome/7.0210.753 Safari/550"
    "Mozilla/5.0 (68K) AppleWebKit/551.0 (KHTML, like Gecko) Chrome/12.0287.562 Safari/551"

]


while 1<2:
    user_agent = random.choice(user_agent_list)
    headers = {'User-Agent': user_agent}
    req1 = requests.get(url1,headers=headers)
    time.sleep(2)
    if re.search('(?i)SOLD OUT',req1.text):
        print('Checked-No Stock Linen')
    else:
        print('Attention-Stocked')

    user_agent = random.choice(user_agent_list)
    headers = {'User-Agent': user_agent}
    req2 = requests.get(url1,headers=headers)
    time.sleep(2)
    if re.search('(?i)SOLD OUT',req2.text):
        print('Checked-No Stock Slide Bone')
    else:
        print('Attention-Stocked')

    user_agent = random.choice(user_agent_list)
    headers = {'User-Agent': user_agent}
    req3 = requests.get(url1,headers=headers)
    time.sleep(2)
    if re.search('(?i)SOLD OUT',req3.text):
        print('Checked-No Stock Slide Earth')
    else:
        print('Attention-Stocked')

    user_agent = random.choice(user_agent_list)
    headers = {'User-Agent': user_agent}
    req4 = requests.get(url1,headers=headers)
    time.sleep(2)
    if re.search('(?i)SOLD OUT',req4.text):
        print('Checked-No Stock Slide Resin')
    else:
        print('Attention-Stocked')

    user_agent = random.choice(user_agent_list)
    headers = {'User-Agent': user_agent}
    req5 = requests.get(url1,headers=headers)
    time.sleep(2)
    if re.search('(?i)SOLD OUT',req5.text):
        print('Checked-No Stock Boost 700')
    else:
        print('Attention-Stocked')

    user_agent = random.choice(user_agent_list)
    headers = {'User-Agent': user_agent}
    req6 = requests.get(url1,headers=headers)
    time.sleep(2)
    if re.search('(?i)SOLD OUT',req6.text):
        print('Checked-No Stock Cinder')
    else:
        print('Attention-Stocked')

    user_agent = random.choice(user_agent_list)
    headers = {'User-Agent': user_agent}
    req7 = requests.get(url1,headers=headers)
    time.sleep(2)
    if re.search('(?i)SOLD OUT',req7.text):
        print('Checked-No Stock Desert Sage')
    else:
        print('Attention-Stocked')

    user_agent = random.choice(user_agent_list)
    headers = {'User-Agent': user_agent}
    req8 = requests.get(url1,headers=headers)
    time.sleep(2)
    if re.search('(?i)SOLD OUT',req8.text):
        print('Checked-No Stock Flax')
    else:
        print('Attention-Stocked')

    pass
