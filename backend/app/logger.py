import logging
import sys
import json
from datetime import datetime, timezone

class StructuredFormatter(logging.Formatter):
    """
    Formata logs em um formato estruturado (JSON) com informações adicionais,
    como timestamp, nível de log, mensagem e logger.
    Os campos adicionais podem ser adicionados usando o prefixo "ctx_" nos atributos do LogRecord.
    Exemplo de uso:
        logger = get_logger("my_logger")
        logger.info("This is a log message", extra={"ctx_user_id": 123, "ctx_request_id": "abc"})
    O log resultante será um JSON contendo os campos "timestamp", "level", "message", "logger", "user_id" e "request_id". 
    Se houver uma exceção, ela será incluída no campo "exception".
    """
    def format(self, record: logging.LogRecord) -> str:
        log_entry = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "level": record.levelname,
            "message": record.getMessage(),
            "logger": record.name,
        }

        for key, value in record.__dict__.items():
            if key.startswith("ctx_"):
                log_entry[key[4:]] = value
                
        if record.exc_info:
            log_entry["exception"] = self.formatException(record.exc_info)
        
        return json.dumps(log_entry, ensure_ascii=False)
    
def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    
    if not logger.hasHandlers():
        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(StructuredFormatter())
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
        logger.propagate = False
        
    return logger