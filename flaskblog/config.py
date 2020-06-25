import os


class Config:
    SECRET_KEY = "1626051a8412bc440d63b0ba12f4bf65"
    SQLALCHEMY_DATABASE_URI = "sqlite:///site.db"  # move to env variable if sensitive information is contained
    MAIL_SERVER = "smtp.googlemail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("EMAIL_USER")
    MAIL_PASSWORD = os.environ.get("EMAIL_PASS")
