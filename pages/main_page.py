from selene import browser, have


class MainPage:

    def open(self):
        browser.open('https://github.com/')

    def should_button_product_by_desktop(self):
        browser.element('(//*[contains(text(),"Product")])[1]').should(have.exact_text('Product'))

    def should_button_product_by_mobile(self):
        # browser.driver.set_window_size('800','600')
        browser.element('[class="Button-content"]').click()
        browser.element('(//*[contains(text(),"Product")])[1]').should(have.exact_text('Product'))
