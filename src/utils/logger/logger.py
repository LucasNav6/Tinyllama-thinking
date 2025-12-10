from loguru import logger

import sys

logger.remove(0)
logger.add(
    sys.stderr,
    format="<level>[{level}]</level> {time:YYYY-MM-DD HH:mm:ss}: {message}",
    colorize=True
)