import allure
import pytest

from qa_guru_hw_11.data import users
from qa_guru_hw_11.pages.registration_page import RegistrationPage

def test_demo_qa(setup_browser):
    registration_page = RegistrationPage()
    test_profile = users.student

    with allure.step('Открываем страницу регистрации'):
        registration_page.open()

    with allure.step('Регистрируем студента'):
        registration_page.register(test_profile)

    with allure.step('Проверяем, что данные сохранены корректно'):
        registration_page.should_have_data(test_profile)


def test_pass_1():
    pass

def test_pass_2():
    pass

def test_pass_3():
    pass


def test_skip_1():
    pytest.skip('skipping this test')

def test_skip_2():
    pytest.skip('skipping this test')

def test_fault_1():
    pytest.xfail('failing this test')

def test_fault_2():
    pytest.xfail('failing this test')