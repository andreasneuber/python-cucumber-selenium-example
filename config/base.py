class Config:
    URL = "http://localhost:8000/index.php"

    CREDENTIALS = {"username": "admin", "password": "1234"}
    BROWSER = {"name": "chrome", "version": "111.0"}

    ELEMENT_FETCH_TIMEOUT = 30
    IMPLICIT_TIMEOUT = 15

    USE_GRID = False
    SELENIUM_GRID_IP = "127.0.0.1"
    SELENIUM_GRID_PORT = 4444

    NUMBER_OF_DAYS_TO_KEEP_LOG_FILES: 7
