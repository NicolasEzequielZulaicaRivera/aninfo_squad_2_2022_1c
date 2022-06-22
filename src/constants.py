import datetime
import os

TESTING = int(os.environ.get("TESTING", False))
API_VERSION_PREFIX = "/api/v1"
# FIXME: we should mock the date in gherkin using Background:
TODAY_DATE = datetime.date(2020, 1, 1)
