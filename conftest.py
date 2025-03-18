import os

import allure
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
import pytest
from _pytest.reports import TestReport

def pytest_addoption(parser):
    """Command-line option to select browsers for parallel execution."""
    parser.addoption("--browser", action="store", default="chrome", help="Choose browser: chrome, firefox, edge")

@pytest.fixture(params=["chrome"], scope="class")
#@pytest.fixture(params=["chrome", "firefox", "edge"], scope="class")
def driver(request):
    """Fixture to initialize WebDriver based on selected browser."""
    browser = request.param

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
    elif browser == "edge":
        options = webdriver.EdgeOptions()
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=options)
    else:
        raise ValueError("Unsupported browser! Choose from chrome, firefox, or edge.")



    # Fetch browser version
    browser_version = driver.capabilities["browserVersion"]

    driver.maximize_window()
    driver.implicitly_wait(10)

    request.cls.driver = driver
    request.cls.browser_name = browser
    request.cls.browser_version = browser_version  # Store for screenshot naming

    # Generate timestamped folder names
    timestamp = datetime.now().strftime("%Y%m%d")
    parent_folder = os.path.join(os.getcwd(), "report", f"test_guest_checkout_{timestamp}")
    report_folder = os.path.join(parent_folder, f"test_guest_checkout_{timestamp}_report")
    screenshot_folder = os.path.join(parent_folder, f"test_guest_checkout_{timestamp}_Screenshots")
    failed_folder = os.path.join(parent_folder, f"TestGuestCheckout_{timestamp}_09_failed")

    # Create necessary directories
    os.makedirs(report_folder, exist_ok=True)
    os.makedirs(screenshot_folder, exist_ok=True)
    os.makedirs(failed_folder, exist_ok=True)

    # Store folders in request object for later access
    request.cls.parent_folder = parent_folder
    request.cls.report_folder = report_folder
    request.cls.screenshot_folder = screenshot_folder
    request.cls.failed_folder = failed_folder

    yield driver
    driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Capture screenshots on test failure and attach them to the HTML report."""
    outcome = yield
    report: TestReport = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver", None)
        if driver:
            test_name = item.nodeid.split("::")[-2] if len(item.nodeid.split("::")) > 1 else "UnknownTest"
            step_name = item.nodeid.split("::")[-1].replace("test_", "").replace("_", " ").capitalize()
            timestamp = datetime.now().strftime("%Y%m%d_%H%M")
            browser = item.funcargs["request"].cls.browser_name
            version = item.funcargs["request"].cls.browser_version

            # Save screenshot in the failed folder
            failed_screenshot_path = os.path.join(item.funcargs["request"].cls.failed_folder, f"{test_name}_{step_name}_{timestamp}_{browser}_version_{version}.png")
            driver.save_screenshot(failed_screenshot_path)
            print(f"📸 Failed screenshot saved: {failed_screenshot_path}")

            # Attach screenshot to HTML report
            extra = getattr(report, "extra", [])
            if "pytest_html" in item.config.pluginmanager.list_name_plugin():
                from pytest_html import extras
                extra.append(extras.image(failed_screenshot_path))
                report.extra = extra

# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_teardown(item, nextitem):
#     """Save screenshots of successful test cases in the screenshots folder."""
#     outcome = yield
#     report: TestReport = outcome.get_result()
#
#     if report.when == "call" and report.passed:
#         driver = item.funcargs.get("driver", None)
#         if driver:
#             test_name = item.nodeid.split("::")[-2] if len(item.nodeid.split("::")) > 1 else "UnknownTest"
#             step_name = item.nodeid.split("::")[-1].replace("test_", "").replace("_", " ").capitalize()
#             timestamp = datetime.now().strftime("%Y%m%d_%H%M")
#             browser = item.funcargs["request"].cls.browser_name
#             version = item.funcargs["request"].cls.browser_version
#
#             # Save screenshot in the Screenshots folder
#             screenshot_path = os.path.join(item.funcargs["request"].cls.screenshot_folder, f"{test_name}_{step_name}_{browser}_{version}_{timestamp}.png")
#             driver.save_screenshot(screenshot_path)
#             print(f"📸 Passed screenshot saved: {screenshot_path}")

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_teardown(item):
    """Save screenshots of successful test cases in the screenshots folder."""
    outcome = yield
    reports = outcome.get_result()

    # Ensure reports is always iterable (list or single object)
    if not isinstance(reports, list):
        reports = [reports]

    for report in reports:
        if report.when == "call" and report.passed:
            test_name = item.nodeid.split("::")[-2] if len(item.nodeid.split("::")) > 1 else "UnknownTest"
            step_name = item.nodeid.split("::")[-1].replace("test_", "").replace("_", " ").capitalize()
            timestamp = datetime.now().strftime("%Y%m%d_%H%M")
            browser = item.funcargs["request"].cls.browser_name
            version = item.funcargs["request"].cls.browser_version
            screenshot_filename = f"{test_name}_{step_name}_{browser}_{timestamp}.png"
            screenshot_path = os.path.join(item.funcargs["request"].cls.screenshot_folder,screenshot_filename+".png")
            driver.save_screenshot(screenshot_path)
            print(f"📸 Passed screenshot saved: {screenshot_path}")

            # Take Screenshot
            item.cls.driver.save_screenshot(screenshot_path)
            allure.attach.file(screenshot_path, name=test_name, attachment_type=allure.attachment_type.PNG)

def pytest_configure(config):
    """Generate timestamped test report automatically in the report folder."""
    timestamp = datetime.now().strftime("%Y%m%d_%H")
    parent_folder = os.path.join(os.getcwd(), "report", f"test_report_{timestamp}")
    report_folder = os.path.join(parent_folder, f"test_report_{timestamp}_report")

    # Ensure report directory exists
    os.makedirs(report_folder, exist_ok=True)

    report_file = os.path.join(report_folder, f"test_report_{timestamp}.html")
    config.option.htmlpath = report_file  # Set report path dynamically
