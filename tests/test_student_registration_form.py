import os
from selene import browser, have, command


def test_student_registration_form():
    # Открытие страницы с формой
    browser.open('https://demoqa.com/automation-practice-form')
    # Заполнение имени
    browser.element('#Firstname').click('#Firstname').type('Stanislav')