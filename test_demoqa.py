import allure

from qa_guru_hw_11.data import users
from qa_guru_hw_11.pages.registration_page import RegistrationPage

def test_demo_qa():
    registration_page = RegistrationPage()
    test_profile = users.student

    with allure.step('Открываем страницу регистрации'):
        registration_page.open()

    with allure.step('Регистрируем студента'):
        registration_page.register(test_profile)

    with allure.step('Проверяем, что данные сохранены корректно'):
        registration_page.should_have_data(test_profile)


