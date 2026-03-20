import logging


def sanitize_secret(value: str | None) -> str:
    if not value:
        return ""
    if value.startswith("sk-"):
        return "sk-*****"
    return "*****"


def build_logger() -> logging.Logger:
    logger = logging.getLogger("whisky")
    if logger.handlers:
        return logger
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler()
    formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger
