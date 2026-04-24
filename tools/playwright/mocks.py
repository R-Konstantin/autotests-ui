from playwright.sync_api import Page


def mock_static_resources(page: Page):
    page.route("**/*.{ico,png,jpg,mp3,woff2}", lambda route: route.abort())