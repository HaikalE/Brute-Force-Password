from urllib.request import urlopen

pass_st=True
url = "https://raw.githubusercontent.com/scipag/password-list/main/countries/password-list-id.txt"
page = urlopen(url)
html_bytes = page.read()
html = html_bytes.decode("utf-8")
html=html.splitlines()
html.pop(0)
pr_2=1
for line in html:
    print('Pass = '+line)
    if (line=='H5s43') :
        pass_st=False
        break
    pr_2+=1 

if (pass_st==False) : print('Password ditemukan')
else : print('Password tidak ditemukan')
