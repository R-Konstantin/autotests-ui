from playwright.sync_api import sync_playwright, expect


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.fill('user.name@gmail.com')

    username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    username_input.fill('username')

    password_input = page.locator('//div[@data-testid="registration-form-password-input"]//div//input') #Для разнообразия использую XPATH (В целях повторить материал)
    password_input.fill('password')

    button_registration = page.locator('button')
    button_registration.click()

    header_dashboard = page.get_by_test_id('dashboard-toolbar-title-text')
    expect(header_dashboard).to_be_visible()


