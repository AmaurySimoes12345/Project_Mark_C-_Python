#instalação e utilização do robobrowser
import robobrowser
import re

url = 'https://m.facebook.com'
loggedin_title = 'Facebook' # isto vai servir para confirmarmos que estamos loggedin, vendo o titulo da pagina para onde fomos redirecionados 

browser = robobrowser.RoboBrowser(history=True, parser='html.parser')
browser.open(url)

form = browser.get_form(id='login_form')
form['email'].value = 'USERNAME'
form['pass'].value = 'PASSWORD'
browser.submit_form(form, submit=form['login'])

redirect_title = re.compile('<title>(.*?)</title>').search(str(browser.parsed)).group(1)

if(redirect_title == loggedin_title):
    print('[+] SUCCESS')
    print('Username: {}\nPassword: {}'.format(form['email'].value, form['pass'].value))
else:
    print('[-] LOGIN FAILED')
