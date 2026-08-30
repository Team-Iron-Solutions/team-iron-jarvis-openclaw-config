"""
Review 10: Testing Patterns (Hard)
Scenario: Unit tests, integration tests, fixtures
"""

import unittest
from typing import List, Optional

class UserRepository:
    def __init__(self, db):
        self.db = db
    
    def get_user(self, user_id: int):
        return self.db.query(f"SELECT * FROM users WHERE id = {user_id}")
    
    def create_user(self, name: str, email: str):
        return self.db.execute(f"INSERT INTO users (name, email) VALUES ('{name}', '{email}')")

class TestUserRepositoryBad(unittest.TestCase):
    """PROBLEMATIC: Tests without proper setup/teardown, no isolation"""
    
    def test_get_user(self):
        """BAD: Depends on real database"""
        repo = UserRepository(db=RealDatabaseConnection())  # Real DB!
        user = repo.get_user(1)
        self.assertIsNotNone(user)
        # What if user 1 doesn't exist? Test becomes flaky
    
    def test_create_user(self):
        """BAD: No cleanup, pollutes database"""
        repo = UserRepository(db=RealDatabaseConnection())
        repo.create_user('John', 'john@example.com')
        # Database now has test data, test is not repeatable
    
    def test_multiple_users(self):
        \"\"\"BAD: Multiple assertions in single test, poor failure isolation\"\"\"
        repo = UserRepository(db=RealDatabaseConnection())
        user1 = repo.get_user(1)
        user2 = repo.get_user(2)
        user3 = repo.get_user(3)
        self.assertIsNotNone(user1)
        self.assertIsNotNone(user2)
        self.assertIsNotNone(user3)
        # If user2 fails, user3 assertion never runs

class MockDatabase:
    \"\"\"Mock for testing\"\"\"\n    def __init__(self):\n        self.data = {}\n    \n    def query(self, sql: str):\n        # Parse user_id from SQL and return mock data\n        return {'id': 1, 'name': 'Mock User'}\n    \n    def execute(self, sql: str):\n        return True

class TestUserRepositoryGood(unittest.TestCase):\n    \"\"\"IMPROVED: Proper isolation, mocking, fixtures\"\"\"\n    \n    def setUp(self):\n        \"\"\"GOOD: Setup runs before each test\"\"\"\n        self.mock_db = MockDatabase()\n        self.repo = UserRepository(db=self.mock_db)\n    \n    def tearDown(self):\n        \"\"\"GOOD: Cleanup after each test\"\"\"\n        self.mock_db = None\n        self.repo = None\n    \n    def test_get_user_returns_dict(self):\n        \"\"\"GOOD: Single assertion, single responsibility\"\"\"\n        user = self.repo.get_user(1)\n        self.assertIsInstance(user, dict)\n    \n    def test_get_user_has_required_fields(self):\n        \"\"\"GOOD: Separate test for different concern\"\"\"\n        user = self.repo.get_user(1)\n        self.assertIn('id', user)\n        self.assertIn('name', user)\n    \n    def test_create_user_success(self):\n        \"\"\"GOOD: Tests happy path\"\"\"\n        result = self.repo.create_user('John', 'john@example.com')\n        self.assertTrue(result)\n    \n    def test_create_user_empty_name_raises_error(self):\n        \"\"\"GOOD: Tests error cases explicitly\"\"\"\n        with self.assertRaises(ValueError):\n            self.repo.create_user('', 'john@example.com')\n    \n    def test_create_user_invalid_email_raises_error(self):\n        \"\"\"GOOD: Tests error cases explicitly\"\"\"\n        with self.assertRaises(ValueError):\n            self.repo.create_user('John', 'invalid-email')\n\nclass TestUserRepositoryBest(unittest.TestCase):\n    \"\"\"BEST: Uses fixtures, parameterized tests, clear naming\"\"\"\n    \n    @classmethod\n    def setUpClass(cls):\n        \"\"\"GOOD: One-time setup for all tests\"\"\"\n        cls.mock_db = MockDatabase()\n    \n    def setUp(self):\n        \"\"\"GOOD: Setup for each test\"\"\"\n        self.repo = UserRepository(db=self.mock_db)\n    \n    def test_given_valid_user_id_when_get_user_then_returns_user(self):\n        \"\"\"GOOD: Descriptive test name (Given-When-Then)\"\"\"\n        # Given\n        user_id = 1\n        \n        # When\n        user = self.repo.get_user(user_id)\n        \n        # Then\n        self.assertIsNotNone(user)\n        self.assertEqual(user['id'], 1)\n\n# Issues:\n# 1. TestUserRepositoryBad uses real database (slow, flaky)\n# 2. No proper setUp/tearDown, tests interfere with each other\n# 3. Multiple assertions per test, poor failure diagnostics\n# 4. No error case testing\n# Recommendation: Use mocks, proper fixtures, Given-When-Then pattern, one assertion per test
