
username = 'spencer'
password = 'asdD1234'


def login(driver):
    driver.get('http://study-miniblog-new.qa.netease.com/')
    driver.send_key('LoginPage', 'Username', username)
    driver.send_key('LoginPage', 'Password', password)
    driver.click('LoginPage', 'Submit')
