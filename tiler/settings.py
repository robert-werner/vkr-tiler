from typing import Any

from decouple import config, UndefinedValueError


class Settings(object):  # noqa: WPS230
    """Class with server settings."""

    def __init__(self) -> None:
        """Create class with server settings."""
        self.redis_host = self.get_setting("REDIS_HOST", "localhost")
        self.redis_port = self.get_setting("REDIS_PORT", "6379")

    def get_setting(self, name: str, default: Any) -> Any:
        """Get setting.

        :param name: Setting name
        :param default: Default value
        :return: Setting value
        """
        setting = None
        try:
            setting = config(name)
        except UndefinedValueError:
            setting = default

        return setting


settings = Settings()
