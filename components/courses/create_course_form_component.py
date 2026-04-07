from components.base_component import BaseComponent
from playwright.sync_api import Page

from elements.input import Input
from elements.textarea import Textarea
import allure


class CreateCourseFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title_input = Input(page, 'create-course-form-title-input', 'Title')
        self.estimated_time_input = Input(
            page, 'create-course-form-estimated-time-input', 'Estimated time')

        self.description_textarea = Textarea(page, 'create-course-form-description-input', 'Description')

        self.max_score_input = Input(page, 'create-course-form-max-score-input', 'Max score')
        self.min_score_input = Input(page, 'create-course-form-min-score-input', 'Min score')

    @allure.step('Check visible create course form at index "{index}"')
    def check_visible(
        self,
        index: int,
        title: str,
        estimated_time: str,
        description: str,
        max_score: str,
        min_score: str
    ):
        self.title_input.check_visible(nth=index)
        self.title_input.check_have_value(title, nth=index)

        self.estimated_time_input.check_visible(nth=index)
        self.estimated_time_input.check_have_value(estimated_time, nth=index)

        self.description_textarea.check_visible(nth=index)
        self.description_textarea.check_have_value(description, nth=index)

        self.max_score_input.check_visible(nth=index)
        self.max_score_input.check_have_value(max_score, nth=index)

        self.min_score_input.check_visible(nth=index)
        self.min_score_input.check_have_value(min_score, nth=index)

    @allure.step('Fill create course form at index "{index}"')
    def fill(
        self,
        index: int,
        title: str,
        estimated_time: str,
        description: str,
        max_score: str,
        min_score: str
    ):
        self.title_input.fill(title, index=index)
        self.title_input.check_have_value(title, index=index)

        self.estimated_time_input.fill(estimated_time, index=index)
        self.estimated_time_input.check_have_value(estimated_time, index=index)

        self.description_textarea.fill(description, index=index)
        self.description_textarea.check_have_value(description, index=index)

        self.max_score_input.fill(max_score, index=index)
        self.max_score_input.check_have_value(max_score, index=index)

        self.min_score_input.fill(min_score, index=index)
        self.min_score_input.check_have_value(min_score, index=index)