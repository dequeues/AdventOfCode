import sys

from loguru import logger

_ = logger.add(
    sys.stderr,
    format="{time} {level} {message}",
    filter="my_module",
    level="INFO",
)

__all__ = ["logger"]
