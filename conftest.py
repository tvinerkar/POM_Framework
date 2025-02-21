import os
import pytest
import sys
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from _pytest.runner import TestReport  # Import for type hinting

def pytest_addoption(parser):
    """Command-line option to select the browser."""
    parser.addoption("--browser", action="store", default="chrome", help="Choose browser: chrome, firefox, edge")

@pytest.fixture(scope="class")
def driver(request):
    """Fixture to initialize WebDriver based on selected browser."""
    browser = request.config.getoption("--browser")

    if browser == "chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    elif browser == "edge":
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    else:
        raise ValueError("Unsupported browser! Choose from chrome, firefox, or edge.")

    driver.maximize_window()
    driver.implicitly_wait(10)
    request.cls.driver = driver
    yield driver
    driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook to capture screenshots on test failure and attach them to the HTML report."""
    outcome = yield
    report: TestReport = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver", None)  # Get WebDriver instance
        if driver:
            test_name = item.nodeid.replace("::", "_").replace("/", "_").replace("\\", "_")
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

            # Ensure the screenshot directory exists
            screenshot_dir = os.path.join(os.getcwd(), "report", "screenshots")
            os.makedirs(screenshot_dir, exist_ok=True)

            # Save screenshot
            screenshot_path = os.path.join(screenshot_dir, f"{test_name}_{timestamp}.png")
            driver.save_screenshot(screenshot_path)
            print(f"📸 Screenshot saved on failure: {screenshot_path}")

            # Attach screenshot to HTML report
            extra = getattr(report, "extra", [])
            if "pytest_html" in item.config.pluginmanager.list_name_plugin():
                from pytest_html import extras
                extra.append(extras.image(screenshot_path))
                report.extra = extra
