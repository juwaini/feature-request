import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestFlaskPage(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def test_index(self):
        self.browser.get('http://localhost:5000')
        self.assertIn('BriteCore Feature Request', self.browser.title)

        self.browser.find_element_by_id('discussions-nav').click()

        WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located((By.ID, "discussions"))
                )
        
        self.assertTrue(self.browser.find_element_by_id('discussions').is_displayed())

        self.browser.find_element_by_id('feature-request-nav').click()

        WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located((By.ID, "feature-request"))
                )

        self.assertTrue(self.browser.find_element_by_id('feature-request').is_displayed())

    def tearDown(self):
        self.browser.quit()

if __name__ == '__main__':
    unittest.main()
