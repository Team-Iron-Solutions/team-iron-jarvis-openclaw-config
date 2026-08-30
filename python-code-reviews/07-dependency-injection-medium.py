"""
Review 07: Dependency Injection vs Globals (Medium)
Scenario: Testability and decoupling
"""

from typing import Protocol, Optional

# ANTI-PATTERN: Global database connection
_db_connection = None

class UserRepositoryGlobal:
    """
    PROBLEMATIC: Uses global database connection
    - Hard to test (can't inject test DB)
    - Can't run tests in parallel
    - Tight coupling to specific DB
    """
    def get_user(self, user_id: int) -> dict:
        result = _db_connection.query(f"SELECT * FROM users WHERE id = {user_id}")
        return result

class DatabaseInterface(Protocol):
    """Interface for any database implementation"""
    def query(self, sql: str) -> list:
        ...

class UserRepositoryInjected:
    """
    IMPROVED: Accepts DB as constructor argument
    - Testable (can inject mock DB)
    - Can run parallel tests with different DBs
    - Loosely coupled
    """
    def __init__(self, db: DatabaseInterface):
        self.db = db
    
    def get_user(self, user_id: int) -> dict:
        result = self.db.query(f"SELECT * FROM users WHERE id = {user_id}")
        return result

class UserRepositoryWithDependencies:
    """
    BEST: All dependencies injected
    - Fully testable
    - Can mock logger, cache, auth
    - Single Responsibility
    """
    def __init__(
        self,
        db: DatabaseInterface,
        logger: Optional[object] = None,
        cache: Optional[object] = None,
        auth: Optional[object] = None
    ):
        self.db = db
        self.logger = logger
        self.cache = cache
        self.auth = auth
    
    def get_user(self, user_id: int, require_auth: bool = False) -> dict:
        if require_auth and self.auth:
            self.auth.verify_token()
        
        if self.cache and self.cache.has(f'user_{user_id}'):
            return self.cache.get(f'user_{user_id}')
        
        result = self.db.query(f"SELECT * FROM users WHERE id = {user_id}")
        
        if self.cache:
            self.cache.set(f'user_{user_id}', result)
        
        if self.logger:
            self.logger.info(f"Fetched user {user_id}")
        
        return result


# Test Example
class MockDatabase:
    def query(self, sql: str) -> list:
        return [{'id': 1, 'name': 'Test User'}]

def test_user_repository():
    """Example: Can test without real DB"""
    mock_db = MockDatabase()
    repo = UserRepositoryInjected(mock_db)
    user = repo.get_user(1)
    assert user['name'] == 'Test User'


# Issues:
# 1. UserRepositoryGlobal depends on global state (untestable)
# 2. Can't run tests in parallel
# 3. Hard to swap implementations
# Recommendation: Use constructor injection, protocol interfaces
