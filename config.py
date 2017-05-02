token = "token"
user = 'username'
password = 'pass'
# token = "YOUR TELEGRAM TOKEN THERE"

# optional
proxies = {
  'http': 'http://proxy.t-systems.ru:3128',
  'https': 'http://proxy.t-systems.ru:3128',
}

ororo_payload = {
    'user[email]': user,
    'user[password]': password,
}
# Need this cause of
headers = {
    'User-Agent': 'Mozilla/5.0 (Platform; Security; OS-or-CPU; Localization; rv:1.4) Gecko/20030624 Netscape/7.1 (ax)'
}
