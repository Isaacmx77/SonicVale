
from dataclasses import dataclass
from datetime import datetime
from typing import Optional



@dataclass
class LLMProviderEntity:
    """业务实体：LLM"""
    name: str
    id: Optional[int] = None
    api_base_url : Optional[str] = None
    api_key: Optional[str] = None
    model_list : Optional[str] = None
    status : Optional[int] = None
    updated_at: Optional[datetime] = None
    created_at: Optional[datetime] = None
