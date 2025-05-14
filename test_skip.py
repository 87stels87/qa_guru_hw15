"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""
import pytest

from pages.main_page import MainPage


def test_github_desktop(setup_browser):
    if setup_browser == "desktop":
        pytest.skip()
    main_page = MainPage()
    main_page.open()
    main_page.should_button_product_by_mobile()


def test_github_mobile(setup_browser):
    if setup_browser == "mobile":
        pytest.skip()
    main_page = MainPage()
    main_page.open()
    main_page.should_button_product_by_desktop()