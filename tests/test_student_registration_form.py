from selene import browser, have, be, command
import os

def test_student_registration_form():
    # Opening the page with the practice form
    browser.open('/automation-practice-form')
    browser.element('footer').execute_script('element.remove()')

    # Filling out the practice form
    browser.element('#firstName').type('Stanislav')
    browser.element('#lastName').type('QA')
    browser.element('#userEmail').type('example@mail.ru')
    browser.all('#genterWrapper .custom-control').element_by(have.exact_text('Male')).click()
    browser.element('#userNumber').type('8495556789')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select [value="1994"]').click()
    browser.element('.react-datepicker__month-select [value="10"]').click()
    browser.element('.react-datepicker__day--028').click()
    browser.element('#subjectsInput').type('His').press_enter()
    browser.all('#hobbiesWrapper .custom-control').element_by(have.exact_text('Sports')).click()
    browser.element('#uploadPicture').send_keys(os.getcwd() + '\Image\Picture.png')
    browser.element('#currentAddress').should(be.blank).type('Russian Federation, Moscow, Lesnaya str.')
    browser.element('#currentAddress').type('Test Address')
    browser.execute_script('window.scrollBy(0, 200);')
    browser.element('#state').click()
    browser.all('#state div').element_by(have.exact_text('NCR')).click()
    browser.element('#city').click()
    browser.all('#city div').element_by(have.exact_text('Delhi')).click()
    browser.element('#submit').perform(command.js.click)

    # Tests for data submitted
    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    browser.element('.table-responsive').should(have.text('Stanislav'))
    browser.element('.table-responsive').should(have.text('QA'))
    browser.element('.table-responsive').should(have.text('example@mail.ru'))
    browser.element('.table-responsive').should(have.text('Male'))
    browser.element('.table-responsive').should(have.text('8495556789'))
    browser.element('.table-responsive').should(have.text('28 November,1994'))
    browser.element('.table-responsive').should(have.text('History'))
    browser.element('.table-responsive').should(have.text('Sports'))
    browser.execute_script('window.scrollBy(0, 200);')
    browser.element('.table-responsive').should(have.text('Picture.png'))
    browser.element('.table-responsive').should(have.text('Russian Federation, Moscow, Lesnaya str.'))
    browser.element('.table-responsive').should(have.text('NCR Delhi'))

    # Close modal result
    browser.element('#closeLargeModal').click()
    browser.element('.modal-dialog').should(be.absent)
    browser.element('#firstName').should(be.blank)