
"""
TASI
"""
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import re
import matplotlib.pyplot as plt
import time
import arabic_reshaper
from arabic_reshaper import ArabicReshaper
from bidi.algorithm import get_display

driver = webdriver.Chrome(executable_path='chromedriver')
driver.maximize_window()
Stored_Data = pd.read_excel('TASI.xlsx')
domain = 'https://sa.investing.com/'

StockPrices_ = []

for i in range(len(Stored_Data['link'])):
    try:
        driver.get(domain+Stored_Data['link'][i]+'-historical-data')
        driver.execute_script("window.scrollTo(0, 800)")
        time.sleep(2)
        
        # Historyical Data - click on the link to get it
        #Last_LINK = driver.find_element('xpath', '/html/body/div/div/div/div/div[2]/main/div/div[6]/nav/ul/li[3]/a').click()
        
        # Historyical Data - click on the date to desplay it
        try:
            driver.find_element('xpath','/html/body/div/div/div/div/div[2]/main/div/div[7]/div/div/div[2]/div[2]/div[2]/div/div[1]').click()
        except:
            driver.find_element('xpath','/html/body/div/div/div/div/div[2]/main/div/div[6]/div/div/div[2]/div[2]/div[2]/div/div[1]').click()
        
        # Specify the date
        try:
            driver.find_element('xpath','/html/body/div/div/div/div/div[2]/main/div/div[7]/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[1]/input').send_keys('01-01-2020')
        except:
            driver.find_element('xpath','/html/body/div/div/div/div/div[2]/main/div/div[6]/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/div/div[1]/input').send_keys('01-01-2020')
        
        # apply the changes
        try:
            driver.find_element('xpath', '/html/body/div/div/div/div/div[2]/main/div/div[7]/div/div/div[2]/div[2]/div[2]/div[2]/div[2]/button').click()
        except:
            driver.find_element('xpath', '/html/body/div/div/div/div/div[2]/main/div/div[6]/div/div/div[2]/div[2]/div[2]/div[2]/div[2]/button').click()
            
        time.sleep(4)
    
    
        
        # we go one level above the table to get the inner HTML that will start from the table itself
        try:
            table_data = driver.find_element('xpath','/html/body/div/div/div/div/div[2]/main/div/div[8]/div/div/div[3]/div').text
        except:
            try:
                table_data = driver.find_element('xpath','/html/body/div/div/div/div/div[2]/main/div/div[7]/div/div/div[3]/div').text
            except:
                try:
                    table_data = driver.find_element('xpath','/html/body/div/div/div/div/div[2]/main/div/div[6]/div/div/div[3]/div').text
                except:
                    break
        
        
        
        # regex for headings
        heading_regex = '[\u0621-\u064A]+[ ]{0,1}[\u0621-\u064A]+'
        
        # regex for data
        data_regex = '\d+\/\d+\/\d+\s\d+\.\d+\s\d+\.\d+\s\d+\.\d+\s\d+\.\d+\s\d+\.\d+[A-Z]\s[-+]*\d+\.\d+\%'
        
        
        Headings = re.findall(heading_regex, table_data) # Done
        Data_Tasi = re.findall(data_regex, table_data) # not sliced yet
        
        
        
        before_oanded = []
        
        
        for j in range(len(Data_Tasi)):
            splited = Data_Tasi[j].split(" ")
            before_oanded.append(splited)
        Final_data = pd.DataFrame(before_oanded)
        Final_data.columns = Headings
        
        
        stockprices = Final_data.iloc[::-1].set_index('تاريخ')
        #20 days to represent the 22 trading days in a month
        stockprices['9'] = stockprices['اخر سعر'].rolling(9).mean()
        stockprices['20'] = stockprices['اخر سعر'].rolling(20).mean()
        stockprices['50'] = stockprices['اخر سعر'].rolling(50).mean()
        stockprices[['اخر سعر','9','20', '50']].plot(figsize=(10,4))
        plt.grid(True)
        plt.title(get_display(arabic_reshaper.reshape(Stored_Data.iloc[i]['short_title'])) + get_display(arabic_reshaper.reshape('المتوسطات المتحركة')))
        plt.axis('tight')
        plt.ylabel(get_display(arabic_reshaper.reshape('السعر')))
        
        StockPrices_.append(stockprices)
    except:
        pass
 
