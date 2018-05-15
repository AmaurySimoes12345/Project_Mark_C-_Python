#Scripts Python - Amaury
import mechanize
br = mechanize.Browser()
br.set_handle_robots(False)
br.addheaders[('User-agent', Firefox)]
br.open('https://www.facebook.com/login.php')
br.select_form(nr=0)
br.form['email'] = 'inserir e-mail'
br.form['pass'] = 'xxxxxxxxxx'
sub = br.submit()
print sub.geturl()