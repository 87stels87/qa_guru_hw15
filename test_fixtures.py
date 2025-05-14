"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""
from pages.main_page import MainPage


def test_github_desktop(desktop_screen):
    main_page = MainPage()
    main_page.open()
    main_page.should_button_product_by_desktop()


def test_github_mobile(mobile_screen):
    main_page = MainPage()
    main_page.open()
    main_page.should_button_product_by_mobile()