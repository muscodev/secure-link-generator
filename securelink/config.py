import os

__all__ = ["config"]


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "MySecret")  # Change in production
    API_KEY = os.getenv("API_KEY", "defaultkey")  # Change in production


config = Config()
