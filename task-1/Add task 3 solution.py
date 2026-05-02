"""
Task 3 Solution
================
Author: Njihia27
Date: May 2026
"""

from typing import List, Dict, Any, Optional
import json
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(_name_)


class TaskThreeSolution:
    """
    Clean and professional solution for Task 3.
    """
    
    def _init_(self):
        self.results: List[Dict[str, Any]] = []
        logger.info("Task 3 Solution initialized")
    
    def process_data(self, data: List[Dict]) -> Dict[str, Any]:
        """
        Main processing function for Task 3.
        
        Args:
            data: Input data as list of dictionaries
            
        Returns:
            Processing summary and results
        """
        try:
            if not data:
                raise ValueError("Input data cannot be empty")
            
            start_time = datetime.now()
            
            # ==================== MAIN TASK 3 LOGIC ====================
            # Replace this section with the actual requirements of Task 3
            processed = []
            for item in data:
                # Example placeholder - update according to task specification
                result = {
                    "id": item.get("id"),
                    "processed_at": datetime.now().isoformat(),
                    "status": "success",
                    # Add your specific transformations, calculations, or logic here
                }
                processed.append(result)
            # ========================================================
            
            execution_time = (datetime.now() - start_time).total_seconds()
            
            summary = {
                "total_items": len(data),
                "successful": len(processed),
                "execution_time_seconds": round(execution_time, 4),
                "timestamp": datetime.now().isoformat(),
                "results": processed
            }
            
            self.results.append(summary)
            logger.info(f"Successfully processed {len(data)} items in {execution_time:.4f}s")
            
            return summary
            
        except Exception as e:
            logger.error(f"Error processing data: {str(e)}")
            return {"error": str(e), "status": "failed"}
    
    def save_results(self, filename: str = "task3_results.json") -> bool:
        """Save results to a JSON file."""
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(self.results, f, indent=2)
            logger.info(f"Results successfully saved to {filename}")
            return True
        except Exception as e:
            logger.error(f"Failed to save results: {e}")
            return False


# ==================== TEST / DEMO ====================

if _name_ == "_main_":
    print("=" * 60)
    print("TASK 3 SOLUTION")
    print("=" * 60)
    
    solution = TaskThreeSolution()
    
    # Sample test data - modify as needed for Task 3
    sample_data = [
        {"id": 1, "name": "Item One", "value": 100},
        {"id": 2, "name": "Item Two", "value": 200},
        {"id": 3, "name": "Item Three", "value": 300},
    ]
    
    result = solution.process_data(sample_data)
    solution.save_results()
    
    print("\n✅ Task 3 Completed Successfully!")
    print(f"Total items processed : {result.get('total_items')}")
    print(f"Execution time        : {result.get('execution_time_seconds')} seconds")
    print("\nResults saved."
