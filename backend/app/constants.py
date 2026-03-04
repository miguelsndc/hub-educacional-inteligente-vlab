from enum import Enum
from dataclasses import dataclass


class AIProviderEnum(str, Enum):
    GEMINI = "gemini"
    ANTHROPIC = "anthropic"
    MOCK = "mock"


@dataclass(frozen=True)
class PaginationConfig:
    default_limit: int = 10
    max_limit: int = 100


class ResourceTypeEnum(str, Enum):
    VIDEO = "video"
    PDF = "pdf"
    LINK = "link"


@dataclass(frozen=True)
class AIConfig:
    tags_count: int = 3
    default_provider: AIProviderEnum = AIProviderEnum.GEMINI
    default_timeout: int = 30  # segundos
