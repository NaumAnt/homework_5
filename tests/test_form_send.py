from pages.form_send import RegistrationPage


import os
from selene import browser, have

def test_form_send(open_form_browser_chrome):

    form_send = RegistrationPage()

    form_send.fill_first_name('Sergey')
    form_send.fill_last_name('Druzhko')
    form_send.fill_user_email('test@test.com')
    form_send.fill_gender('Male')
    form_send.fill_user_number('1233211234')
    form_send.fill_date_of_birth('1998', 'July', '08' )
    form_send.fill_hobbies('Sports')
    form_send.fill_picture('imagetest.png')
    form_send.fill_current_address('ул. Пушкина. д.100')
    form_send.fill_subjects('Economics')
    form_send.fill_state('Rajasthan')
    form_send.fill_city('Jaipur')
    form_send.fill_submit()

    form_send.check_registered_user('Sergey Druzhko', 'test@test.com', 'Male', '1233211234', '08 July,1998',
                                    'Economics', 'Sports', 'imagetest.png', 'ул. Пушкина. д.100',
                                    'Rajasthan Jaipur')



