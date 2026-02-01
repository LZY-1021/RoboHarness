"""
SOMA Orchestrator

Main orchestrator that integrates the Eyes (Memory-Augmented RAG),
Brain (Strategic LLM), and MCP Tools to provide strategic orchestration
and memory-augmented agentic capabilities.
"""

from typing import Dict, List, Any, Optional
import numpy as np
from dataclasses import dataclass

from .eyes import MemoryAugmentedRAG, ExperienceQuintuple
from .brain import StrategicLLM, TheoreticalAttribution, RootCauseType
from .mcp_tools import MCPToolOrchestrator


@dataclass
class SOMAResult:
    """Result from SOMA orchestration."""
    success: bool
    contextual_awareness: Dict[str, Any]
    theoretical_attribution: TheoreticalAttribution
    orchestration_result: Dict[str, Any]
    strategic_conversion: Dict[str, Any]
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary representation."""
        return {
            "success": self.success,
            "contextual_awareness": self.contextual_awareness,
            "theoretical_attribution": {
                "root_cause": self.theoretical_attribution.root_cause.value,
                "confidence": self.theoretical_attribution.confidence,
                "explanation": self.theoretical_attribution.explanation,
                "suggested_strategies": self.theoretical_attribution.suggested_strategies,
                "model_weaknesses": self.theoretical_attribution.model_weaknesses,
                "potential_advantages": self.theoretical_attribution.potential_advantages
            },
            "orchestration_result": self.orchestration_result,
            "strategic_conversion": self.strategic_conversion
        }


class SOMAOrchestrator:
    """
    SOMA Strategic Orchestrator.
    
    Integrates the Eyes (Memory-Augmented RAG), Brain (Strategic LLM),
    and MCP Tools to provide zero-shot VLA generalization capabilities.
    
    Key Features:
    - Retrieves experience quintuples with multimodal embeddings
    - Performs theoretical attribution to diagnose root causes
    - Strategically converts model weaknesses into advantages
    - Orchestrates dynamic chain of MCP tools
    """
    
    def __init__(self, embedding_dim: int = 768, llm_model: Optional[str] = None):
        """
        Initialize the SOMA Orchestrator.
        
        Args:
            embedding_dim: Dimension of embedding vectors
            llm_model: Name of the LLM model to use for the Brain
        """
        # Initialize components
        self.eyes = MemoryAugmentedRAG(embedding_dim=embedding_dim)
        self.brain = StrategicLLM(model_name=llm_model)
        self.mcp_orchestrator = MCPToolOrchestrator()
        
        # Track orchestration history
        self.orchestration_history: List[SOMAResult] = []
    
    def process_experience(
        self,
        state: Dict[str, Any],
        action: Dict[str, Any],
        outcome: Dict[str, Any],
        embedding: np.ndarray,
        failure_attribution: Optional[Dict[str, Any]] = None
    ) -> None:
        """
        Process and store a new experience quintuple.
        
        Args:
            state: State information
            action: Action taken
            outcome: Outcome observed
            embedding: Multimodal embedding vector
            failure_attribution: Optional failure attribution information
        """
        quintuple = ExperienceQuintuple(
            state=state,
            action=action,
            outcome=outcome,
            embedding=embedding,
            failure_attribution=failure_attribution
        )
        
        self.eyes.store_experience(quintuple)
    
    def orchestrate(
        self,
        query_embedding: np.ndarray,
        current_context: Dict[str, Any],
        failure_info: Optional[Dict[str, Any]] = None
    ) -> SOMAResult:
        """
        Main orchestration method that coordinates Eyes, Brain, and MCP Tools.
        
        Args:
            query_embedding: Query embedding for retrieving relevant experiences
            current_context: Current context information
            failure_info: Optional information about a failure to analyze
        
        Returns:
            SOMAResult containing the complete orchestration outcome
        """
        # Step 1: Eyes - Retrieve contextual awareness
        contextual_awareness = self.eyes.get_contextual_awareness(
            query_embedding=query_embedding,
            top_k=5
        )
        
        # Merge current context with retrieved context
        merged_context = {**current_context, **contextual_awareness}
        
        # Step 2: Brain - Perform theoretical attribution
        if failure_info is None:
            # If no failure info provided, check if we need to diagnose
            failure_info = self._detect_potential_failure(merged_context)
        
        attribution = self.brain.diagnose_root_cause(
            context=merged_context,
            failure_info=failure_info
        )
        
        # Step 3: Strategic Conversion - Convert weaknesses to advantages
        strategic_conversion = self._convert_weaknesses_to_advantages(attribution)
        
        # Step 4: MCP Orchestration - Execute tool chain
        orchestration_context = {
            "root_cause": attribution.root_cause.value,
            "weaknesses": attribution.model_weaknesses,
            "advantages": attribution.potential_advantages
        }
        
        orchestration_result = self.mcp_orchestrator.orchestrate(
            context=orchestration_context,
            strategies=attribution.suggested_strategies,
            input_data=current_context
        )
        
        # Create result
        result = SOMAResult(
            success=orchestration_result["success_rate"] > 0.5,
            contextual_awareness=contextual_awareness,
            theoretical_attribution=attribution,
            orchestration_result=orchestration_result,
            strategic_conversion=strategic_conversion
        )
        
        # Store in history
        self.orchestration_history.append(result)
        
        return result
    
    def _detect_potential_failure(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Detect potential failures from context.
        
        Args:
            context: Context information
        
        Returns:
            Failure information dictionary
        """
        failure_info = {
            "failure_detected": False,
            "failure_type": "unknown"
        }
        
        # Check failure rate from retrieved experiences
        if context.get("failure_rate", 0) > 0.5:
            failure_info["failure_detected"] = True
            failure_info["failure_type"] = "high_failure_rate"
        
        return failure_info
    
    def _convert_weaknesses_to_advantages(
        self,
        attribution: TheoreticalAttribution
    ) -> Dict[str, Any]:
        """
        Strategically convert identified model weaknesses into advantages.
        
        This is a core capability of SOMA - rather than merely avoiding errors,
        it strategically converts weaknesses into advantages.
        
        Args:
            attribution: Theoretical attribution from the Brain
        
        Returns:
            Strategic conversion information
        """
        conversion_strategies = []
        
        for weakness, advantage in zip(
            attribution.model_weaknesses,
            attribution.potential_advantages
        ):
            conversion_strategies.append({
                "weakness": weakness,
                "advantage": advantage,
                "strategy": self._generate_conversion_strategy(weakness, advantage)
            })
        
        return {
            "conversions": conversion_strategies,
            "total_weaknesses": len(attribution.model_weaknesses),
            "total_advantages": len(attribution.potential_advantages),
            "conversion_confidence": attribution.confidence
        }
    
    def _generate_conversion_strategy(
        self,
        weakness: str,
        advantage: str
    ) -> str:
        """Generate a specific strategy for converting a weakness to an advantage."""
        if "correlation" in weakness.lower():
            return "Leverage correlation detection for rapid hypothesis generation"
        elif "visual" in weakness.lower():
            return "Use visual feature sensitivity for enhanced perception tasks"
        elif "susceptible" in weakness.lower():
            return "Fine-tune on targeted examples to build robustness"
        else:
            return "Apply strategic adaptation to leverage identified patterns"
    
    def get_comprehensive_summary(self) -> Dict[str, Any]:
        """
        Get a comprehensive summary of SOMA's performance.
        
        Returns:
            Dictionary containing comprehensive system summary
        """
        # Get component summaries
        eyes_summary = {
            "total_experiences": len(self.eyes.memory_bank),
            "failure_experiences": len(self.eyes.get_failure_contexts())
        }
        
        brain_summary = self.brain.get_strategic_analysis()
        mcp_summary = self.mcp_orchestrator.get_execution_stats()
        
        # Overall performance
        overall_summary = {
            "total_orchestrations": len(self.orchestration_history),
            "success_rate": sum(1 for r in self.orchestration_history if r.success) / max(len(self.orchestration_history), 1),
            "average_conversion_confidence": sum(
                r.strategic_conversion["conversion_confidence"]
                for r in self.orchestration_history
            ) / max(len(self.orchestration_history), 1)
        }
        
        return {
            "eyes": eyes_summary,
            "brain": brain_summary,
            "mcp_tools": mcp_summary,
            "overall": overall_summary
        }
    
    def adaptive_generalization(
        self,
        query_embedding: np.ndarray,
        task_context: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Perform adaptive zero-shot generalization for a new task.
        
        This method demonstrates SOMA's ability to generalize to zero-shot
        scenarios by leveraging memory-augmented retrieval and strategic reasoning.
        
        Args:
            query_embedding: Query embedding for the new task
            task_context: Context information about the task
        
        Returns:
            Generalization result with recommendations
        """
        # Retrieve similar experiences
        similar_experiences = self.eyes.retrieve_experiences(
            query_embedding=query_embedding,
            top_k=10
        )
        
        # Analyze patterns from similar experiences
        pattern_analysis = self._analyze_experience_patterns(similar_experiences)
        
        # Generate strategic recommendations
        recommendations = self._generate_generalization_recommendations(
            pattern_analysis,
            task_context
        )
        
        return {
            "similar_experiences_found": len(similar_experiences),
            "pattern_analysis": pattern_analysis,
            "recommendations": recommendations,
            "generalization_confidence": self._calculate_generalization_confidence(
                similar_experiences,
                pattern_analysis
            )
        }
    
    def _analyze_experience_patterns(
        self,
        experiences: List[tuple]
    ) -> Dict[str, Any]:
        """Analyze patterns from retrieved experiences."""
        if not experiences:
            return {"patterns": [], "confidence": 0.0}
        
        # Analyze success/failure patterns
        failures = [exp for exp, score in experiences if exp.failure_attribution is not None]
        
        return {
            "total_experiences": len(experiences),
            "failure_count": len(failures),
            "success_rate": (len(experiences) - len(failures)) / len(experiences),
            "patterns": ["pattern_1", "pattern_2"]  # Simplified
        }
    
    def _generate_generalization_recommendations(
        self,
        pattern_analysis: Dict[str, Any],
        task_context: Dict[str, Any]
    ) -> List[str]:
        """Generate recommendations for zero-shot generalization."""
        recommendations = []
        
        if pattern_analysis.get("success_rate", 0) > 0.7:
            recommendations.append("High success rate observed - apply similar strategies")
        else:
            recommendations.append("Low success rate - apply adaptive strategies")
        
        recommendations.append("Leverage strategic tool orchestration")
        recommendations.append("Monitor for potential weaknesses and convert to advantages")
        
        return recommendations
    
    def _calculate_generalization_confidence(
        self,
        experiences: List[tuple],
        pattern_analysis: Dict[str, Any]
    ) -> float:
        """Calculate confidence in generalization capability."""
        base_confidence = 0.5
        
        # Increase confidence with more experiences
        if len(experiences) > 0:
            base_confidence += min(0.3, len(experiences) * 0.03)
        
        # Adjust based on success rate
        success_rate = pattern_analysis.get("success_rate", 0)
        base_confidence += success_rate * 0.2
        
        return min(base_confidence, 1.0)
