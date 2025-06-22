from data_users.users import User
from pages.form_send import RegistrationPage



def test_form_send(open_form_browser_chrome):

    form_send = RegistrationPage()

    user = User(
        first_name='Sergey',
        last_name='Druzhko',
        email='test@test.com',
        gender='Male',
        phone_number='1233211234',
        year='1998',
        month='July',
        day='08',
        subjects='Economics',
        hobbies='Sports',
        picture='imagetest.png',
        address='ул. Пушкина. д.100',
        state='Rajasthan',
        city='Jaipur'
    )

    form_send.fill_user_registration_form(user)


    form_send.check_registered_user(user)



