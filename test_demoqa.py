import allure

from qa_guru_hw_11.data import users
from qa_guru_hw_11.pages.registration_page import RegistrationPage

def test_demo_qa(setup_browser):
    registration_page = RegistrationPage()
    test_profile = users.student
    with allure.step("Открываем главую страницу GitHub"):
        registration_page.open()
    registration_page.register(test_profile)
    registration_page.should_have_data(test_profile)


