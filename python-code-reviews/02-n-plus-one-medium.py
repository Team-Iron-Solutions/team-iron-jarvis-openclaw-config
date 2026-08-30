"""
Review 02: N+1 Query Optimization (Medium)
Scenario: Inefficient database query pattern
"""

class Order:
    def __init__(self, order_id, user_id, total):
        self.order_id = order_id
        self.user_id = user_id
        self.total = total

class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

class OrderService:
    def __init__(self, db):
        self.db = db
    
    def get_all_orders_with_user_info(self):
        """
        INEFFICIENT: N+1 Query Problem
        - Fetches all orders (1 query)
        - For each order, fetches user info (N queries)
        - Total: 1 + N queries
        """
        orders = self.db.query("SELECT * FROM orders")
        result = []
        
        for order in orders:
            user = self.db.query(f"SELECT * FROM users WHERE id = {order.user_id}")
            result.append({
                'order_id': order.order_id,
                'user_name': user.name,
                'total': order.total
            })
        
        return result
    
    def get_all_orders_with_user_info_optimized(self):
        """
        OPTIMIZED: Join in single query
        - Fetches orders + user info in 1 query
        """
        query = """
            SELECT o.order_id, o.total, u.name 
            FROM orders o 
            JOIN users u ON o.user_id = u.id
        """
        return self.db.query(query)
    
    def get_orders_by_user_batch(self, user_ids):
        """
        OPTIMIZED: Batch query with IN clause
        - Fetches orders with multiple users in 1 query
        """
        placeholders = ','.join('?' * len(user_ids))
        query = f"SELECT * FROM orders WHERE user_id IN ({placeholders})"
        return self.db.query(query, user_ids)


# Issues:
# 1. get_all_orders_with_user_info() has N+1 problem
# 2. Performance degrades with large order volumes
# Recommendation: Use JOIN or batch queries
