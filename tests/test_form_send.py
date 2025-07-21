import os
import allure
from allure_commons.types import Severity
from selene import Config, have, command


def test_form_send(setup_browser):
    setup_browser.open("https://demoqa.com/automation-practice-form")
    setup_browser.element('#firstName').type('Sergey')
    setup_browser.element('#lastName').type('Druzhko')
    setup_browser.element('#userEmail').type('test@test.com')
    setup_browser.element('.custom-control-label').click()
    setup_browser.element('#userNumber').type('1233211234')

    setup_browser.element('#dateOfBirthInput').click()
    setup_browser.element('.react-datepicker__year-select').element('option[value="1998"]').click()
    setup_browser.element('.react-datepicker__month-select').element('option[value="5"]').click()
    setup_browser.element('[aria-label="Choose Wednesday, July 8th, 1998"]').click()

    setup_browser.element('#subjectsInput').type('econom').press_enter()
    setup_browser.element('[for="hobbies-checkbox-1"]').perform(command.js.scroll_into_view).click()

    image = 'imagetest.png'
    setup_browser.element('#uploadPicture').send_keys('imagetest.png')

    setup_browser.element('#currentAddress').type('ул. Пушкина. д.100')
    setup_browser.element('#react-select-3-input').type('raja').press_enter()
    setup_browser.element('#react-select-4-input').type('jaip').press_enter()

    setup_browser.element('#submit').click()

    setup_browser.element('tbody').should(have.text('Student Name Sergey Druzhko'))
    setup_browser.element('tbody').should(have.text('Student Email test@test.com'))
    setup_browser.element('tbody').should(have.text('Gender Male'))
    setup_browser.element('tbody').should(have.text('Mobile 1233211234'))
    setup_browser.element('tbody').should(have.text('Date of Birth 08 July,1998'))
    setup_browser.element('tbody').should(have.text('Subjects Economics'))
    setup_browser.element('tbody').should(have.text('Hobbies Sports'))
    setup_browser.element('tbody').should(have.text('Picture imagetest.png'))
    setup_browser.element('tbody').should(have.text('Address ул. Пушкина. д.100'))
    setup_browser.element('tbody').should(have.text('State and City Rajasthan Jaipur'))



