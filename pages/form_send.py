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

    def fill_first_name(self, value):
        self.first_name.type(value)

    def fill_last_name(self, value):
        self.last_name.type(value)

    def fill_user_email(self, value):
        self.user_email.type(value)

    def fill_gender(self, value):
        self.gender.element_by(have.value(value)).element('..').click()

    def fill_user_number(self, value):
        self.user_number.type(value)

    def fill_date_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(month)
        browser.element('.react-datepicker__year-select').type(year)
        browser.element(
            f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)'
        ).click()

    def fill_subjects(self, value):
        self.subjects.type(value).press_enter()

    def fill_hobbies(self, value):
        self.hobbies.element_by(have.exact_text(value)).click()

    def fill_picture(self, value):
        self.upload_pictures.send_keys(os.path.abspath(value))

    def fill_current_address(self, value):
        self.current_address.type(value)

    def fill_state(self, value):
        self.state.type(value).press_enter()

    def fill_city(self, value):
        self.city.type(value).press_enter()

    def fill_submit(self):
        self.submit.click()

    def check_registered_user(self, student_name, student_email, gender, mobile, date_of_birth, subjects, hobbies,
                              picture, address, state_and_city):
        self.registered_user.even.should(have.exact_texts(
            student_name, student_email, gender, mobile,
            date_of_birth, subjects,
            hobbies, picture, address, state_and_city,
        )
        )


