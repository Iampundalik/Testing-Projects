from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
import time

search_item = input("Enter the item to be search: ")

driver = webdriver.Chrome()
driver.get("https://www.flipkart.com/")
driver.maximize_window()

try: 
    driver.find_element(By.XPATH,'//input[]').click()
except:
    pass

time.sleep(2)

# def filter_product():
#         driver.find_element(By.XPATH,'//input[@name="q"]').send_keys(search_item)
#         driver.find_element(By.XPATH,'//button[@class="_2iLD__"]').click()
#         time.sleep(2)
#         field = driver.find_element(By.CLASS_NAME,"_24_Dny")
#         print(field)
#         field.click()
#         time.sleep(5)



def Product_details():
            driver.find_element(By.XPATH,'//input[@name="q"]').send_keys(search_item)
            driver.find_element(By.XPATH,'//button[@class="_2iLD__"]').click()
            time.sleep(2)
            all_products = driver.find_elements(By.CLASS_NAME,"_4rR01T")
            for product in all_products:
                product.click()
                driver.switch_to.window(driver.window_handles[1])

                title = driver.find_element(By.CLASS_NAME,"B_NuCI").text
                discounted_price = driver.find_element(By.XPATH,'//div[@class="_30jeq3 _16Jk6d"]').text
                seller = driver.find_element(By.ID,"sellerName").text

                try:
                    actual_price = driver.find_element(By.CLASS_NAME,"_3I9_wc _2p6lqe").text
                    discount = driver.find_element(By.CLASS_NAME,"_3Ay6Sb _31Dcoz").text
                except:
                    pass
            
                print(f"Title: {title}")
                print(f"Discounted Price: {discounted_price}")
                print(f"Seller Name: {seller}")

                try:
                        print(f"Discount: {discount}")
                        print(f"Actual Price: {actual_price}")
                except:    
                        pass

                driver.close()      
                driver.switch_to.window(driver.window_handles[0])

Product_details()

driver.quit()       