import pytest
from selene import browser


@pytest.fixture()
def desktop_screen():
    browser.config.window_width = 1600
    browser.config.window_height = 900
    yield
    browser.quit()


@pytest.fixture()
def mobile_screen():
    browser.config.window_width = 400
    browser.config.window_height = 300
    yield
    browser.quit()


@pytest.fixture(scope='function', params=[(2500, 1000), (1920, 1080), (1600, 900), (1600, 1000), (400, 300)])
def setup_browser(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height
    if width > 500:
        yield "desktop"
    else:
        yield "mobile"
    browser.quit()


desktop = pytest.mark.parametrize('setup_browser', [(1920, 1080)], indirect=True)
mobile = pytest.mark.parametrize('setup_browser', [(400, 300)], indirect=True)