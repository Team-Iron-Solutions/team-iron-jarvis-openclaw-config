"""
Review 08: REST API Design (Very Hard)
Scenario: API endpoints and HTTP semantics
"""

from typing import Dict, List, Optional, Tuple
from enum import Enum

class HTTPStatus(Enum):
    OK = 200
    CREATED = 201
    BAD_REQUEST = 400
    NOT_FOUND = 404
    CONFLICT = 409
    INTERNAL_ERROR = 500

class APIEndpointsBad:
    """
    PROBLEMATIC: Poor REST design
    - Uses verbs in URLs instead of resources
    - Inconsistent status codes
    - No pagination
    """
    
    def getUserData(self, user_id: int) -> Tuple[int, Dict]:
        \"\"\"
        BAD: Verb in URL, no pagination
        GET /getUserData?id=123
        \"\"\"
        users = [{'id': i, 'name': f'User{i}'} for i in range(1000)]
        return 200, {'users': users}  # Returns all 1000!
    
    def createNewUser(self, data: Dict) -> Tuple[int, Dict]:
        \"\"\"
        BAD: Verb in URL, inconsistent response
        POST /createNewUser
        \"\"\"
        if not data.get('name'):
            return 500, {'error': 'name required'}  # Wrong status code!
        return 200, {'id': 1}  # Should be 201 CREATED
    
    def deleteUserRecord(self, user_id: int) -> Tuple[int, Dict]:
        \"\"\"
        BAD: Verb in URL, no safety checks
        POST /deleteUserRecord?id=123
        \"\"\"
        # What if user_id doesn't exist?
        return 200, {'status': 'deleted'}

class APIEndpointsGood:
    \"\"\"
    IMPROVED: Proper REST design
    - Resource-based URLs
    - Correct HTTP status codes
    - Pagination support
    \"\"\"
    
    def get_users(
        self,
        page: int = 1,
        page_size: int = 20,
        filters: Optional[Dict] = None
    ) -> Tuple[int, Dict]:
        \"\"\"
        GOOD: Resource URL, pagination
        GET /users?page=1&page_size=20&name=john
        \"\"\"
        total_users = 1000
        paginated = [{'id': i, 'name': f'User{i}'} for i in range((page-1)*page_size, page*page_size)]
        
        return 200, {
            'data': paginated,
            'pagination': {
                'page': page,
                'page_size': page_size,
                'total': total_users,
                'total_pages': (total_users + page_size - 1) // page_size
            }
        }
    
    def create_user(self, data: Dict) -> Tuple[int, Dict]:
        \"\"\"
        GOOD: Correct status codes and response
        POST /users
        \"\"\"
        if not data.get('name'):
            return 400, {'error': 'name required', 'code': 'MISSING_FIELD'}
        
        if not data.get('email'):
            return 400, {'error': 'email required', 'code': 'MISSING_FIELD'}
        
        user = {'id': 123, 'name': data['name'], 'email': data['email']}
        return 201, user  # 201 CREATED
    
    def get_user(self, user_id: int) -> Tuple[int, Dict]:
        \"\"\"
        GOOD: Single resource endpoint
        GET /users/123
        \"\"\"
        # Check if exists
        user = self._fetch_user(user_id)
        if not user:
            return 404, {'error': 'user not found', 'code': 'USER_NOT_FOUND'}
        
        return 200, user
    
    def delete_user(self, user_id: int) -> Tuple[int, Dict]:
        \"\"\"
        GOOD: Idempotent delete
        DELETE /users/123
        \"\"\"
        user = self._fetch_user(user_id)
        if not user:
            return 404, {'error': 'user not found', 'code': 'USER_NOT_FOUND'}
        
        self._delete_user(user_id)
        return 204, {}  # 204 No Content
    
    def _fetch_user(self, user_id: int) -> Optional[Dict]:
        # Simulated fetch
        return None
    
    def _delete_user(self, user_id: int):
        pass


# Issues:
# 1. getUserData() has verb in URL
# 2. createNewUser() returns wrong status code (500 instead of 400)
# 3. No pagination on bulk endpoints
# 4. Inconsistent error response format
# Recommendation: RESTful design, proper status codes, pagination
