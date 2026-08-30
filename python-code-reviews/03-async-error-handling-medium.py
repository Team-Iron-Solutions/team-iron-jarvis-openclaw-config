"""
Review 03: Async Error Handling (Medium)
Scenario: Concurrent tasks with improper error handling
"""

import asyncio
from typing import List, Optional

class APIClient:
    async def fetch_user(self, user_id: int) -> dict:
        """Simulated API call"""
        await asyncio.sleep(0.1)
        return {"id": user_id, "name": f"User {user_id}"}
    
    async def fetch_orders(self, user_id: int) -> List[dict]:
        """Simulated API call"""
        await asyncio.sleep(0.2)
        return [{"order_id": i, "user_id": user_id} for i in range(3)]

class DataFetcher:
    def __init__(self, client: APIClient):
        self.client = client
    
    async def get_user_with_orders_unsafe(self, user_id: int):
        """
        PROBLEMATIC: Fire-and-forget without error handling
        - If fetch_orders fails, exception is lost
        - No retry mechanism
        - Task cancellation not properly handled
        """
        user_task = asyncio.create_task(self.client.fetch_user(user_id))
        orders_task = asyncio.create_task(self.client.fetch_orders(user_id))
        
        user = await user_task
        orders = await orders_task
        
        return {"user": user, "orders": orders}
    
    async def get_user_with_orders_safe(self, user_id: int, timeout: float = 5.0):
        """
        IMPROVED: Proper error handling with timeout
        """
        try:
            user_task = asyncio.create_task(self.client.fetch_user(user_id))
            orders_task = asyncio.create_task(self.client.fetch_orders(user_id))
            
            user = await asyncio.wait_for(user_task, timeout=timeout)
            orders = await asyncio.wait_for(orders_task, timeout=timeout)
            
            return {"user": user, "orders": orders}
        
        except asyncio.TimeoutError:
            print(f"Timeout fetching data for user {user_id}")
            raise
        except Exception as e:
            print(f"Error fetching user data: {e}")
            # Cleanup
            user_task.cancel() if 'user_task' in locals() else None
            orders_task.cancel() if 'orders_task' in locals() else None
            raise
    
    async def fetch_multiple_users_batch(self, user_ids: List[int]):
        """
        IMPROVED: Gather with exception handling
        """
        tasks = [self.client.fetch_user(uid) for uid in user_ids]
        results = await asyncio.gather(*tasks, return_exceptions=True)
        
        # Filter valid results
        users = [r for r in results if not isinstance(r, Exception)]
        errors = [r for r in results if isinstance(r, Exception)]
        
        if errors:
            print(f"Errors fetching {len(errors)} users")
        
        return users


# Issues:
# 1. get_user_with_orders_unsafe() doesn't handle exceptions
# 2. No timeout protection for hung tasks
# 3. Task cancellation not managed
# Recommendation: Use try/except, asyncio.gather(), timeout handling
