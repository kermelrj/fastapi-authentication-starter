import logging, sys, json
from .config import settings

class JsonFormatter(logging.Formatter):

    def format(self, record: logging.LogRecord) -> str:
        log_record = {
            "level": record.levelname,
            "time": self.formatTime(record, self.datefmt),
            "message": record.getMessage(),
            "module": record.module,
            "line": record.lineno,
        }
        if record.exc_info:
            log_record["exc_info"] = self.formatException(record.exc_info)
        return json.dumps(log_record)