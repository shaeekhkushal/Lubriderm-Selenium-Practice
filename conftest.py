import allure
import pytest


@pytest.fixture(autouse=True)
def attach_print_output(capfd):
    yield
    captured = capfd.readouterr()
    allure.attach(captured.out, name='Console Logs', attachment_type=allure.attachment_type.TEXT)


def pytest_runtest_logreport(report):
    if report.when == 'call':
        allure.attach(f"Outcome: {report.outcome}, Duration: {str(report.duration)}")
