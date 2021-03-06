import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language")


@pytest.fixture(scope="function")
def browser(request):
    browser_lang = request.config.getoption("language")
    browser = None
    if browser_lang:
        print(f"\nstart browser for {browser_lang} language..")
        options = Options()
        options.add_experimental_option(
        'prefs', {'intl.accept_languages': browser_lang}
        )
        browser = webdriver.Chrome(options=options)
    else:
        raise pytest.UsageError("Pleace enter --language")
    yield browser
    print("\nquit browser..")
    browser.quit()
