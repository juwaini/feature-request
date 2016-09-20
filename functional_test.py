import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestFeatureRequest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_index(self):
        self.browser.get('http://localhost:5000')

        #self.redirect_to_login_page()
        self.go_to_correct_website()
        self.displaying_correct_subpage()
        self.opening_add_new_feature_request_modal()
        self.opening_add_new_client_modal()
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
         
        self.browser.find_element_by_id('client-nav').click()
        WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located((By.ID, "client"))
                )
        self.assertTrue(self.browser.find_element_by_id('client').is_displayed())
       
        self.browser.find_element_by_id('discussion-nav').click()
        WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located((By.ID, "discussion"))
                )
        self.assertTrue(self.browser.find_element_by_id('discussion').is_displayed())

        self.browser.find_element_by_id('feature-request-nav').click()
        WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located((By.ID, "feature-request"))
                )
        self.assertTrue(self.browser.find_element_by_id('feature-request').is_displayed())

    def opening_add_new_feature_request_modal(self):
        """
        Click 'Add New Feature Request' button and open a modal
        """
        self.browser.find_element_by_id('create-feature-request-modal').click()
        WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located((By.ID, "feature-request-modal"))
                )
        self.assertTrue(self.browser.find_element_by_id('feature-request-modal').is_displayed())

        self.assertIn('Create New Feature Request', self.browser.find_element_by_class_name('modal-title').text)
        self.browser.find_element_by_id('create-feature-request-close').click()
        WebDriverWait(self.browser, 10).until(
                EC.invisibility_of_element_located((By.ID, "feature-request-modal")) 
                )

    def checking_for_correct_form_in_add_new_feature_request_modal(self):
        """
        Check form in 'Add New Feature Request Modal
        """

    def opening_add_new_client_modal(self):
        """
        Click 'Add New Feature Request' button and open a modal
        """
        WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located((By.ID, "client-nav")) 
                )

        self.assertTrue(self.browser.find_element_by_id('client-nav').is_displayed())
        self.browser.find_element_by_id('client-nav').click()
        WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located((By.ID, "client-nav")) 
                )
        self.assertTrue(self.browser.find_element_by_id('client-nav').is_displayed())
        
        self.browser.find_element_by_id('create-client-modal').click()
        WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located((By.ID, "client-modal")) 
                )

        self.assertTrue(self.browser.find_element_by_id('client-modal').is_displayed())

        self.assertIn('Create New Client', self.browser.find_element_by_class_name('modal-title').text)
        #self.browser.find_element_by_id('name').keys('Titanium')
        #self.browser.find_element_by_id('email').keys('test@titanium.com')
        #self.browser.find_element_by_id('create-client-submit').click()
        #WebDriverWait(self.browser, 10).until(
        #        EC.alertIsPresent())
        
if __name__ == '__main__':
    unittest.main()
