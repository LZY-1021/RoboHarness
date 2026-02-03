"""
Tests for the SOMA Orchestrator
"""

import unittest
import numpy as np
from soma.orchestrator import SOMAOrchestrator


class TestSOMAOrchestrator(unittest.TestCase):
    """Test cases for SOMA Orchestrator."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.embedding_dim = 768
        self.soma = SOMAOrchestrator(embedding_dim=self.embedding_dim)
    
    def test_initialization(self):
        """Test orchestrator initialization."""
        self.assertIsNotNone(self.soma.eyes)
        self.assertIsNotNone(self.soma.brain)
        self.assertIsNotNone(self.soma.mcp_orchestrator)
        self.assertEqual(len(self.soma.orchestration_history), 0)
    
    def test_process_experience(self):
        """Test processing experiences."""
        state = {"position": [0, 0]}
        action = {"move": "forward"}
        outcome = {"success": True}
        embedding = np.random.rand(self.embedding_dim)
        
        self.soma.process_experience(state, action, outcome, embedding)
        
        self.assertEqual(len(self.soma.eyes.memory_bank), 1)
    
    def test_orchestrate(self):
        """Test full orchestration process."""
        # Add some experiences first
        for i in range(5):
            state = {"position": [i, i]}
            action = {"move": "forward"}
            outcome = {"success": True}
            embedding = np.random.rand(self.embedding_dim)
            self.soma.process_experience(state, action, outcome, embedding)
        
        # Run orchestration
        query_embedding = np.random.rand(self.embedding_dim)
        current_context = {"task": "navigation"}
        failure_info = {"error": "test_error"}
        
        result = self.soma.orchestrate(query_embedding, current_context, failure_info)
        
        self.assertIsNotNone(result)
        self.assertIn("contextual_awareness", result.to_dict())
        self.assertIn("theoretical_attribution", result.to_dict())
        self.assertIn("orchestration_result", result.to_dict())
        self.assertIn("strategic_conversion", result.to_dict())
    
    def test_strategic_conversion(self):
        """Test strategic conversion of weaknesses to advantages."""
        # Add experiences
        for i in range(3):
            embedding = np.random.rand(self.embedding_dim)
            failure_attr = {"error": "visual_bias"} if i == 0 else None
            self.soma.process_experience(
                {"position": [i, i]},
                {"move": "forward"},
                {"success": i > 0},
                embedding,
                failure_attr
            )
        
        # Run orchestration
        query_embedding = np.random.rand(self.embedding_dim)
        result = self.soma.orchestrate(
            query_embedding,
            {"task": "test"},
            {"failure_type": "visual_error"}
        )
        
        conversion = result.strategic_conversion
        self.assertIn("conversions", conversion)
        self.assertIn("conversion_confidence", conversion)
    
    def test_comprehensive_summary(self):
        """Test getting comprehensive summary."""
        # Add experiences and run orchestration
        for i in range(3):
            embedding = np.random.rand(self.embedding_dim)
            self.soma.process_experience(
                {"position": [i, i]},
                {"move": "forward"},
                {"success": True},
                embedding
            )
        
        query_embedding = np.random.rand(self.embedding_dim)
        self.soma.orchestrate(query_embedding, {"task": "test"})
        
        summary = self.soma.get_comprehensive_summary()
        
        self.assertIn("eyes", summary)
        self.assertIn("brain", summary)
        self.assertIn("mcp_tools", summary)
        self.assertIn("overall", summary)
    
    def test_adaptive_generalization(self):
        """Test adaptive zero-shot generalization."""
        # Add experiences
        for i in range(5):
            embedding = np.random.rand(self.embedding_dim)
            self.soma.process_experience(
                {"position": [i, i]},
                {"move": "forward"},
                {"success": True},
                embedding
            )
        
        # Test generalization
        query_embedding = np.random.rand(self.embedding_dim)
        task_context = {"task": "new_task", "environment": "unknown"}
        
        result = self.soma.adaptive_generalization(query_embedding, task_context)
        
        self.assertIn("similar_experiences_found", result)
        self.assertIn("pattern_analysis", result)
        self.assertIn("recommendations", result)
        self.assertIn("generalization_confidence", result)
    
    def test_zero_shot_scenario(self):
        """Test zero-shot scenario with no prior experiences."""
        query_embedding = np.random.rand(self.embedding_dim)
        result = self.soma.orchestrate(
            query_embedding,
            {"task": "new_task"},
            {"error": "unknown"}
        )
        
        # Should still work with no experiences
        self.assertIsNotNone(result)
        self.assertIsInstance(result.success, bool)


if __name__ == "__main__":
    unittest.main()
