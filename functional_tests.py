from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retreive_it_later(self):
        # Seems odd to type this here, but oh well.
        # Fun with functional tests or black box testing.
        # M has heard about a new "cool" online to-do app. She goes
        # to check out its homepage.
        self.browser.get('http://localhost:8000')
        
        # I notice the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)
        
        # I'm invited to enter a to-do item right away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
                inputbox.get_attribute('placeholder'),
                'Enter a to-do item'
                )
        
        # I type "Buy some coffee pods" into a text box
        inputbox.send_keys('Buy some coffee pods')
        
        # When I hit enter, the page updates, and not the page lists
        # "1: Buy some coffee pods" as an item in the to-do list
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
                any(row.text == '1: Buy some coffee pods' for row in rows),
                "New to-do item did not appear in table"
                )
        
        # There is still a text box inviting me to add another item. I
        # enter "Make some coffee with a coffee pod"
        self.fail('Finish the test!')
        
        # The page updates again, and now shows both items on the list
        
        # I wonder whether the site will remmeber my list. I see that the
        # site has generate a unique URL for me -- there is some information
        # on the page that says so.
        
        # I visit the URL and my to-do list is still there.
        
        # Satisfied it is saved, I move on to other things.

if __name__ == '__main__':
    unittest.main(warnings='ignore')
