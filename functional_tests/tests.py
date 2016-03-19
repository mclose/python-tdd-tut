from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class NewVisitorTest(LiveServerTestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retreive_it_later(self):
        # Seems odd to type this here, but oh well.
        # Fun with functional tests or black box testing.
        # M has heard about a new "cool" online to-do app. She goes
        # to check out its homepage.
        self.browser.get(self.live_server_url)
        
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
        my_list_url = self.browser.current_url
        self.assertRegex(my_list_url, '/lists/.+')
        self.check_for_row_in_list_table('1: Buy some coffee pods')
        
        # There is still a text box inviting me to add another item. I
        # enter "Make some coffee with a coffee pod"
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Make some coffee with a coffee pod')
        inputbox.send_keys(Keys.ENTER)
        
        # The page updates again, and now shows both items on the list
        self.check_for_row_in_list_table('1: Buy some coffee pods')
        self.check_for_row_in_list_table('2: Make some coffee with a coffee pod')

        # Now a new user, Francis, comes along to the site.

        ## We user a new browser session to make sure that no information
        ## of mine is coming through from cookies, etc.
        self.browser.quit()
        self.browser = webdriver.Firefox()

        # Francis visits the home page. There is no signe of my
        # list
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy some coffee pods', page_text)
        self.assertNotIn('Make some coffee', page_text)

        # Francis starts a new list by entering a new item.
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys('Keys.ENTER')

        # Francis gets his own unique URL
        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, '/lists/+.')
        self.assertNotEqual(francis_list_url, my_list_url)

        # Again, there is no trace of Edith's list
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy some coffee pods', page_text)
        self.assertNotIn('Make some coffee', page_text)

        # Satisfied, they both go back to sleep
        self.fail('Finish the test!')
        
        # I visit the URL and my to-do list is still there.
        
        # Satisfied it is saved, I move on to other things.
