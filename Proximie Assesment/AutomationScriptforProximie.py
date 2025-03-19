from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
print("Setup Complete")


username = "nvtgubbxgczvrvkjdm@ytnhy.com"
password = "MHXRz6y!aD4BrSdq"
URL="https://old.reddit.com/"
print("Creds Met")
try:
    print("Automation Script Started")
    driver.get(URL)
    time.sleep(3)

    # Perform Login
    login_button = driver.find_element(By.LINK_TEXT, "Log in")
    login_button.click()
    time.sleep(2)

    print("Sending Login Info")
    driver.find_element(By.NAME, "username").send_keys(username)
    driver.find_element(By.NAME, "password").send_keys(password)
    #driver.find_element(By.NAME, "submit").click() #Login button not working
    time.sleep(5)

    #Redirecting to Gaming SubReddit
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("gaming")
    search_box.send_keys(Keys.RETURN)
    time.sleep(5)
    print("Search Completed")

    subreddit_link = driver.find_element(By.PARTIAL_LINK_TEXT, "r/gaming")
    subreddit_link.click()
    time.sleep(5)
    print("Subreddit Link redirected")
    #Get all visible posts (excluding pinned and ads)
    posts = driver.find_elements(By.CSS_SELECTOR, ".thing")

    # Filter out pinned posts and ads
    visible_posts = [post for post in posts if "promoted" not in post.get_attribute("class") and "stickied" not in post.get_attribute("class")]
    print("Filter Posts Completed")
    if len(visible_posts) > 1:
        second_post = visible_posts[1]  # Second visible post
        title = second_post.find_element(By.CSS_SELECTOR, "a.title").text.lower()

        if "nintendo" in title:
            # Upvote
            second_post.find_element(By.CSS_SELECTOR, "button[aria-label='upvote']").click()
            print("Upvote Completed")
        else:
            second_post.find_element(By.CSS_SELECTOR, "button[aria-label='downvote']").click()
            print("Downvote Completed")

    time.sleep(3)
    user_menu = driver.find_element(By.ID, "USER_DROPDOWN_ID")
    user_menu.click()
    time.sleep(2)

    logout_button = driver.find_element(By.LINK_TEXT, "Log Out")
    logout_button.click()
    time.sleep(3)
    print("Logout Performed")

finally:
    driver.quit()  # Close the browser
