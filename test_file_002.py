import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

class Test_Credence_002:
    @pytest.mark.xfail
    def test_registration_01(self):
        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://automation.credence.in/register")
        driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/input[1]").send_keys("sunilz")
        driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/form[1]/div[2]/div[1]/input[1]").send_keys("Credkart100043@gmail.com")
        driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/form[1]/div[3]/div[1]/input[1]").send_keys("snil122m")
        driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/form[1]/div[4]/div[1]/input[1]").send_keys("snil122m")
        driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/form[1]/div[5]/div[1]/button[1]").click()
        try:
            driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]")
            print("Registration is sucessful")
        except:
            print("Registration is failed")

    @pytest.mark.Credence
    def test_credkart_login_02(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://automation.credence.in/login")
        driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/input[1]").send_keys("Credkart222@gmail.com")
        driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/form[1]/div[2]/div[1]/input[1]").send_keys("snil122m")
        driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/form[1]/div[4]/div[1]/button[1]").click()
        try:
            driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]")
            driver.save_screenshot("C:\\PYTHON PRACTICE\\from begining selenium\\Scrrenshot\\loginsucessful.png")
            print("login is sucessful")
            assert True
            driver.close()
        except:
            print("login is failed")
            driver.close()
            assert False


    @pytest.mark.Credenace
    def test_credkart_order_amount_verification_003(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://automation.credence.in/login")

        driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/input[1]").send_keys("Credkart21@gmail.com")
        driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/form[1]/div[2]/div[1]/input[1]").send_keys("Snil122m@")
        driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/form[1]/div[4]/div[1]/button[1]").click()
        try:
            driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/h2[1]")
            print("login is successful")
        except:
            print("login is failed")

        driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[3]/div[1]/div[1]/a[2]/h3[1]").click()
        driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/form[1]/input[5]").click()
        Apple_macbook_pro_qty = Select(driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/table[1]/tbody[1]/tr[1]/td[3]/select[1]"))
        Apple_macbook_pro_qty.select_by_visible_text('2')
        time.sleep(2)
        driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/a[1]").click()

        driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[4]/div[1]/div[1]/a[2]/h3[1]").click()
        driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/form[1]/input[5]").click()
        Apple_ipad_qty = Select(driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/table[1]/tbody[1]/tr[2]/td[3]/select[1]"))
        Apple_ipad_qty.select_by_index(3)
        time.sleep(3)
        item_length = len(driver.find_elements(By.XPATH, "/html[1]/body[1]/div[1]/table[1]/tbody[1]/tr/td[4]"))
        print(item_length)
        item_price = []
        for r in range(1, item_length - 2):
            val1 = driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/table[1]/tbody[1]/tr[" + str(r) + "]/td[4]").text
            val1 = (val1[1:])
            item_price.append(float(val1))
        print("product_prices", item_price)
        subtotal = (round(sum(item_price), 2))
        tax = round(13 / 100 * (subtotal), 2)
        Total = subtotal + tax

        system_value = []
        for r in range(item_length - 2, item_length + 1):
            val2 = driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/table[1]/tbody[1]/tr[" + str(r) + "]/td[4]").text
            val2 = (val2[1:])
            val = val2.replace(",", "")
            system_value.append(float(val))
        print(system_value)

        if system_value[0] == subtotal:
            print("Subtotal is correct")
        else:
            print("Subtotal is wrong")
        if system_value[1] == tax:
            print("Tax is correct")
        else:
            print("Tax is wrong")
        if system_value[2] == Total:
            print("Total is correct")
        else:
            print("Total is wrong")

    @pytest.mark.xfail
    def test_credkart_checkout_004(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://automation.credence.in/login")
        driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/input[1]").send_keys("Credkart21@gmail.com")
        driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/form[1]/div[2]/div[1]/input[1]").send_keys("Snil122m@")
        driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/form[1]/div[4]/div[1]/button[1]").click()
        driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[3]/div[1]/div[1]/a[2]/h3[1]").click()
        driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/form[1]/input[5]").click()
        driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/a[1]").click()
        driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[4]/div[1]/div[1]/a[2]/h3[1]").click()
        driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/form[1]/input[5]").click()
        driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/a[1]").click()
        driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[3]/div[3]/div[1]/div[1]/a[2]/h3[1]").click()
        driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/form[1]/input[5]").click()
        driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/a[2]").click()
        time.sleep(3)
        driver.find_element(By.XPATH,"/html[1]/body[1]/form[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]").send_keys("sunil")
        driver.find_element(By.XPATH,"/html[1]/body[1]/form[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/input[1]").send_keys("zarpala")
        driver.find_element(By.XPATH,"/html[1]/body[1]/form[1]/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/input[1]").send_keys("9822549998")
        time.sleep(2)
        driver.find_element(By.XPATH,"/html[1]/body[1]/form[1]/div[1]/div[3]/div[1]/div[1]/div[3]/div[1]/div[1]/textarea[1]").send_keys("Khadakwasla")
        driver.find_element(By.XPATH,"/html[1]/body[1]/form[1]/div[1]/div[3]/div[1]/div[1]/div[4]/div[1]/div[1]/input[1]").send_keys("411024")
        Select_city = Select(driver.find_element(By.XPATH,"/html[1]/body[1]/form[1]/div[1]/div[3]/div[1]/div[1]/div[4]/div[2]/div[1]/select[1]"))
        Select_city.select_by_visible_text("Pune")
        time.sleep(2)
        driver.find_element(By.XPATH,"/html[1]/body[1]/form[1]/div[1]/div[3]/div[2]/div[1]/div[2]/div[1]/input[1]").send_keys("Sunilz")
        driver.find_element(By.XPATH,"/html[1]/body[1]/form[1]/div[1]/div[3]/div[2]/div[1]/div[2]/div[2]/input[1]").send_keys("043")
        driver.find_element(By.XPATH,"/html[1]/body[1]/form[1]/div[1]/div[3]/div[2]/div[1]/div[2]/div[3]/input[1]").send_keys("5281")
        driver.find_element(By.XPATH,"/html[1]/body[1]/form[1]/div[1]/div[3]/div[2]/div[1]/div[2]/div[3]/input[1]").send_keys("0370")
        driver.find_element(By.XPATH,"/html[1]/body[1]/form[1]/div[1]/div[3]/div[2]/div[1]/div[2]/div[3]/input[1]").send_keys("4891")
        driver.find_element(By.XPATH,"/html[1]/body[1]/form[1]/div[1]/div[3]/div[2]/div[1]/div[2]/div[3]/input[1]").send_keys("6168")
        time.sleep(3)
        Select_EXp_year = Select(driver.find_element(By.XPATH,"/html[1]/body[1]/form[1]/div[1]/div[3]/div[2]/div[1]/div[2]/div[4]/select[2]"))
        Select_EXp_year.select_by_index(2)
        Select_EXp_month = Select(driver.find_element(By.XPATH,"/html[1]/body[1]/form[1]/div[1]/div[3]/div[2]/div[1]/div[2]/div[4]/select[1]"))
        Select_EXp_month.select_by_index(2)
        time.sleep(2)
        driver.find_element(By.XPATH, "/html[1]/body[1]/form[1]/div[1]/div[3]/div[2]/button[1]").click()
        try:
            driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/p[2]")
            time.sleep(2)
            print(driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/p[2]").text)
            print("order is placed Sucessfully")
        except:
            print("Order is failed to place")


