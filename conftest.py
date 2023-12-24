import allure


def pytest_runtest_logreport(report):
    if report.when == 'call':
        allure.attach(f"Outcome: {report.outcome}, Duration: {str(report.duration)}")

