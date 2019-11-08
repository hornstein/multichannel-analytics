# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

import unittest, time, re, random
from random import randint

import numpy as np
import uuid

import requests
import json

import sqlite3
conn = sqlite3.connect('/home/ros/Downloads/multichannel.db', check_same_thread=False)
c = conn.cursor()

class MultiChannelCustomerSimulation(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('/home/ros/Downloads/chromedriver')
        #self.driver = webdriver.Firefox(executable_path='/home/bluebottle/Downloads/geckodriver')
        #self.driver = webdriver.Remote(command_executor='http://dockerselenium.azurewebsites.net/wd/hub/',desired_capabilities={'platform':'All','browserName':'firefox'})
        self.driver.implicitly_wait(10)
        #self.driver.set_window_size(1024, 2024)
        self.base_url = "http://www.bluebottlesurfboards.com/"
        self.verificationErrors = []
        self.accept_next_alert = True


    def enterThroughChannel(self, group, mygender, myyear, myzip, myid, isreturning):
        print (myid)
        driver = self.driver

        channels=['direct', 'social', 'organic', 'referral_surfineurope', 'referral_boardcad', 'email', 'radio']
        group_probabilities_channels=[[0.1, 0.1, 0.1, 0.4, 0.1, 0.2, 0.0],
                                     [0.2, 0.3, 0.1, 0.1, 0.1, 0.1, 0.1],
                                     [0.4, 0.0, 0.1, 0.1, 0.2, 0.0, 0.2]]
        my_channel=np.random.choice(7, 1, p=group_probabilities_channels[group])[0]

        #print my_channel

        #my_channel=5
        driver.get(self.base_url + 'dummy.html')

        cookie = {'expiry': 1636207927, 'secure': False, 'path': '/', 'name': '_ga', 'value': 'GA1.2.1211559674.' + myid, 'httpOnly': False, 'domain': '.bluebottlesurfboards.com'}
        
        driver.add_cookie(cookie)

        if channels[my_channel]=='direct':
            driver.get(self.base_url)

        if channels[my_channel]=='email':

            #jsondata={"name": "email", "domain": "", "gender": mygender, "year": str(myyear), "zip": str(myzip), "id": myid, "isreturning": isreturning} 
            #res = requests.post('http://localhost:8080/bidrequest',  headers={'Content-Type': 'application/json'}, data=json.dumps(jsondata))
            #response = res.json()
            #print response
            #print response['group']

            driver.get(self.base_url+'?utm_source=newsletter&utm_medium=email&utm_campaign=cyber_monday')
            #driver.get(self.base_url+'?utm_source=newsletter&utm_medium=email&utm_campaign=black_friday&utm_content='+response['group'])

        if channels[my_channel]=='radio':

            #jsondata={"name": "gp", "domain": "", "gender": mygender, "year": str(myyear), "zip": str(myzip), "id": myid, "isreturning": isreturning} 
            #res = requests.post('http://localhost:8080/bidrequest',  headers={'Content-Type': 'application/json'}, data=json.dumps(jsondata))
            #response = res.json()
            #print response
            #print response['group']

            driver.get(self.base_url+'/radio')

            #driver.get(self.base_url+'?utm_source=gp&utm_medium=newspaper&utm_campaign=superdupersale')
            #driver.get(self.base_url+'?utm_source=gp&utm_medium=newspaper&utm_campaign=superdupersale&utm_content='+response['group'])

        if channels[my_channel]=='social':

            #jsondata={"name": "facebook", "domain": "", "gender": mygender, "year": str(myyear), "zip": str(myzip), "id": myid, "isreturning": isreturning} 
            #res = requests.post('http://localhost:8080/bidrequest',  headers={'Content-Type': 'application/json'}, data=json.dumps(jsondata))
            #response = res.json()
            #print response
            #print response['group']

            driver.get(self.base_url + 'social.html')
            #driver.find_element_by_link_text("Bluebottle surfboards").click()
            
            #driver.find_element_by_link_text("Bluebottle surfboards "+response['group']).click()
            #driver.find_element_by_xpath('//a[@href="http://www.bluebottlesurfboards.com"]')
            #driver.get('https://www.facebook.com/Bluebottle-Surfboards-170163783047234/')
            #driver.find_element_by_xpath('//*[@id="u_0_p"]/div/a[2]').click()

        if channels[my_channel]=='organic':
            driver.get(self.base_url + 'organic.html')
            #driver.find_element_by_link_text("Bluebottle surfboards").click()
            
            #driver.find_element_by_xpath('//a[@href="http://www.bluebottlesurfboards.com"]')
            #driver.get('https://www.google.se/search?q=bluebottlesurfboards')
            #driver.find_element_by_xpath('//a[@href="http://www.bluebottlesurfboards.com/"]')


        if channels[my_channel]=='referral_surfineurope':
            driver.get(self.base_url + 'surfineurope.html')
            #driver.find_element_by_link_text("Bluebottle surfboards").click()
            
            #driver.find_element_by_xpath('//a[@href="http://www.bluebottlesurfboards.com"]')
            #driver.get('http://www.surfineurope.net')
            #driver.find_element_by_xpath('//a[@href="http://www.bluebottlesurfboards.com"]')


        if channels[my_channel]=='referral_boardcad':

            #jsondata={"name": "aftonbladet", "domain": "", "gender": mygender, "year": str(myyear), "zip": str(myzip), "id": myid, "isreturning": isreturning} 
            #res = requests.post('http://localhost:8080/bidrequest',  headers={'Content-Type': 'application/json'}, data=json.dumps(jsondata))
            #response = res.json()
            #print response
            #print response['group']

            driver.get(self.base_url + 'boardcad.html')
            #driver.find_element_by_link_text("Bluebottle surfboards").click()
            
            #driver.find_element_by_link_text("Bluebottle surfboards "+response['group']).click()
            #driver.find_element_by_xpath('//a[@href="http://www.bluebottlesurfboards.com"]')
            #driver.get('http://www.boardcad.com')
            #driver.find_element_by_xpath('//a[@href="http://www.bluebottlesurfboards.com"]')

        mycookies=driver.get_cookies()
        print (mycookies)


    def registerUser(self, group, mygender, myyear, myzip, myemail):

        driver = self.driver
        driver.get(self.base_url)

        driver.find_element_by_link_text("Skapa konto").click()
        driver.find_element_by_id(mygender).click()
        driver.find_element_by_id("FirstName").clear()
        driver.find_element_by_id("FirstName").send_keys("Firstname")
        driver.find_element_by_id("LastName").clear()
        driver.find_element_by_id("LastName").send_keys("Lastname")
        Select(driver.find_element_by_name("DateOfBirthDay")).select_by_visible_text("3")
        Select(driver.find_element_by_name("DateOfBirthMonth")).select_by_visible_text("augusti")
        Select(driver.find_element_by_name("DateOfBirthYear")).select_by_visible_text(str(myyear))
        driver.find_element_by_id("Email").clear()
        driver.find_element_by_id("Email").send_keys(myemail)
        driver.find_element_by_id("Company").clear()
        driver.find_element_by_id("Company").send_keys("Group" + str(group))
        driver.find_element_by_id("Password").clear()
        driver.find_element_by_id("Password").send_keys("Password123")
        driver.find_element_by_id("ConfirmPassword").clear()
        driver.find_element_by_id("ConfirmPassword").send_keys("Password123")
        driver.find_element_by_id("register-button").click()
        driver.find_element_by_name("register-continue").click()

        # Add address
        driver.find_element_by_link_text("Mitt konto").click()
        driver.find_element_by_link_text("Mina adresser").click()

        driver.find_element_by_xpath('/html/body/div[6]/div[3]/div/div[2]/div/div[2]/div[2]/input').click()
        driver.find_element_by_id("Address_FirstName").clear()
        driver.find_element_by_id("Address_FirstName").send_keys("Jonas")
        driver.find_element_by_id("Address_LastName").clear()
        driver.find_element_by_id("Address_LastName").send_keys("Test")
        driver.find_element_by_id("Address_Email").clear()
        driver.find_element_by_id("Address_Email").send_keys(myemail)
        Select(driver.find_element_by_id("Address_CountryId")).select_by_visible_text("Sweden")
        driver.find_element_by_id("Address_City").clear()
        driver.find_element_by_id("Address_City").send_keys("Test")
        driver.find_element_by_id("Address_Address1").clear()
        driver.find_element_by_id("Address_Address1").send_keys("Gatan 1")
        driver.find_element_by_id("Address_ZipPostalCode").clear()
        driver.find_element_by_id("Address_ZipPostalCode").send_keys(myzip)
        driver.find_element_by_id("Address_PhoneNumber").clear()
        driver.find_element_by_id("Address_PhoneNumber").send_keys("0706112300")
        driver.find_element_by_xpath('/html/body/div[6]/div[3]/div/div[2]/form/div/div[2]/div[2]/input').click()


    def removeFromCart(self):
        driver = self.driver
        driver.get(self.base_url + 'cart')
        elements = driver.find_elements_by_css_selector('td.remove-from-cart input')
        for element in elements:
            element.click()
        if len(elements)>0:
            driver.find_element_by_css_selector('.update-cart-button').click()

    def loginUser(self, myemail):

        driver = self.driver
        driver.get(self.base_url)

        #lines = open('username100.txt').read().splitlines()
        #myuser =random.choice(lines)
        #print(myuser)
        driver.find_element_by_link_text("Logga in").click()
        driver.find_element_by_id("Email").clear()
        driver.find_element_by_id("Email").send_keys(myemail)
        driver.find_element_by_id("Password").clear()
        driver.find_element_by_id("Password").send_keys("Password123")
        driver.find_element_by_xpath('/html/body/div[6]/div[3]/div/div/div/div[2]/div[1]/div[2]/form/div[3]/input').click()

    def browseCategory(self, group):

        driver = self.driver

        categories=['surf', 'kite', 'windsurf-2']

        group_probabilities=[[0.8, 0.1, 0.1],
                            [0.1, 0.8, 0.1],
                            [0.1, 0.1, 0.8]]

        my_probabilities=group_probabilities[group]


        group_probabilities_exit=[0.2, 0.3, 0.1]
        my_probabilities_exit=group_probabilities_exit[group]
        
        #driver.get(self.base_url + "/")
        added_to_cart = False

        for n in range(6):
            # print n
            if random.random()<my_probabilities_exit:
                return False
            i=0
            for category in categories:
                i=i+1
                if random.random()<my_probabilities[i-1]:
                    driver.get(self.base_url + category)
                    if random.random()<0.2:
                        a=[]
                        a = driver.find_elements_by_class_name("product-box-add-to-cart-button")
                        random.choice(a).click()
                        added_to_cart = True

        return added_to_cart


    def orderProduct(self, group):

        driver = self.driver

        driver.find_element_by_link_text("Varukorg").click()
        driver.find_element_by_id("termsofservice").click()
        driver.find_element_by_id("checkout").click()
        time.sleep(3)
        driver.find_element_by_css_selector("input.button-1.new-address-next-step-button").click()
        time.sleep(3)
        driver.find_element_by_css_selector("#shipping-buttons-container > input.button-1.new-address-next-step-button").click()
        time.sleep(3)
        driver.find_element_by_css_selector("input.button-1.shipping-method-next-step-button").click()
        driver.find_element_by_id("paymentmethod_1").click()
        time.sleep(3)
        driver.find_element_by_css_selector("input.button-1.payment-method-next-step-button").click()
        time.sleep(3)
        driver.find_element_by_css_selector("input.button-1.payment-info-next-step-button").click()
        time.sleep(3)
        driver.find_element_by_css_selector("input.button-1.confirm-order-next-step-button").click()
        time.sleep(3)
        driver.find_element_by_css_selector("input.button-1.order-completed-continue-button").click()
        time.sleep(5)


    def test_group2_selenium_script(self):
        
        print('starting test case')

        mygroup=random.randrange(3)

        # returning customer?
        returning=['yes', 'no']
        group_probabilities_returning=[[0.7, 0.3],
                                  [0.5, 0.5],
                                  [0.9, 0.1]]
        isreturning=np.random.choice(2, 1, p=group_probabilities_returning[mygroup])[0]

        #isreturning=1

        if (returning[isreturning]=='yes'):
            c.execute("SELECT * FROM users WHERE groupnr=" + str(mygroup) + " ORDER BY random() LIMIT 1")
            all_rows = c.fetchall()
            myid=all_rows[0][0]
            myemail=all_rows[0][1]
            myyear=all_rows[0][2]
            mygender=all_rows[0][3]
            myzip=all_rows[0][4]

        else:
            # generate id
            myid=str(randint(1000000000,9999999999))
            #myid=str(uuid.uuid4())

            # generate email
            myemail="3bitstest+" + myid + "@gmail.com"

            # generate gender
            gender=['gender-male', 'gender-female']
            group_probabilities_gender=[[0.5, 0.5],
                                       [0.2, 0.8],
                                       [0.8, 0.2]]
            mygenderid=np.random.choice(2, 1, p=group_probabilities_gender[mygroup])[0]
            mygender=gender[mygenderid]

            # generate age
            if mygroup==0:
                age=random.randint(20, 60)
            if mygroup==1:
                age=random.randint(20, 40)
            if mygroup==2:
                age=random.randint(40, 60)
            myyear=2019-age

            # print myyear

            # generate zip
            zipcode=['20800', '11000', '40010']
            group_probabilities_zipcode=[[0.25, 0.5, 0.25],
                                       [0.5, 0.25, 0.25],
                                       [0.25, 0.25, 0.5]]
            myzipid=np.random.choice(3, 1, p=group_probabilities_zipcode[mygroup])[0]
            myzip=zipcode[myzipid]



 
        self.enterThroughChannel(mygroup, mygender, myyear, myzip, myid, returning[isreturning])

        group_probabilities_bounce=[0.3, 0.5, 0.1]
        my_probabilities_bounce=group_probabilities_bounce[mygroup]
        if random.random()<my_probabilities_bounce:
            return

        login=['yes', 'no']
        group_probabilities_login=[[0.5, 0.5],
                                  [0.2, 0.8],
                                  [0.8, 0.2]]
        isloggedin=np.random.choice(2, 1, p=group_probabilities_login[mygroup])[0]


        if login[isloggedin]=='yes':
            if returning[isreturning]=='yes':
                print('Returning customer')
                self.loginUser(myemail)
                self.removeFromCart()
            else:
                print('Register new user')
                self.registerUser(mygroup, mygender, myyear, myzip, myemail)
                # store user in database
                c.execute("INSERT INTO users VALUES ('"+myid+"', '"+myemail+"'," +str(myyear)+", '"+mygender+"', '"+myzip+"', "+str(mygroup)+")")
                conn.commit()

        result=self.browseCategory(mygroup)

        print(result)

        if result:
            self.orderProduct(mygroup)


      
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
