"""
SOMA: Strategic Orchestration and Memory-Augmented Agentic System
for Zero-Shot VLA Generalization
"""

__version__ = "0.1.0"

from .eyes import MemoryAugmentedRAG
from .brain import StrategicLLM
from .mcp_tools import MCPToolOrchestrator
from .orchestrator import SOMAOrchestrator

__all__ = [
    "MemoryAugmentedRAG",
    "StrategicLLM",
    "MCPToolOrchestrator",
    "SOMAOrchestrator",
]
