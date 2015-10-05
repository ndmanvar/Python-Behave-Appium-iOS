import os
from appium import webdriver
from sauceclient import SauceClient

username = os.environ.get('SAUCE_USERNAME')
access_key = os.environ.get('SAUCE_ACCESS_KEY')

def before_scenario(context, scenario):
  context.name = scenario.name

def after_scenario(context, scenario):
  if hasattr(context, 'driver'):
    context.driver.quit()
    sauce_client = SauceClient(username, access_key)
    test_status = scenario.status == 'passed'
    sauce_client.jobs.update_job(context.driver.session_id, passed = test_status)
    