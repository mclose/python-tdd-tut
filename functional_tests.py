from selenium import webdriver
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
        self.fail('Finish the test!')
        
        # I'm invited to enter a to-do item right away
        
        # I type "Buy some coffee pods" into a text box
        
        # When I hit enter, the page updates, and not the page lists
        # "1: Buy some coffee pods" as an item in the to-do list
        
        # There is still a text box inviting me to add another item. I
        # enter "Make some coffee with a coffee pod"
        
        # The page updates again, and now shows both items on the list
        
        # I wonder whether the site will remmeber my list. I see that the
        # site has generate a unique URL for me -- there is some information
        # on the page that says so.
        
        # I visit the URL and my to-do list is still there.
        
        # Satisfied it is saved, I move on to other things.

if __name__ == '__main__':
    unittest.main(warnings='ignore')
