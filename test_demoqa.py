from qa_guru_hw_11.data import users
from qa_guru_hw_11.data.users import User, student
from qa_guru_hw_11.pages.registration_page import RegistrationPage
from datetime import date

def test_demo_qa():
    registration_page = RegistrationPage()
    test_profile = users.student
    registration_page.open()
    registration_page.register(test_profile)
    registration_page.should_have_data(test_profile)


