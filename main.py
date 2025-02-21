import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# **🔑 Facebook Credentials from Environment Variables**
FB_USERNAME = os.getenv("FB_USERNAME")  # Secure way to get credentials
FB_PASSWORD = os.getenv("FB_PASSWORD")
GROUP_URL = "https://www.messenger.com/t/YOUR_GROUP_ID"

# **🚀 Start WebDriver in Headless Mode**
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run without opening browser
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)
driver.get("https://www.facebook.com/")

# **🔐 Login Karein**
time.sleep(3)
driver.find_element(By.ID, "email").send_keys(FB_USERNAME)
driver.find_element(By.ID, "pass").send_keys(FB_PASSWORD, Keys.RETURN)
time.sleep(5)

# **📩 Open Messenger Group**
driver.get(GROUP_URL)
time.sleep(5)

# **⚙️ Open Group Settings**
settings_button = driver.find_element(By.XPATH, "//*[@aria-label='Chat settings']")
settings_button.click()
time.sleep(2)

# **✏️ Change Group Name**
group_name_field = driver.find_element(By.XPATH, "//*[contains(@placeholder, 'Chat name')]")
group_name_field.clear()
group_name_field.send_keys("🚀 Auto Group Name", Keys.RETURN)
time.sleep(2)

# **🔄 Change Nicknames**
nickname_button = driver.find_element(By.XPATH, "//*[contains(text(), 'Change nicknames')]")
nickname_button.click()
time.sleep(2)

# **📝 Update Nicknames for Everyone**
nickname_fields = driver.find_elements(By.XPATH, "//input[@type='text']")
for field in nickname_fields:
    field.clear()
    field.send_keys("🔥 Auto Nick", Keys.RETURN)
    time.sleep(1)

print("✅ Nicknames and Group Name Updated Successfully!")

# **🚪 Close Browser**
time.sleep(5)
driver.quit()

