import logging
import json_log_formatter

formatter = json_log_formatter.JSONFormatter()

# ! Deprecated code - Day 1
#json_handler = logging.StreamHandler()
#json_handler.setFormatter(formatter)

#logger = logging.getLogger("security-api")
#logger.setLevel(logging.INFO)
#logger.addHandler(json_handler)

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

file_handler = logging.FileHandler("app_logs.jsonl")
file_handler.setFormatter(formatter)

logger = logging.getLogger("security-api")
logger.setLevel(logging.INFO)
logger.addHandler(file_handler)
logger.addHandler(console_handler)