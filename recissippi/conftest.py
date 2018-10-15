# Fixtures ?????????????????

def pytest_addoption(parser):
    parser.addoption("--day_of_the_week", action="store", default=1)
    parser.addoption("--expected_value",  action="store", default="tuesday")
	


def pytest_generate_tests(metafunc):
    # This is called for every test. Only get/set command line arguments
    # if the argument is specified in the list of test "fixturenames".
    option_value = metafunc.config.option.day_of_the_week
    if 'day_of_the_week' in metafunc.fixturenames and option_value is not None:
        metafunc.parametrize("day_of_the_week", [option_value])
    #
    option_value = metafunc.config.option.expected_value
    if 'expected_value' in metafunc.fixturenames and option_value is not None:
        metafunc.parametrize("expected_value", [option_value])