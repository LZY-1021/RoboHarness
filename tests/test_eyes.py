"""
Tests for the Eyes (Memory-Augmented RAG) component
"""

import unittest
import numpy as np
from soma.eyes import MemoryAugmentedRAG, ExperienceQuintuple


class TestMemoryAugmentedRAG(unittest.TestCase):
    """Test cases for Memory-Augmented RAG."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.embedding_dim = 768
        self.eyes = MemoryAugmentedRAG(embedding_dim=self.embedding_dim)
    
    def test_initialization(self):
        """Test RAG initialization."""
        self.assertEqual(self.eyes.embedding_dim, self.embedding_dim)
        self.assertEqual(len(self.eyes.memory_bank), 0)
        self.assertIsNone(self.eyes.embedding_index)
    
    def test_store_experience(self):
        """Test storing experience quintuples."""
        quintuple = ExperienceQuintuple(
            state={"position": [0, 0]},
            action={"move": "forward"},
            outcome={"success": True},
            embedding=np.random.rand(self.embedding_dim),
            failure_attribution=None
        )
        
        self.eyes.store_experience(quintuple)
        self.assertEqual(len(self.eyes.memory_bank), 1)
        self.assertIsNotNone(self.eyes.embedding_index)
    
    def test_store_experience_dimension_mismatch(self):
        """Test that storing experience with wrong dimension raises error."""
        quintuple = ExperienceQuintuple(
            state={"position": [0, 0]},
            action={"move": "forward"},
            outcome={"success": True},
            embedding=np.random.rand(512),  # Wrong dimension
            failure_attribution=None
        )
        
        with self.assertRaises(ValueError):
            self.eyes.store_experience(quintuple)
    
    def test_retrieve_experiences(self):
        """Test retrieving similar experiences."""
        # Store multiple experiences
        for i in range(10):
            quintuple = ExperienceQuintuple(
                state={"position": [i, i]},
                action={"move": "forward"},
                outcome={"success": True},
                embedding=np.random.rand(self.embedding_dim),
                failure_attribution=None
            )
            self.eyes.store_experience(quintuple)
        
        # Retrieve experiences
        query_embedding = np.random.rand(self.embedding_dim)
        results = self.eyes.retrieve_experiences(query_embedding, top_k=5)
        
        self.assertEqual(len(results), 5)
        self.assertTrue(all(isinstance(score, float) for _, score in results))
    
    def test_retrieve_experiences_with_filter(self):
        """Test retrieving experiences with failure filter."""
        # Store experiences with and without failures
        for i in range(5):
            failure_attr = {"error": "test_error"} if i < 2 else None
            quintuple = ExperienceQuintuple(
                state={"position": [i, i]},
                action={"move": "forward"},
                outcome={"success": i >= 2},
                embedding=np.random.rand(self.embedding_dim),
                failure_attribution=failure_attr
            )
            self.eyes.store_experience(quintuple)
        
        # Retrieve only failures
        query_embedding = np.random.rand(self.embedding_dim)
        results = self.eyes.retrieve_experiences(
            query_embedding,
            top_k=5,
            filter_failures=True
        )
        
        self.assertLessEqual(len(results), 2)
    
    def test_get_failure_contexts(self):
        """Test getting all failure contexts."""
        # Store experiences with failures
        for i in range(5):
            failure_attr = {"error": "test_error"} if i < 3 else None
            quintuple = ExperienceQuintuple(
                state={"position": [i, i]},
                action={"move": "forward"},
                outcome={"success": i >= 3},
                embedding=np.random.rand(self.embedding_dim),
                failure_attribution=failure_attr
            )
            self.eyes.store_experience(quintuple)
        
        failure_contexts = self.eyes.get_failure_contexts()
        self.assertEqual(len(failure_contexts), 3)
    
    def test_get_contextual_awareness(self):
        """Test getting contextual awareness."""
        # Store experiences
        for i in range(5):
            quintuple = ExperienceQuintuple(
                state={"position": [i, i]},
                action={"move": "forward"},
                outcome={"success": True},
                embedding=np.random.rand(self.embedding_dim),
                failure_attribution=None
            )
            self.eyes.store_experience(quintuple)
        
        query_embedding = np.random.rand(self.embedding_dim)
        context = self.eyes.get_contextual_awareness(query_embedding, top_k=3)
        
        self.assertIn("retrieved_experiences", context)
        self.assertIn("experiences", context)
        self.assertIn("similarity_scores", context)
        self.assertIn("failure_rate", context)
        self.assertEqual(context["retrieved_experiences"], 3)


if __name__ == "__main__":
    unittest.main()
