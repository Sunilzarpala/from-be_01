import pytest
from selenium import webdriver


class Test_Credence_001:
    @pytest.mark.xfail
    def test_multiplication_001(self):
        a=10
        b=20
        mul=(a*b)
        print("Multiplication of a and b:",mul)
        if mul==200:
            assert True
        else:
            assert False
    @pytest.mark.skip
    def test_substraction_002(self):
        a=25
        b=20
        sub=a-b
        print("Substraction of a-b:",sub)
        if sub== 5:
            assert True
        else:
            assert False
    @pytest.mark.Credence
    def test_credence_site_003(self):
        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://credence.in/")
        if driver.title=="Credence":
            print("You are at credence.in")
            assert True
            driver.close()
        else:
            print("You are at wrong url")
            driver.close()
            assert False


