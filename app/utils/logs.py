from typing import Union
from google.cloud import logging
import datetime, json

class Logs:
    def __init__(self, logger_name) -> None:
        self.logging_client = logging.Client()
        self.logger = self.logging_client.logger(logger_name)

    def _log(self, content:Union[str, dict], severity="INFO")->None:
        print(severity, datetime.datetime.now().isoformat(), json.dumps(content) if content is dict else str(content))
        if content is dict:
            self.logger.log_struct(content, severity=severity)
        else:
            self.logger.log_text(str(content), severity=severity)        

    def debug(self, content)->None:
        self._log(content, "DEBUG")
    
    def info(self, content)->None:
        self._log(content, "INFO")

    def warn(self, content)->None:
        self._log(content, "WARN")

    def error(self, content)->None:
        self._log(content, "ERROR")


logs = Logs("fast_api")


if __name__=="__main__":
    logs.info("hello, world!")