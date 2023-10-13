import pyperclip
import pyautogui
import time
import webbrowser

# pseudo code
# -- take screenshot of both of the images
# -- click on the bookmarklet
# -- save the bookmark data to a variable
# -- extract the useful info
# -- store all the three data to a dataframe

# todo


# webbrowser.open("")

def change_tab():
    pyautogui.hotkey('alt', 'tab')
    time.sleep(.05)
    pyautogui.press('enter')

# time.sleep(.5)
# change_tab()
webbrowser.open('www.google.com')

def get_facebook_post_date(link):
    # open the webbrowser
    # pyautogui.hotkey('ctrl'+'n')
    webbrowser.open(link)
    time.sleep(6)

    #position of the visible date
    pos_1 = (626,291,233, 34)
    img1 = pyautogui.screenshot('screenshot.png', region=(pos_1))
    #move the mouse to a positiona
    pyautogui.moveTo(730,307)

    time.sleep(1)
    #position to the hovering image
    pos_2 = (550,335,379,35)
    # pos_2 = (726,426)
    # take a screenshot with pyautoguy for a given position
    img2 = pyautogui.screenshot('screenshot.png', region=(pos_2))
    # text = pytesseract.image_to_string(img)

    #click on the bookmark
    bookmark_pos = (39, 107)
    pyautogui.click(bookmark_pos)
    time.sleep(.3)
    pyautogui.hotkey('ctrl', 'w')

    #get the data from the clipboard
    txt = pyperclip.paste()

    # get the date from the returned data
    print(txt.split('\n')[3])
    print(txt.split('\n')[2])
    maybe_date = txt.split('\n')[3], txt.split('\n')[2]
    return img1, img2, maybe_date
   