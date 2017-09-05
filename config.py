token = "351273899:AAHVRSW1Fb9c1-Fyh3t21n3097hsy2Zj5nQ"
user = 'username'
password = 'pass'

# optional
proxies = {
  # 'http': 'http://proxy.t-systems.ru:3128',
  # 'https': 'http://proxy.t-systems.ru:3128',
}

ororo_payload = {
    'user[email]': user,
    'user[password]': password,
}
# Need this cause of
headers = {
    'User-Agent': 'Mozilla/5.0 (Platform; Security; OS-or-CPU; Localization; rv:1.4) Gecko/20030624 Netscape/7.1 (ax)'
}
