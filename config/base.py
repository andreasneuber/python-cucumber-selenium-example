from dataclasses import dataclass, field
from typing import Dict


@dataclass(frozen=True)
class Config:
    # App settings
    URL: str = "http://localhost:8000/index.php"
    BROWSER: str = "chrome"  # Options: 'chrome', 'firefox'

    # Selenium timeouts (in seconds)
    ELEMENT_FETCH_TIMEOUT: int = 30
    IMPLICIT_TIMEOUT: int = 15

    # Selenium Grid support
    USE_GRID: bool = False
    SELENIUM_GRID_IP: str = "127.0.0.1"
    SELENIUM_GRID_PORT: int = 4444

    # Logging config
    NUMBER_OF_DAYS_TO_KEEP_LOG_FILES: int = 7

    # Sensitive credentials (consider loading from .env in production)
    CREDENTIALS: Dict[str, str] = field(default_factory=lambda: {
        "username": "admin",
        "password": "1234"
    })
