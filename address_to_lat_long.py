import pyautogui
import time

class delay:
    
    def delay_one_quarter_second():
        time.sleep(0.25)
    
    def delay_one_second():
        time.sleep(1)
    
    def delay_five_seconds():
        time.sleep(5)

class Navigation:
    
    def open_chrome():
        pyautogui.click(192, 1064, button='left')
    
    def focus_searchbar():
        pyautogui.click(724, 81, button='left')
    
    def chrome_search():
        Navigation.focus_searchbar(); pyautogui.write('https://www.latlong.net/convert-address-to-lat-long.html')
        
    def focus_address_field():
        pyautogui.click(483,457, button='left')
    
    def add_second_tab():
        pyautogui.click(269, 45, button='left')
    
    def scroll():
        pyautogui.scroll(200)