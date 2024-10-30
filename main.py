from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from datetime import datetime
from typing import List, Dict
from dotenv import dotenv_values
import schedule
import sys

config = dotenv_values(".env") # Load the environment variables from the .env file

def login(driver: webdriver.Edge, config: dict):
    driver.get("https://foreupsoftware.com/index.php/booking/19765/2431#welcome")  # URL of the login page

    # Find and click login button
    loginButton = driver.find_element(By.XPATH, '//*[@id="content"]/div/div/p/button')
    loginButton.click()

    # Find and fill in username and password fields, then click enter button
    usernameField = driver.find_element(By.XPATH, '//*[@id="login_email"]')
    passwordField = driver.find_element(By.XPATH, '//*[@id="login_password"]')
    enterButton = driver.find_element(By.XPATH, '//*[@id="login"]/div/div[3]/div[1]/button[1]')

    usernameField.send_keys(config['USERNAME'])
    passwordField.send_keys(config['PASSWORD'])
    enterButton.click()

def reservation(driver: webdriver.Edge, config: dict):
    #go to the reservation page
    driver.get("https://foreupsoftware.com/index.php/booking/19765/2431#teetimes")
    
    #find and click reservation button
    reservationButton = driver.find_element(By.XPATH, '//*[@id="content"]/div/button[2]')  # Change to 2 after testing is complete
    reservationButton.click()
    
    sleep(1) #wait 1 second for the page to load
    
    reservationFields(driver, config)
    sleep(2)
    bookTimes(driver, config)


#fill in the fields for the reservation
def reservationFields(driver: webdriver.Edge, config: dict):
    
    #fill in date
    dateField = driver.find_element(By.XPATH, '//*[@id="date-field"]')
    dateField.click()
    dateField.send_keys(Keys.CONTROL + "a")
    dateField.send_keys(Keys.DELETE)
    dateField.send_keys(config['DATE'])
    dateField.send_keys(Keys.ENTER)
    
    #click 4 players
    fourPlayersButton = driver.find_element(By.XPATH, '//*[@id="nav"]/div/div[3]/div/div/a[4]') #change to a[4] after testing is complete
    fourPlayersButton.click() 
    
    #click 18 holes
    eighteenHolesButton = driver.find_element(By.XPATH, '//*[@id="nav"]/div/div[4]/div[2]/div/a[2]')
    eighteenHolesButton.click()

def bookTimes(driver: webdriver.Edge, config: Dict[str, str]):
    timeElements = driver.find_elements(By.XPATH, '//*[@id="times"]/div/div/div/div/div/div[1]/div[1]/div[1]')
    if len(timeElements) == 0:
        print("No times available")
        return
    
    timeObjects = []

    for timeElement in timeElements:
        time = timeElement.text.strip().lower()
        if 'pm' in time:
            time = time.replace('pm', '')
            if '12' not in time:
                time = str(int(time[:time.index(':')]) + 12) + ':' + time[time.index(':') + 1:]
        else:
            time = time.replace('am', '')
        #only time is used, date remains the same to ensure that times can be compared
        timeObjects.append(datetime.fromisoformat('2024-10-17' + ' ' + time))

    configTime = datetime.fromisoformat('2024-10-17' + ' ' + config['TIME'])
    
    print(timeObjects)
    print(configTime)
    index = timeObjects.index(nearest(timeObjects, configTime))
    print(index)
    timeElements[index].click() 
    
    #Click on the book time button
    bookTimeButton = driver.find_element(By.XPATH, '//*[@id="book_time"]/div/div[3]/button[1]')
    bookTimeButton.click()
    sys.exit('Run successful, exiting...')

def nearest(items: List[datetime], pivot: datetime):
    return min(items, key=lambda x: abs(x - pivot))

def job():
    driver = webdriver.Edge()  # Make sure you have the EdgeDriver installed and in your PATH
    #Login to the website
    login(driver, config)

    #Make a reservation
    reservation(driver, config)

    sleep(2)
    driver.quit()
    
schedule.every(int(config['INTERVAL_IN_SECONDS'])).seconds.do(job)

while True:
    schedule.run_pending()
    sleep(1)