# Graph Report - graph.json  (2026-08-30)

## Corpus Check
- cluster-only mode — file stats not available

## Summary
- 132 nodes · 133 edges · 10 communities
- Extraction: 100% EXTRACTED · 0% INFERRED · 0% AMBIGUOUS
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `62e73bff`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- 07-dependency-injection-medium.py
- UserService
- OrderService
- RecommendationEngine
- DataFetcher
- 08-api-design-very-hard.py
- UserRepository
- DataProcessor
- DatabaseQuery
- 09-ml-pipeline-very-hard.py

## God Nodes (most connected - your core abstractions)
1. `RecommendationEngine` - 7 edges
2. `UserRepository` - 7 edges
3. `DatabaseInterface` - 6 edges
4. `DataProcessor` - 6 edges
5. `DatabaseQuery` - 6 edges
6. `UserRepositoryInjected` - 5 edges
7. `UserService` - 5 edges
8. `OrderService` - 5 edges
9. `DataFetcher` - 5 edges
10. `TestUserRepositoryBad` - 5 edges

## Surprising Connections (you probably didn't know these)
- None detected - all connections are within the same source files.

## Import Cycles
- None detected.

## Communities (10 total, 0 thin omitted)

### Community 0 - "07-dependency-injection-medium.py"
Cohesion: 0.11
Nodes (13): DatabaseInterface, MockDatabase, Review 07: Dependency Injection vs Globals (Medium) Scenario: Testability and…, PROBLEMATIC: Uses global database connection - Hard to test (can't inject test…, Interface for any database implementation, IMPROVED: Accepts DB as constructor argument - Testable (can inject mock DB) -…, BEST: All dependencies injected - Fully testable - Can mock logger, cache, auth…, Example: Can test without real DB (+5 more)

### Community 1 - "UserService"
Cohesion: 0.12
Nodes (10): Review 06: Type Hints & Input Validation (Medium) Scenario: Type safety and…, UNSAFE: No type hints, no validation - user_id could be anything: string, list,…, IMPROVED: Type hints specify contract - Input: user_id must be int - Output:…, WEAK: Type hints but no validation - name could be empty string - email could…, IMPROVED: Type hints + validation, BEST: Dataclass with validation - Type hints embedded in class definition - IDE…, Validate after initialization, User (+2 more)

### Community 2 - "OrderService"
Cohesion: 0.14
Nodes (7): Order, OrderService, Review 02: N+1 Query Optimization (Medium) Scenario: Inefficient database query…, INEFFICIENT: N+1 Query Problem - Fetches all orders (1 query) - For each order,…, OPTIMIZED: Join in single query - Fetches orders + user info in 1 query, OPTIMIZED: Batch query with IN clause - Fetches orders with multiple users in 1…, User

### Community 3 - "RecommendationEngine"
Cohesion: 0.15
Nodes (7): Review 05: Caching & Memoization (Hard) Scenario: Expensive computation without…, INEFFICIENT: No caching, recalculates for every request - For 1000 requests…, IMPROVED: Manual cache with TTL considerations, BEST: Using lru_cache decorator - Automatic cache management - Thread-safe -…, INEFFICIENT: No caching for graph-like computations - user A -> user B, user C…, IMPROVED: Cache similarity calculations - _similarity_score(1,2) cached once -…, RecommendationEngine

### Community 4 - "DataFetcher"
Cohesion: 0.17
Nodes (6): APIClient, DataFetcher, Review 03: Async Error Handling (Medium) Scenario: Concurrent tasks with…, PROBLEMATIC: Fire-and-forget without error handling - If fetch_orders fails,…, IMPROVED: Proper error handling with timeout, IMPROVED: Gather with exception handling

### Community 5 - "08-api-design-very-hard.py"
Cohesion: 0.18
Nodes (7): APIEndpointsBad, delete_user(), _fetch_user(), HTTPStatus, Review 08: REST API Design (Very Hard) Scenario: API endpoints and HTTP…, PROBLEMATIC: Poor REST design - Uses verbs in URLs instead of resources -…, Enum

### Community 6 - "UserRepository"
Cohesion: 0.19
Nodes (6): Review 10: Testing Patterns (Hard) Scenario: Unit tests, integration tests,…, PROBLEMATIC: Tests without proper setup/teardown, no isolation, BAD: Depends on real database, BAD: No cleanup, pollutes database, TestUserRepositoryBad, UserRepository

### Community 7 - "DataProcessor"
Cohesion: 0.17
Nodes (6): DataProcessor, Review 04: Performance Bottleneck (Hard) Scenario: Memory inefficient data…, INEFFICIENT: Loads entire file into memory - For 1GB file: 1GB+ RAM usage - No…, EFFICIENT: Streaming with generator pattern - Constant memory usage regardless…, SLOW: Multiple passes, redundant calculations - O(n) for mean, O(n) for std…, FAST: Single pass with numpy - Vectorized operations - Compiled C code…

### Community 8 - "DatabaseQuery"
Cohesion: 0.18
Nodes (5): DatabaseQuery, Review 01: SQL Injection Detection (Easy) Scenario: Simple parameterized query…, VULNERABLE: String concatenation in SQL query, SECURE: Parameterized query using placeholder, VULNERABLE: Direct string formatting

### Community 9 - "09-ml-pipeline-very-hard.py"
Cohesion: 0.40
Nodes (4): MLPipelineProblematic, ModelMetrics, Review 09: ML Pipeline Architecture (Very Hard) Scenario: Data transformation…, \"\"PROBLEMATIC: Monolithic pipeline, no validation, no versioning\"\"\"\n \n…

## Knowledge Gaps
- **1 isolated node(s):** `ModelMetrics`
  These have ≤1 connection - possible missing edges or undocumented components.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **What connects `ModelMetrics` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `07-dependency-injection-medium.py` be split into smaller, more focused modules?**
  _Cohesion score 0.11428571428571428 - nodes in this community are weakly interconnected._
- **Should `UserService` be split into smaller, more focused modules?**
  _Cohesion score 0.125 - nodes in this community are weakly interconnected._
- **Should `OrderService` be split into smaller, more focused modules?**
  _Cohesion score 0.14285714285714285 - nodes in this community are weakly interconnected._