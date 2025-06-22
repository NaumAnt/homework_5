import os

from selene import browser, have



class RegistrationPage:
    def __init__(self):
        self.first_name = browser.element('#firstName')
        self.last_name = browser.element('#lastName')
        self.user_email = browser.element('#userEmail')
        self.gender = browser.all('[name=gender]')
        self.user_number = browser.element('#userNumber')
        self.subjects = browser.element('#subjectsInput')
        self.hobbies = browser.all('#hobbiesWrapper label')
        self.upload_pictures = browser.element('#uploadPicture')
        self.current_address = browser.element('#currentAddress')
        self.state = browser.element('#react-select-3-input')
        self.city = browser.element('#react-select-4-input')
        self.submit = browser.element('#submit')
        self.registered_user = browser.all('td')

    def fill_user_registration_form(self, user):
        self.first_name.type(user.first_name)
        self.last_name.type(user.last_name)
        self.user_email.type(user.email)
        self.gender.element_by(have.value(user.gender)).element('..').click()
        self.user_number.type(user.phone_number)
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(user.month)
        browser.element('.react-datepicker__year-select').type(user.year)
        browser.element(
            f'.react-datepicker__day--0{user.day}:not(.react-datepicker__day--outside-month)'
        ).click()
        self.subjects.type(user.subjects).press_enter()
        self.hobbies.element_by(have.exact_text(user.hobbies)).click()
        self.upload_pictures.send_keys(os.path.abspath(user.picture))
        self.current_address.type(user.address)
        self.state.type(user.state).press_enter()
        self.city.type(user.city).press_enter()
        self.submit.click()

    def check_registered_user(self, user):
        self.registered_user.even.should(have.exact_texts(
            f'{user.first_name} {user.last_name}',
            user.email,
            user.gender,
            user.phone_number,
            f'{user.day} {user.month},{user.year}',
            user.subjects,
            user.hobbies,
            user.picture,
            user.address,
            f'{user.state} {user.city}'
        )
        )