"""
Переопределите параметр с помощью indirect параметризации на уровне теста
"""

from conftest import desktop, mobile
from pages.main_page import MainPage


@desktop
def test_github_desktop(setup_browser):
    main_page = MainPage()
    main_page.open()
    main_page.should_button_product_by_desktop()


@mobile
def test_github_mobile(setup_browser):
    main_page = MainPage()
    main_page.open()
    main_page.should_button_product_by_mobile()