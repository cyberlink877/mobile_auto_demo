import time
import unittest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options


capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='SM-J730GM',
    appPackage='com.android.settings',
    appActivity='.Settings',
    language='en',
    locale='US'
)

appium_server_url = 'http://localhost:4723'
capabilities_options = UiAutomator2Options().load_capabilities(capabilities)


class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(appium_server_url, options=capabilities_options)

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def test_find_settings(self) -> None:
        # el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Battery"]')
        #el = self.driver.find_element(by=AppiumBy.XPATH, value='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[6]/android.widget.LinearLayout/android.widget.TextView[1]')
        el1 = self.driver.find_element(by=AppiumBy.XPATH, value="(//android.widget.ImageView[@resource-id=\"com.sec.android.app.launcher:id/iconview_imageView\"])[2]")
        el1.click()
        time.sleep(5)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestAppium('test_find_settings'))
    unittest.TextTestRunner().run(suite)


