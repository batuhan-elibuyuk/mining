# # # import time
# # # import pandas as pd
# # # from selenium import webdriver
# # # from selenium.webdriver.common.by import By
# # # from selenium.webdriver.chrome.service import Service
# # # from selenium.webdriver.chrome.options import Options

# # # # Set up ChromeDriver options
# # # options = Options()
# # # options.headless = True  # Runs Chrome in headless mode.
# # # service = Service('/path/to/chromedriver')  # Update with the path to your ChromeDriver

# # # # Initialize the WebDriver
# # # driver = webdriver.Chrome(service=service, options=options)

# # # def get_car_details(url):
# # #     driver.get(url)
# # #     time.sleep(2)  # Allow some time for the page to load
# # #     car_data = {}
# # #     for item in driver.find_elements(By.CSS_SELECTOR, "ul.classifiedInfoList li"):
# # #         key = item.find_element(By.TAG_NAME, "strong").text.strip()
# # #         value = item.find_element(By.TAG_NAME, "span").text.strip()
# # #         car_data[key] = value
# # #     return car_data

# # # def scrape_cars(base_url, total_pages=8):  # Adjust total_pages to get more cars
# # #     cars = []
# # #     for page in range(total_pages):
# # #         print(f"Scraping page {page + 1}")
# # #         driver.get(f"{base_url}?pagingOffset={page * 20}")
# # #         time.sleep(2)  # Allow some time for the page to load
# # #         links = driver.find_elements(By.CSS_SELECTOR, "a.classifiedTitle")
# # #         for link in links:
# # #             car_url = "https://www.sahibinden.com" + link.get_attribute('href')
# # #             cars.append(get_car_details(car_url))
# # #     return cars

# # # # URL to start with
# # # start_url = "https://www.sahibinden.com/toyota"

# # # # Scrape the cars
# # # car_list = scrape_cars(start_url)

# # # # Closing the driver
# # # driver.quit()

# # # # Creating a DataFrame and saving to CSV
# # # df = pd.DataFrame(car_list)
# # # df.to_csv('car_data.csv', index=False)
# # # print("Data saved to 'car_data.csv'.")

# # import time
# # import pandas as pd
# # from selenium import webdriver
# # from selenium.webdriver.common.by import By
# # from selenium.webdriver.chrome.service import Service
# # from selenium.webdriver.chrome.options import Options

# # # Set up ChromeDriver options
# # options = Options()
# # options.headless = True
# # service = Service('/path/to/chromedriver')

# # # Initialize the WebDriver
# # driver = webdriver.Chrome(service=service, options=options)

# # def get_car_details(url):
# #     driver.get(url)
# #     time.sleep(2)  # Added sleep for rate limiting
# #     car_data = {}
# #     for item in driver.find_elements(By.CSS_SELECTOR, "ul.classifiedInfoList li"):
# #         key = item.find_element(By.TAG_NAME, "strong").text.strip()
# #         value = item.find_element(By.TAG_NAME, "span").text.strip()
# #         car_data[key] = value
# #     return car_data

# # def scrape_cars(base_url, total_pages=8):
# #     cars = []
# #     for page in range(total_pages):
# #         print(f"Scraping page {page + 1}")
# #         driver.get(f"{base_url}?pagingOffset={page * 20}")
# #         time.sleep(5)  # Increased sleep for rate limiting
# #         links = driver.find_elements(By.CSS_SELECTOR, "a.classifiedTitle")
# #         for link in links:
# #             car_url = "https://www.sahibinden.com" + link.get_attribute('href')
# #             cars.append(get_car_details(car_url))
# #     return cars

# # start_url = "https://www.sahibinden.com/toyota"

# # car_list = scrape_cars(start_url)

# # driver.quit()

# # df = pd.DataFrame(car_list)
# # df.to_csv('car_data.csv', index=False)
# # print("Data saved to 'car_data.csv'.")

# import time
# import pandas as pd
# from googletrans import Translator, LANGUAGES
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options

# # Set up ChromeDriver options
# options = Options()
# options.headless = True
# service = Service(r'C:\Users\batuh\Desktop\chromedriver.exe')


# # Initialize the WebDriver and Translator
# driver = webdriver.Chrome(service=service, options=options)
# translator = Translator()

# def translate_text(text, dest='en'):
#     try:
#         translation = translator.translate(text, dest=dest)
#         return translation.text
#     except Exception as e:
#         print(f"Error during translation: {e}")
#         return text  # Return the original text if translation fails

# def get_car_details(url):
#     driver.get(url)
#     time.sleep(2)  # Allow some time for the page to load
#     car_data = {}
#     for item in driver.find_elements(By.CSS_SELECTOR, "ul.classifiedInfoList li"):
#         key = item.find_element(By.TAG_NAME, "strong").text.strip()
#         value = item.find_element(By.TAG_NAME, "span").text.strip()
#         # Translate key and value
#         translated_key = translate_text(key)
#         translated_value = translate_text(value)
#         car_data[translated_key] = translated_value
#     return car_data

# def scrape_cars(base_url, total_pages=8):
#     cars = []
#     for page in range(total_pages):
#         print(f"Scraping page {page + 1}")
#         driver.get(f"{base_url}?pagingOffset={page * 20}")
#         time.sleep(5)  # Sleep for rate limiting
#         links = driver.find_elements(By.CSS_SELECTOR, "a.classifiedTitle")
#         for link in links:
#             car_url = "https://www.sahibinden.com" + link.get_attribute('href')
#             cars.append(get_car_details(car_url))
#     return cars

# start_url = "https://www.sahibinden.com/toyota"

# car_list = scrape_cars(start_url)

# driver.quit()

# df = pd.DataFrame(car_list)
# df.to_csv('car_data_translated.csv', index=False)
# print("Data saved to 'car_data_translated.csv'.")

import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Set up ChromeDriver options
options = Options()
options.add_argument(r"C:\Users\batuh\AppData\Local\Google\Chrome\User Data")
# options.add_argument("--profile-directory=Profile X")  # Adjust if using a specific profile
service = Service(r'C:\Users\batuh\Desktop\chromedriver.exe')

# Initialize the WebDriver
driver = webdriver.Chrome(service=service, options=options)

def get_car_details(url):
    driver.get(url)
    time.sleep(2)  # Allow some time for the page to load
    car_data = {}
    for item in driver.find_elements(By.CSS_SELECTOR, "ul.classifiedInfoList li"):
        key = item.find_element(By.TAG_NAME, "strong").text.strip()
        value = item.find_element(By.TAG_NAME, "span").text.strip()
        car_data[key] = value
    return car_data

def scrape_cars(base_url, total_pages=8):
    cars = []
    for page in range(total_pages):
        print(f"Scraping page {page + 1}")
        driver.get(f"{base_url}?pagingOffset={page * 20}")
        time.sleep(5)  # Sleep for rate limiting
        links = driver.find_elements(By.CSS_SELECTOR, "a.classifiedTitle")
        for link in links:
            car_url = "https://www.sahibinden.com" + link.get_attribute('href')
            cars.append(get_car_details(car_url))
    return cars

start_url = "https://www.sahibinden.com/toyota"

car_list = scrape_cars(start_url)

driver.quit()

df = pd.DataFrame(car_list)
df.to_csv('car_data.csv', index=False)
print("Data saved to 'car_data.csv'.")
