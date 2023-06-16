import os

from selene import browser, have, command


def test_student_registration_form():
    # Открытие страницы с формой
    browser.open('/automation-practice-form')
    # Заполнение имени
    browser.element('#Firstname').type('Stanislav')