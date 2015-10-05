Feature: Calculating a sum using an iOS app

  Scenario Outline: Calculate a Sum
    Given we are using the "<app>" app, on a "<device_name>" device
      And we input values 8 and 12 into the fields
    When we click the submit button
    Then the value should equal 20

    Examples: Platforms
      | device_name       | app                                                |
      | iPhone 6 Device   | sauce-storage:TestApp-iphoneos.app.zip             |


