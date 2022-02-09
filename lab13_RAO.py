from selenium import webdriver  # imports selenium to the file

from time import sleep

# create a variable, specify path to chromedriver file

driver = webdriver.Chrome('Chromedriver.exe')

# Make browser full screen

driver.maximize_window()

# Give browser up to 30 seconds to respond

driver.implicitly_wait(30)

# Navigate to Moodle app website

driver.get('https://www.google.ca/')

# Check that Moodle URL and the home page titles are displayed

if driver.current_url == 'https://www.google.ca/' and driver.title == 'Google':
    print(' Hurray! Google Canada Launched Successfully')
    print (f' Google homepage URL: {driver.current_url} \nHome Page Title: {driver.title}')
    sleep(5)
    driver.close()

else:

    print(f'Google Canada did not launch. Check your code or application!')
    print(f' Current URL: {driver.current_url} \nHome Page Title: {driver.title}')
    driver.close()
    driver.quit()


