"""
Review 06: Type Hints & Input Validation (Medium)
Scenario: Type safety and runtime validation
"""

from typing import Union, List, Optional, Dict, Any
from dataclasses import dataclass

class UserService:
    def get_user_unsafe(self, user_id):
        """
        UNSAFE: No type hints, no validation
        - user_id could be anything: string, list, None
        - No return type specification
        - Hard to understand contract
        """
        result = {}
        result['id'] = user_id
        result['name'] = 'John'
        return result
    
    def get_user_safe(self, user_id: int) -> Dict[str, Union[int, str]]:
        """
        IMPROVED: Type hints specify contract
        - Input: user_id must be int
        - Output: dict with str keys, int|str values
        - IDE can validate before runtime
        """
        if not isinstance(user_id, int):
            raise ValueError(f"user_id must be int, got {type(user_id)}")
        if user_id < 0:
            raise ValueError(f"user_id must be positive")
        
        return {'id': user_id, 'name': 'John'}
    
    def create_user_unvalidated(self, name: str, email: str, age: int) -> dict:
        """
        WEAK: Type hints but no validation
        - name could be empty string
        - email could be invalid format
        - age could be negative
        """
        return {'name': name, 'email': email, 'age': age}
    
    def create_user_validated(self, name: str, email: str, age: int) -> Dict[str, Any]:
        """
        IMPROVED: Type hints + validation
        """
        if not name or len(name) < 2:
            raise ValueError("name must be at least 2 characters")
        if '@' not in email or '.' not in email:
            raise ValueError("invalid email format")
        if age < 0 or age > 150:
            raise ValueError("age must be between 0 and 150")
        
        return {'name': name, 'email': email, 'age': age}

@dataclass
class User:
    """
    BEST: Dataclass with validation
    - Type hints embedded in class definition
    - IDE autocomplete works
    - Serialization/deserialization support
    """
    id: int
    name: str
    email: str
    age: int
    
    def __post_init__(self):
        """Validate after initialization"""
        if self.age < 0 or self.age > 150:
            raise ValueError("Invalid age")
        if '@' not in self.email:
            raise ValueError("Invalid email")


# Issues:
# 1. get_user_unsafe() has no type safety
# 2. create_user_unvalidated() doesn't validate input
# 3. No use of pydantic or dataclasses for complex objects
# Recommendation: Use type hints, dataclasses, pydantic validators
