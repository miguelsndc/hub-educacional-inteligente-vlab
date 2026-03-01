from enum import Enum

class AIProvider(str, Enum):
    GEMINI = "gemini"
    ANTHROPIC = "anthropic"
    MOCK = "mock"

PAGINATION_DEFAULT_LIMIT = 10
PAGINATION_MAX_LIMIT = 100
RESOURCE_TYPES = ["video", "pdf", "link"]
AI_TAGS_COUNT = 3
AI_DEFAULT_PROVIDER = AIProvider.GEMINI
AI_DEFAULT_TIMEOUT = 30  # segundos
