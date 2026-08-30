"""
Review 04: Performance Bottleneck (Hard)
Scenario: Memory inefficient data processing
"""

from typing import List, Iterator
import numpy as np

class DataProcessor:
    def __init__(self, batch_size: int = 1000):
        self.batch_size = batch_size
    
    def process_large_file_inefficient(self, filepath: str) -> List[dict]:
        """
        INEFFICIENT: Loads entire file into memory
        - For 1GB file: 1GB+ RAM usage
        - No streaming
        - Full data kept until processing complete
        """
        data = []
        with open(filepath, 'r') as f:
            for line in f:
                record = {
                    'id': int(line.split(',')[0]),
                    'value': float(line.split(',')[1]),
                    'timestamp': line.split(',')[2],
                }
                data.append(record)
        
        # Process all at once
        for record in data:
            record['value'] = record['value'] * 2
        
        return data
    
    def process_large_file_efficient(self, filepath: str) -> Iterator[dict]:
        """
        EFFICIENT: Streaming with generator pattern
        - Constant memory usage regardless of file size
        - Process one batch at a time
        - Lazy evaluation
        """
        batch = []
        with open(filepath, 'r') as f:
            for line in f:
                record = {
                    'id': int(line.split(',')[0]),
                    'value': float(line.split(',')[1]),
                    'timestamp': line.split(',')[2],
                }
                record['value'] = record['value'] * 2
                
                batch.append(record)
                if len(batch) >= self.batch_size:
                    yield from batch
                    batch = []
            
            if batch:
                yield from batch
    
    def calculate_statistics_slow(self, data: List[float]) -> dict:
        """
        SLOW: Multiple passes, redundant calculations
        - O(n) for mean, O(n) for std dev, O(n) for min, O(n) for max
        - Total: 4 passes over data
        """
        mean = sum(data) / len(data)
        variance = sum((x - mean) ** 2 for x in data) / len(data)
        std_dev = variance ** 0.5
        
        min_val = min(data)
        max_val = max(data)
        
        return {
            'mean': mean,
            'std_dev': std_dev,
            'min': min_val,
            'max': max_val
        }
    
    def calculate_statistics_fast(self, data: List[float]) -> dict:
        """
        FAST: Single pass with numpy
        - Vectorized operations
        - Compiled C code underneath
        - ~100x faster for large datasets
        """
        arr = np.array(data)
        return {
            'mean': float(np.mean(arr)),
            'std_dev': float(np.std(arr)),
            'min': float(np.min(arr)),
            'max': float(np.max(arr))
        }


# Issues:
# 1. process_large_file_inefficient() causes OOM on large files
# 2. calculate_statistics_slow() makes 4 passes (inefficient)
# 3. No streaming or batch processing
# Recommendation: Use generators, numpy, streaming patterns
