from selene import browser, be, have, by, command
import os

from qa_guru_hw_11.data.users import User


class RegistrationPage:

    def open(self):
        browser.open('/automation-practice-form')
        browser.all('[id^=google_ads][id$=container__]').with_(timeout=10).wait_until(
            have.size_greater_than_or_equal(3)
        )
        browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)
        browser.element(".practice-form-wrapper").should(have.text("Student Registration Form"))
        browser.driver.execute_script("$('footer').remove()")
        browser.driver.execute_script("$('#fixedban').remove()")
        return self

    def fill_first_name(self, value):
        browser.element('#firstName').should(be.blank).type(value)
        return self

    def fill_last_name(self, value):
        browser.element('#lastName').should(be.blank).type(value)
        return self

    def fill_email(self, value):
        browser.element('#userEmail').should(be.blank).type(value)
        return self

    def fill_gender(self, value):
        browser.all('[name=gender]').element_by(have.value(value)).element('..').click()
        return self

    def fill_number(self, value):
        browser.element('#userNumber').should(be.blank).type(value)
        return self

    def fill_date(self, date):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').click().element(f'[value="{date.month}"]').click()
        browser.element('.react-datepicker__year-select').click().element(f'[value="{date.year}"]').click()
        browser.all('.react-datepicker__day').element_by(have.exact_text(str(date.day))).click()
        return self

    def fill_subjects(self, value):
        browser.element("#subjectsInput").send_keys(value)
        browser.element("#subjectsInput").press_enter()
        return self

    def fill_hobbies(self, value):
        browser.all('.custom-checkbox').element_by(have.exact_text(value)).click()
        return self

    def upload_img(self, value):
        browser.element('#uploadPicture').send_keys(os.path.join(os.path.abspath('resources'), value))
        return self

    def fill_current_address(self, value):
        browser.element('#currentAddress').should(be.blank).type(value)
        return self

    def fill_state(self, value):
        browser.element('#state').click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(value)
        ).click()
        return self

    def fill_city(self, value):
        browser.element('#city').click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(value)
        ).click()
        return self

    def submit(self):
        browser.element('#submit').click()
        return self

    def should_have_title(self, value):
        browser.element('#example-modal-sizes-title-lg').should(
            have.exact_text(value))
        return self

    def register(self, test_profile: User):
        self.fill_first_name(test_profile.first_name)
        self.fill_last_name(test_profile.last_name)
        self.fill_email(test_profile.email)
        self.fill_gender(test_profile.gender)
        self.fill_number(test_profile.number)
        self.fill_date(test_profile.date_of_birth)
        self.fill_subjects(test_profile.subjects)
        self.fill_hobbies(test_profile.hobby)
        self.upload_img(test_profile.img_file)
        self.fill_current_address(test_profile.current_address)
        self.fill_state(test_profile.state)
        self.fill_city(test_profile.city)
        self.submit()

        pass

    def should_have_data(self, test_profile: User):
        full_name = f'{test_profile.first_name} {test_profile.last_name}'

        months = {0: 'January',
                  1: 'February',
                  2: 'March',
                  3: 'April',
                  4: 'May',
                  5: 'June',
                  6: 'July',
                  7: 'August',
                  8: 'September',
                  9: 'October',
                  10: 'November',
                  11: 'December'
                  }

        full_date = f'{test_profile.date_of_birth.day} {months[test_profile.date_of_birth.month]},{test_profile.date_of_birth.year}'

        browser.element('.table.table-dark.table-striped.table-bordered.table-hover').all('tr').should(
            have.exact_texts(
                f'Label Values',
                f'Student Name {full_name}',
                f'Student Email {test_profile.email}',
                f'Gender {test_profile.gender}',
                f'Mobile {test_profile.number}',
                f'Date of Birth {full_date}',
                f'Subjects {test_profile.subjects}',
                f'Hobbies {test_profile.hobby}',
                f'Picture {test_profile.img_file}',
                f'Address {test_profile.current_address}',
                f'State and City {test_profile.state} {test_profile.city}'
            )
        )






