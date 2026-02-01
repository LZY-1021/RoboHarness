"""
Brain (Strategic LLM) Component

Performs theoretical attribution to diagnose root causes like causal confusion
or visual biases.
"""

from typing import Dict, List, Any, Optional
from dataclasses import dataclass
from enum import Enum


class RootCauseType(Enum):
    """Types of root causes that can be diagnosed."""
    CAUSAL_CONFUSION = "causal_confusion"
    VISUAL_BIAS = "visual_bias"
    DISTRIBUTIONAL_SHIFT = "distributional_shift"
    SPURIOUS_CORRELATION = "spurious_correlation"
    OVERFITTING = "overfitting"
    UNDERFITTING = "underfitting"
    UNKNOWN = "unknown"


@dataclass
class TheoreticalAttribution:
    """
    Theoretical attribution result from the Strategic LLM.
    """
    root_cause: RootCauseType
    confidence: float
    explanation: str
    suggested_strategies: List[str]
    model_weaknesses: List[str]
    potential_advantages: List[str]


class StrategicLLM:
    """
    Strategic LLM component - the "Brain" of SOMA.
    
    Performs theoretical attribution to diagnose root causes and
    strategically converts identified model weaknesses into advantages.
    """
    
    def __init__(self, model_name: Optional[str] = None):
        """
        Initialize the Strategic LLM.
        
        Args:
            model_name: Name of the LLM model to use
        """
        self.model_name = model_name or "strategic-llm-v1"
        self.attribution_history: List[TheoreticalAttribution] = []
    
    def diagnose_root_cause(
        self,
        context: Dict[str, Any],
        failure_info: Dict[str, Any]
    ) -> TheoreticalAttribution:
        """
        Diagnose the root cause of a failure using theoretical attribution.
        
        Args:
            context: Contextual information from the Eyes component
            failure_info: Information about the failure
        
        Returns:
            Theoretical attribution with diagnosed root cause
        """
        # Analyze failure patterns
        root_cause = self._analyze_failure_patterns(context, failure_info)
        
        # Generate strategic recommendations
        strategies = self._generate_strategies(root_cause, context)
        
        # Identify model weaknesses
        weaknesses = self._identify_weaknesses(root_cause, failure_info)
        
        # Find potential advantages
        advantages = self._convert_weaknesses_to_advantages(weaknesses)
        
        attribution = TheoreticalAttribution(
            root_cause=root_cause,
            confidence=self._calculate_confidence(context, failure_info),
            explanation=self._generate_explanation(root_cause, context),
            suggested_strategies=strategies,
            model_weaknesses=weaknesses,
            potential_advantages=advantages
        )
        
        self.attribution_history.append(attribution)
        return attribution
    
    def _analyze_failure_patterns(
        self,
        context: Dict[str, Any],
        failure_info: Dict[str, Any]
    ) -> RootCauseType:
        """
        Analyze failure patterns to identify root cause type.
        
        Args:
            context: Contextual information
            failure_info: Failure information
        
        Returns:
            Diagnosed root cause type
        """
        # Check for causal confusion indicators
        if self._check_causal_confusion(context, failure_info):
            return RootCauseType.CAUSAL_CONFUSION
        
        # Check for visual bias indicators
        if self._check_visual_bias(context, failure_info):
            return RootCauseType.VISUAL_BIAS
        
        # Check for distributional shift
        if self._check_distributional_shift(context, failure_info):
            return RootCauseType.DISTRIBUTIONAL_SHIFT
        
        # Check for spurious correlations
        if self._check_spurious_correlation(context, failure_info):
            return RootCauseType.SPURIOUS_CORRELATION
        
        return RootCauseType.UNKNOWN
    
    def _check_causal_confusion(
        self,
        context: Dict[str, Any],
        failure_info: Dict[str, Any]
    ) -> bool:
        """Check for causal confusion indicators."""
        # Look for inconsistent action-outcome relationships
        if "experiences" in context:
            experiences = context["experiences"]
            if len(experiences) > 1:
                # Check if similar actions lead to different outcomes
                action_consistency = self._analyze_action_consistency(experiences)
                return action_consistency < 0.5
        return False
    
    def _check_visual_bias(
        self,
        context: Dict[str, Any],
        failure_info: Dict[str, Any]
    ) -> bool:
        """Check for visual bias indicators."""
        if "failure_type" in failure_info:
            return "visual" in failure_info["failure_type"].lower()
        return False
    
    def _check_distributional_shift(
        self,
        context: Dict[str, Any],
        failure_info: Dict[str, Any]
    ) -> bool:
        """Check for distributional shift indicators."""
        if "failure_rate" in context:
            return context["failure_rate"] > 0.7
        return False
    
    def _check_spurious_correlation(
        self,
        context: Dict[str, Any],
        failure_info: Dict[str, Any]
    ) -> bool:
        """Check for spurious correlation indicators."""
        if "correlation_detected" in failure_info:
            return failure_info["correlation_detected"]
        return False
    
    def _analyze_action_consistency(self, experiences: List[Dict[str, Any]]) -> float:
        """
        Analyze consistency of action-outcome relationships.
        
        Returns:
            Consistency score between 0 and 1
        """
        # Simplified consistency analysis
        # In a real implementation, this would use more sophisticated analysis
        return 0.6
    
    def _generate_strategies(
        self,
        root_cause: RootCauseType,
        context: Dict[str, Any]
    ) -> List[str]:
        """Generate strategic recommendations based on root cause."""
        strategies = []
        
        if root_cause == RootCauseType.CAUSAL_CONFUSION:
            strategies.extend([
                "Apply causal intervention techniques",
                "Use counterfactual reasoning",
                "Implement temporal consistency checks"
            ])
        elif root_cause == RootCauseType.VISUAL_BIAS:
            strategies.extend([
                "Apply domain randomization",
                "Use adversarial training",
                "Implement visual attention mechanisms"
            ])
        elif root_cause == RootCauseType.DISTRIBUTIONAL_SHIFT:
            strategies.extend([
                "Apply domain adaptation techniques",
                "Use test-time adaptation",
                "Implement robust feature extraction"
            ])
        
        return strategies
    
    def _identify_weaknesses(
        self,
        root_cause: RootCauseType,
        failure_info: Dict[str, Any]
    ) -> List[str]:
        """Identify model weaknesses based on root cause."""
        weaknesses = []
        
        if root_cause == RootCauseType.CAUSAL_CONFUSION:
            weaknesses.append("Inability to distinguish correlation from causation")
        elif root_cause == RootCauseType.VISUAL_BIAS:
            weaknesses.append("Over-reliance on visual features")
        
        if "error_type" in failure_info:
            weaknesses.append(f"Susceptible to {failure_info['error_type']} errors")
        
        return weaknesses
    
    def _convert_weaknesses_to_advantages(
        self,
        weaknesses: List[str]
    ) -> List[str]:
        """
        Convert identified weaknesses into potential advantages.
        
        This is a key strategic capability of SOMA - rather than merely avoiding
        errors, it converts model weaknesses into advantages.
        """
        advantages = []
        
        for weakness in weaknesses:
            if "correlation" in weakness.lower():
                advantages.append("Can identify hidden patterns in data")
            elif "visual" in weakness.lower():
                advantages.append("Can leverage visual features for rapid perception")
            elif "susceptible" in weakness.lower():
                advantages.append("Can be fine-tuned for specific error types")
        
        return advantages
    
    def _calculate_confidence(
        self,
        context: Dict[str, Any],
        failure_info: Dict[str, Any]
    ) -> float:
        """Calculate confidence score for the attribution."""
        base_confidence = 0.7
        
        # Increase confidence with more context
        if "retrieved_experiences" in context:
            base_confidence += min(0.2, context["retrieved_experiences"] * 0.02)
        
        return min(base_confidence, 1.0)
    
    def _generate_explanation(
        self,
        root_cause: RootCauseType,
        context: Dict[str, Any]
    ) -> str:
        """Generate human-readable explanation of the diagnosis."""
        explanations = {
            RootCauseType.CAUSAL_CONFUSION: "The model appears to confuse correlation with causation, leading to incorrect action selections.",
            RootCauseType.VISUAL_BIAS: "The model exhibits bias towards certain visual features, potentially missing important contextual information.",
            RootCauseType.DISTRIBUTIONAL_SHIFT: "The model encounters data that differs significantly from its training distribution.",
            RootCauseType.SPURIOUS_CORRELATION: "The model relies on spurious correlations that don't generalize.",
            RootCauseType.UNKNOWN: "The root cause could not be definitively identified."
        }
        
        return explanations.get(root_cause, "Unknown root cause")
    
    def get_strategic_analysis(self) -> Dict[str, Any]:
        """
        Get comprehensive strategic analysis based on attribution history.
        
        Returns:
            Dictionary containing strategic analysis
        """
        if not self.attribution_history:
            return {"status": "No attributions available"}
        
        # Aggregate insights from history
        root_causes = [attr.root_cause for attr in self.attribution_history]
        all_weaknesses = [w for attr in self.attribution_history for w in attr.model_weaknesses]
        all_advantages = [a for attr in self.attribution_history for a in attr.potential_advantages]
        
        return {
            "total_attributions": len(self.attribution_history),
            "common_root_causes": self._get_most_common(root_causes),
            "identified_weaknesses": list(set(all_weaknesses)),
            "strategic_advantages": list(set(all_advantages)),
            "average_confidence": sum(attr.confidence for attr in self.attribution_history) / len(self.attribution_history)
        }
    
    def _get_most_common(self, items: List[Any]) -> List[Any]:
        """Get most common items from a list."""
        from collections import Counter
        counter = Counter(items)
        return [item for item, count in counter.most_common(3)]
