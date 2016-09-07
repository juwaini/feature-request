import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestFlaskPage(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_index(self):
        self.browser.get('http://localhost:5000')

        #self.redirect_to_login_page()
        self.go_to_correct_website()
        self.displaying_correct_subpage()
        #self.correctly_redirect_to_logout()

    def go_to_correct_website(self):
        """
        Check for webpage title (so far)
        TODO: Check for another elements maybe?
        """
        self.assertIn('BriteCore Feature Request', self.browser.title)

    def displaying_correct_subpage(self):
        """
        Check for default subpage, click leftnav, check whether it changes subpage, then back to
        default subpage
        """
        WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located((By.ID, "feature-request"))
                )
        self.assertTrue(self.browser.find_element_by_id('feature-request').is_displayed())
        
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


if __name__ == '__main__':
    unittest.main()
