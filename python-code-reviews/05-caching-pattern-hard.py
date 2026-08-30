"""
Review 05: Caching & Memoization (Hard)
Scenario: Expensive computation without proper caching
"""

from functools import lru_cache
from typing import Dict, Optional
import time

class RecommendationEngine:
    def __init__(self):
        self.cache = {}
        self.call_count = 0
    
    def compute_user_recommendations_naive(self, user_id: int, product_limit: int = 10) -> list:
        """
        INEFFICIENT: No caching, recalculates for every request
        - For 1000 requests same user: 1000 full calculations
        - ~5 seconds per calculation
        - Total: 5000 seconds wasted
        """
        self.call_count += 1
        
        # Simulated expensive ML operation
        time.sleep(5)
        
        # Return recommendations
        return [f"product_{i}" for i in range(product_limit)]
    
    def compute_user_recommendations_cached(self, user_id: int, product_limit: int = 10) -> list:
        """
        IMPROVED: Manual cache with TTL considerations
        """
        cache_key = (user_id, product_limit)
        
        if cache_key in self.cache:
            return self.cache[cache_key]
        
        self.call_count += 1
        time.sleep(5)
        
        result = [f"product_{i}" for i in range(product_limit)]
        self.cache[cache_key] = result
        
        return result
    
    @lru_cache(maxsize=1000)
    def compute_user_recommendations_decorator(self, user_id: int, product_limit: int = 10) -> tuple:
        """
        BEST: Using lru_cache decorator
        - Automatic cache management
        - Thread-safe
        - Clear semantics
        """
        self.call_count += 1
        time.sleep(5)
        
        return tuple(f"product_{i}" for i in range(product_limit))
    
    def compute_similar_users_without_cache(self, user_id: int) -> list:
        """
        INEFFICIENT: No caching for graph-like computations
        - user A -> user B, user C (3 comparisons)
        - user B -> user A, user C (3 comparisons, duplicated!)
        - Total redundant work
        """
        similar = []
        for other_id in range(1, 100):
            if self._similarity_score(user_id, other_id) > 0.8:
                similar.append(other_id)
        return similar
    
    @lru_cache(maxsize=10000)
    def _similarity_score(self, user_a: int, user_b: int) -> float:
        """
        IMPROVED: Cache similarity calculations
        - _similarity_score(1,2) cached once
        - Reused across all calls
        """
        time.sleep(0.1)  # Simulated computation
        return (user_a + user_b) % 10 / 10


# Issues:
# 1. compute_user_recommendations_naive() recalculates unnecessarily
# 2. No cache invalidation strategy
# 3. Missing cache key design for similar products
# Recommendation: Use @lru_cache, implement cache TTL, consider Redis
