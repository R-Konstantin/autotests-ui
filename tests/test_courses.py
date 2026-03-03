from playwright.sync_api import expect, Page, Playwright
import pytest


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state: Page):

        chromium_page_with_state.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

        header_courses = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
        expect(header_courses).to_be_visible()
        expect(header_courses).to_have_text('Courses')

        block_there_is_no_results = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
        expect(block_there_is_no_results).to_be_visible()
        expect(block_there_is_no_results).to_have_text('There is no results')

        icon_block = chromium_page_with_state.get_by_test_id('courses-list-empty-view-icon')
        expect(icon_block).to_be_visible()

        block_results_from_the_load_test = chromium_page_with_state.get_by_test_id('courses-list-empty-view-description-text')
        expect(block_results_from_the_load_test).to_be_visible()
        expect(block_results_from_the_load_test).to_have_text('Results from the load test pipeline will be displayed here')