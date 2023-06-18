import os
from selene import browser, have, command


def test_student_registration_form():
    # Открытие страницы с формой
    browser.open('/automation-practice-form')
    # Заполнение личных данных
    browser.element('#firstName').type('Stanislav')
    browser.element('#lastName').type('QA')
    browser.element('#userEmail').type('example@mail.ru')
    browser.all('#genterWrapper .custom-control').element_by(have.exact_text('Male')).click()
    browser.element('#userNumber').type('8495556789')
    # Выбор даты рождения
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select [value="1994"]').click()
    browser.element('.react-datepicker__month-select [value="9"]').click()
    browser.element('.react-datepicker__day--028').click()
    # Выбор предмета
    browser.element('#subjectsInput').type('Mobile')
    # Выбор хобби
    browser.all('#hobbiesWrapper .custom-control').element_by(have.exact_text('Sports')).click()
    # Загрузка файла
    browser.element('#uploadPicture').click()