"""
Tests for the MCP Tools component
"""

import unittest
from soma.mcp_tools import (
    MCPToolOrchestrator,
    MCPToolType,
    DomainAdaptationTool,
    CausalInterventionTool,
    VisualAugmentationTool
)


class TestMCPTools(unittest.TestCase):
    """Test cases for MCP Tools."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.orchestrator = MCPToolOrchestrator()
    
    def test_initialization(self):
        """Test orchestrator initialization."""
        self.assertGreater(len(self.orchestrator.tools), 0)
        self.assertEqual(len(self.orchestrator.execution_history), 0)
    
    def test_domain_adaptation_tool(self):
        """Test domain adaptation tool."""
        tool = DomainAdaptationTool()
        input_data = {"features": [1, 2, 3]}
        
        result = tool.execute(input_data)
        
        self.assertTrue(result.success)
        self.assertEqual(result.tool_type, MCPToolType.DOMAIN_ADAPTATION)
        self.assertIn("adapted_features", result.output)
    
    def test_causal_intervention_tool(self):
        """Test causal intervention tool."""
        tool = CausalInterventionTool()
        input_data = {"state": "test"}
        
        result = tool.execute(input_data)
        
        self.assertTrue(result.success)
        self.assertEqual(result.tool_type, MCPToolType.CAUSAL_INTERVENTION)
        self.assertIn("causal_graph", result.output)
    
    def test_visual_augmentation_tool(self):
        """Test visual augmentation tool."""
        tool = VisualAugmentationTool()
        input_data = {"image": "test_image"}
        
        result = tool.execute(input_data)
        
        self.assertTrue(result.success)
        self.assertEqual(result.tool_type, MCPToolType.VISUAL_AUGMENTATION)
        self.assertIn("augmented_views", result.output)
    
    def test_tool_selection(self):
        """Test tool selection based on context."""
        context = {"root_cause": "causal_confusion"}
        strategies = ["intervention"]
        
        selected_tools = self.orchestrator.select_tools(context, strategies)
        
        self.assertGreater(len(selected_tools), 0)
    
    def test_tool_chain_execution(self):
        """Test executing a chain of tools."""
        tools = [
            self.orchestrator.tools[MCPToolType.CAUSAL_INTERVENTION],
            self.orchestrator.tools[MCPToolType.COUNTERFACTUAL_REASONING]
        ]
        input_data = {"test": "data"}
        
        results = self.orchestrator.execute_tool_chain(tools, input_data)
        
        self.assertEqual(len(results), 2)
        self.assertTrue(all(result.success for result in results))
    
    def test_orchestrate(self):
        """Test full orchestration."""
        context = {"root_cause": "visual_bias"}
        strategies = ["augmentation"]
        input_data = {"image": "test"}
        
        result = self.orchestrator.orchestrate(context, strategies, input_data)
        
        self.assertIn("selected_tools", result)
        self.assertIn("execution_results", result)
        self.assertIn("success_rate", result)
        self.assertGreater(result["success_rate"], 0)
    
    def test_execution_stats(self):
        """Test getting execution statistics."""
        # Execute some tools
        context = {"root_cause": "causal_confusion"}
        strategies = ["intervention"]
        input_data = {"test": "data"}
        
        self.orchestrator.orchestrate(context, strategies, input_data)
        self.orchestrator.orchestrate(context, strategies, input_data)
        
        stats = self.orchestrator.get_execution_stats()
        
        self.assertIn("total_executions", stats)
        self.assertIn("tool_usage", stats)
        self.assertGreater(stats["total_executions"], 0)


if __name__ == "__main__":
    unittest.main()
