import unittest
import pytest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
from colorama import Fore, Back, Style
import time
from POM.MyAccountPage import MyAccountPage
import HtmlTestRunner
from Utils.screenShot import Screen



@pytest.mark.usefixtures("test_setup")

class TestVerify_BannersHomePage():


    def test_Verify_BannersHomePage(self):
        driver = self.driver
        # driver.get(utils.URL)
        time.sleep(2)
        account = MyAccountPage(driver)



    if __name__ == '__main__':
            unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
                output='C:\\Users\\admin\\PycharmProjects\\TercerProyecto\\Reports'), verbosity=2)
