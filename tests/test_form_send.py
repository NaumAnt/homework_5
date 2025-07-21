import os
import allure
from allure_commons.types import Severity
from selene import browser, have

def test_form_send(setup_browser):
    browser.open("https://demoqa.com/automation-practice-form")
    browser.element('#firstName').type('Sergey')
    browser.element('#lastName').type('Druzhko')
    browser.element('#userEmail').type('test@test.com')
    browser.element('.custom-control-label').click()
    browser.element('#userNumber').type('1233211234')

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').element('option[value="1998"]').click()
    browser.element('.react-datepicker__month-select').element('option[value="5"]').click()
    browser.element('[aria-label="Choose Wednesday, July 8th, 1998"]').click()

    browser.element('#subjectsInput').type('econom').press_enter()
    browser.element('[for="hobbies-checkbox-1"]').click()

    image = 'imagetest.png'
    browser.element('#uploadPicture').send_keys(os.path.abspath(image))

    browser.element('#currentAddress').type('ул. Пушкина. д.100')
    browser.element('#react-select-3-input').type('raja').press_enter()
    browser.element('#react-select-4-input').type('jaip').press_enter()

    browser.element('#submit').click()

    browser.element('tbody').should(have.text('Student Name Sergey Druzhko'))
    browser.element('tbody').should(have.text('Student Email test@test.com'))
    browser.element('tbody').should(have.text('Gender Male'))
    browser.element('tbody').should(have.text('Mobile 1233211234'))
    browser.element('tbody').should(have.text('Date of Birth 08 July,1998'))
    browser.element('tbody').should(have.text('Subjects Economics'))
    browser.element('tbody').should(have.text('Hobbies Sports'))
    browser.element('tbody').should(have.text('Picture imagetest.png'))
    browser.element('tbody').should(have.text('Address ул. Пушкина. д.100'))
    browser.element('tbody').should(have.text('State and City Rajasthan Jaipur'))



