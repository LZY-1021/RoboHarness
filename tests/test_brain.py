"""
Tests for the Brain (Strategic LLM) component
"""

import unittest
from soma.brain import StrategicLLM, RootCauseType


class TestStrategicLLM(unittest.TestCase):
    """Test cases for Strategic LLM."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.brain = StrategicLLM()
    
    def test_initialization(self):
        """Test LLM initialization."""
        self.assertIsNotNone(self.brain.model_name)
        self.assertEqual(len(self.brain.attribution_history), 0)
    
    def test_diagnose_causal_confusion(self):
        """Test diagnosing causal confusion."""
        context = {
            "retrieved_experiences": 5,
            "experiences": [
                {"action": {"move": "forward"}, "outcome": {"success": True}},
                {"action": {"move": "forward"}, "outcome": {"success": False}}
            ]
        }
        failure_info = {"error": "inconsistent_outcome"}
        
        attribution = self.brain.diagnose_root_cause(context, failure_info)
        
        self.assertIsInstance(attribution.root_cause, RootCauseType)
        self.assertGreater(attribution.confidence, 0)
        self.assertIsNotNone(attribution.explanation)
        self.assertGreater(len(attribution.suggested_strategies), 0)
    
    def test_diagnose_visual_bias(self):
        """Test diagnosing visual bias."""
        context = {"retrieved_experiences": 3}
        failure_info = {"failure_type": "visual_recognition_error"}
        
        attribution = self.brain.diagnose_root_cause(context, failure_info)
        
        self.assertEqual(attribution.root_cause, RootCauseType.VISUAL_BIAS)
        self.assertIn("visual", attribution.explanation.lower())
    
    def test_diagnose_distributional_shift(self):
        """Test diagnosing distributional shift."""
        context = {"failure_rate": 0.8}
        failure_info = {"error": "high_failure_rate"}
        
        attribution = self.brain.diagnose_root_cause(context, failure_info)
        
        self.assertEqual(attribution.root_cause, RootCauseType.DISTRIBUTIONAL_SHIFT)
    
    def test_convert_weaknesses_to_advantages(self):
        """Test converting weaknesses to advantages."""
        context = {"retrieved_experiences": 3}
        failure_info = {"error": "test_error"}
        
        attribution = self.brain.diagnose_root_cause(context, failure_info)
        
        self.assertGreater(len(attribution.model_weaknesses), 0)
        self.assertGreater(len(attribution.potential_advantages), 0)
    
    def test_get_strategic_analysis(self):
        """Test getting strategic analysis."""
        # Run multiple diagnoses
        for i in range(3):
            context = {"retrieved_experiences": i + 1}
            failure_info = {"error": f"error_{i}"}
            self.brain.diagnose_root_cause(context, failure_info)
        
        analysis = self.brain.get_strategic_analysis()
        
        self.assertEqual(analysis["total_attributions"], 3)
        self.assertIn("common_root_causes", analysis)
        self.assertIn("average_confidence", analysis)
    
    def test_confidence_calculation(self):
        """Test confidence calculation."""
        context = {"retrieved_experiences": 10}
        failure_info = {"error": "test_error"}
        
        attribution = self.brain.diagnose_root_cause(context, failure_info)
        
        self.assertGreaterEqual(attribution.confidence, 0)
        self.assertLessEqual(attribution.confidence, 1.0)


if __name__ == "__main__":
    unittest.main()
