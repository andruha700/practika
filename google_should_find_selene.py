from selene import browser, be, have

browser.config.driver_name = "edge"
browser.open('https://google.com')
browser.element('[name="q"]').should(be.blank).type('qa.guru').press_enter()
browser.element('html').should(have.text('About this page'))

# browser.element('[id="search"]').should(have.text('QA.GURU: Курсы тестировщиков'))g