import logging
import re

import pytest


logger = logging.getLogger(__name__)
email_regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"


@pytest.mark.parametrize("email",
                         ["test@test.ru", "w@w.com", "123QWE@mmm.mmm", "invalid_mail.ru", ""])
def test_valid_emails(email):
    try:
        assert re.fullmatch(email_regex, email), "Email is not valid!"
        logger.info(f"PASSED with email: {email}")
    except AssertionError as err:
        logger.info(f"FAILED with email: {email}")
        raise err


@pytest.mark.parametrize("email", ["test@test.", "w@", "@tt", "valid@gmail.com"])
def test_invalid_emails(email):
    try:
        assert not re.fullmatch(email_regex, email), "Email is valid!"
        logger.info(f"PASSED with email: {email}")
    except AssertionError as err:
        logger.info(f"FAILED with email: {email}")
        raise err
