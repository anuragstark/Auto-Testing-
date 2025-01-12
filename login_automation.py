from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from appium.options.android import UiAutomator2Options
import time
import datetime
from pathlib import Path

options = UiAutomator2Options()
options.platform_name = 'Android'
options.device_name = '8ffd1618'
options.automation_name = 'UiAutomator2'
options.platform_version = '11'
options.app_package = 'com.modularitylabs.mobile.a3things'
options.app_activity = 'com.modularitylabs.mobile.a3things.login.LoginActivity'

try:
    #Appium server 
    driver = webdriver.Remote('http://127.0.0.1:4723', options=options)
    time.sleep(5)
    print("Spiralist App Started Successfully")

    #Click on more
    more_button = driver.find_element(By.ID, "com.modularitylabs.mobile.a3things:id/tv_more_logins")
    more_button.click()
    print("Clicked on More button successfully")
    time.sleep(2)

    #Click on sign in
    sign_in_email = driver.find_element(By.XPATH, '//android.widget.TextView[@resource-id="android:id/title" and @text="Sign in with email"]')
    sign_in_email.click()
    print("Clicked on Sign in with Email successfully")
    time.sleep(2)

    #Enter email
    email_field = driver.find_element(By.ID, "com.modularitylabs.mobile.a3things:id/tv_email")
    email_field.click()
    email_field.send_keys("anuragstark.ent@gmail.com")
    print("Email entered successfully")
    time.sleep(1)

    #Enter pswd
    password_field = driver.find_element(By.ID, "com.modularitylabs.mobile.a3things:id/et_password")
    password_field.click()
    password_field.send_keys("Spiralist")
    print("Password entered successfully")
    time.sleep(1)

    #Click sign  in
    sign_in_button = driver.find_element(By.ID, "com.modularitylabs.mobile.a3things:id/btn_login")
    sign_in_button.click()
    print("Clicked Sign In button")
    test_status = "PASS"

except Exception as e:
    print(f"Test failed: {str(e)}")
    test_status = "FAIL"

finally:
    # Gen.report
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    Path("reports").mkdir(exist_ok=True)
    
    report_content = f"""
    <html>
        <head>
            <title>Spiralist Login Test Report</title>
            <style>
                body {{ font-family: Arial; padding: 20px; }}
                .pass {{ color: green; font-weight: bold; }}
                .fail {{ color: red; font-weight: bold; }}
                table {{ border-collapse: collapse; width: 100%; margin-top: 20px; }}
                th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
                th {{ background-color: #f2f2f2; }}
            </style>
        </head>
        <body>
            <h1>Spiralist App Login Test Report</h1>
            <table>
                <tr><th>Test Date/Time</th><td>{timestamp}</td></tr>
                <tr><th>Device ID</th><td>{options.device_name}</td></tr>
                <tr><th>Platform</th><td>{options.platform_name} {options.platform_version}</td></tr>
                <tr><th>App Package</th><td>{options.app_package}</td></tr>
                <tr><th>Status</th><td class="{test_status.lower()}">{test_status}</td></tr>
                <tr><th>Email Used</th><td>anuragstark@gmail.com</td></tr>
            </table>
        </body>
    </html>
    """
    
    report_file = f"reports/spiralist_test_report_{timestamp}.html"
    with open(report_file, "w") as f:
        f.write(report_content)
    
    print(f"\nTest report generated: {report_file}")
    
    # Close app
    if 'driver' in locals():
        time.sleep(3)
        driver.quit()
        print("Spiralist app closed!")