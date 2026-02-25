from playwright.sync_api import sync_playwright, expect


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()


    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.fill('user.name@gmail.com')

    username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    username_input.fill('username')

    password_input = page.locator('//div[@data-testid="registration-form-password-input"]//div//input') #Для разнообразия использую XPATH (В целях повторить материал)
    password_input.fill('password')

    button_registration = page.get_by_test_id('registration-page-registration-button')
    button_registration.click()


    context.storage_state(path='browser-state.json')

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state='browser-state.json')
    page = context.new_page()

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

    header_courses = page.get_by_test_id('courses-list-toolbar-title-text')
    expect(header_courses).to_be_visible()
    expect(header_courses).to_have_text('Courses')

    block_there_is_no_results = page.get_by_test_id('courses-list-empty-view-title-text')
    expect(block_there_is_no_results).to_be_visible()
    expect(block_there_is_no_results).to_have_text('There is no results')

    icon_block = page.get_by_test_id('courses-list-empty-view-icon')
    expect(icon_block).to_be_visible()

    block_results_from_the_load_test = page.get_by_test_id('courses-list-empty-view-description-text')
    expect(block_results_from_the_load_test).to_be_visible()
    expect(block_results_from_the_load_test).to_have_text('Results from the load test pipeline will be displayed here')

    page.wait_for_timeout(5000)


