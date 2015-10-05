import os
from appium import webdriver

username = os.environ.get('SAUCE_USERNAME')
access_key = os.environ.get('SAUCE_ACCESS_KEY')

@given('we are using the "{app}" app, on a "{device_name}" device')
def step_impl(context, app, device_name):

  desired_caps = {
    "name": context.name,
    "app": app,
    "platformName": "iOS",
    "deviceName": device_name,
    "browserName": "",
    "platformVersion": "8.4",
    "appiumVersion": "1.4.11",
    "deviceOrientation": "portrait"
  }

  url = 'http://%s:%s@ondemand.saucelabs.com:80/wd/hub' % (username, access_key)

  context.driver = webdriver.Remote(url, desired_caps)

@given('we input values 8 and 12 into the fields')
def step_impl(context):
  field_one = context.driver.find_element_by_accessibility_id("TextField1")
  field_one.send_keys("12")

  field_two = context.driver.find_elements_by_class_name("UIATextField")[1]
  field_two.send_keys("8")

@when('we click the submit button')
def step_impl(context):
  button = context.driver.find_element_by_accessibility_id("ComputeSumButton")
  button.click()

@then('the value should equal 20')
def step_impl(context):
  sum = context.driver.find_element_by_class_name("UIAStaticText").text
  assert int(sum) == 20, "ERROR MESSAGE"
