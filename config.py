import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

    APP_ID = int(os.environ.get("APP_ID", 11750778))

    API_HASH = os.environ.get("API_HASH", "d0352df3ddb5e00bcf16b55dae071b52")
