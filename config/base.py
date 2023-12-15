class Config:
    URL = "http://localhost:8000/index.php"

    BROWSER = "chrome"
    # BROWSER = "firefox"

    ELEMENT_FETCH_TIMEOUT = 30
    IMPLICIT_TIMEOUT = 15

    USE_GRID = False
    SELENIUM_GRID_IP = "127.0.0.1"
    SELENIUM_GRID_PORT = 4444

    NUMBER_OF_DAYS_TO_KEEP_LOG_FILES: 7

    CREDENTIALS = {"username": "admin", "password": "1234"}
