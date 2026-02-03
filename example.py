"""
Example usage of SOMA for zero-shot VLA generalization.

This example demonstrates how to use SOMA to:
1. Store experiences with multimodal embeddings
2. Diagnose failure root causes
3. Convert weaknesses to advantages
4. Orchestrate MCP tools
"""

import numpy as np
from soma import SOMAOrchestrator


def main():
    print("=" * 60)
    print("SOMA: Strategic Orchestration and Memory-Augmented System")
    print("=" * 60)
    print()
    
    # Initialize SOMA
    embedding_dim = 768
    soma = SOMAOrchestrator(embedding_dim=embedding_dim)
    print(f"✓ Initialized SOMA with embedding dimension: {embedding_dim}")
    print()
    
    # Simulate storing multiple experiences
    print("Storing experiences...")
    for i in range(10):
        state = {"position": [i, i], "orientation": i * 45}
        action = {"move": "forward", "speed": i * 0.1}
        outcome = {"success": i > 3, "distance": i * 10}
        embedding = np.random.rand(embedding_dim)
        
        # Add failure attribution for some experiences
        failure_attr = None
        if i <= 3:
            failure_attr = {
                "error": "visual_bias" if i % 2 == 0 else "causal_confusion",
                "details": f"Failed at iteration {i}"
            }
        
        soma.process_experience(state, action, outcome, embedding, failure_attr)
    
    print(f"✓ Stored {len(soma.eyes.memory_bank)} experiences")
    print(f"  - Failure experiences: {len(soma.eyes.get_failure_contexts())}")
    print()
    
    # Run orchestration for a new scenario
    print("Running orchestration for new scenario...")
    query_embedding = np.random.rand(embedding_dim)
    current_context = {
        "task": "navigation",
        "environment": "indoor",
        "difficulty": "high"
    }
    failure_info = {
        "failure_type": "visual_recognition_error",
        "error": "unable_to_identify_object"
    }
    
    result = soma.orchestrate(query_embedding, current_context, failure_info)
    print()
    
    # Display results
    print("=" * 60)
    print("ORCHESTRATION RESULTS")
    print("=" * 60)
    print()
    
    print("1. CONTEXTUAL AWARENESS (Eyes)")
    print("-" * 60)
    ca = result.contextual_awareness
    print(f"   Retrieved experiences: {ca['retrieved_experiences']}")
    print(f"   Failure rate: {ca['failure_rate']:.2%}")
    print()
    
    print("2. THEORETICAL ATTRIBUTION (Brain)")
    print("-" * 60)
    ta = result.theoretical_attribution
    print(f"   Root cause: {ta.root_cause.value}")
    print(f"   Confidence: {ta.confidence:.2%}")
    print(f"   Explanation: {ta.explanation}")
    print()
    print("   Identified weaknesses:")
    for weakness in ta.model_weaknesses:
        print(f"     • {weakness}")
    print()
    print("   Potential advantages (Strategic Conversion):")
    for advantage in ta.potential_advantages:
        print(f"     • {advantage}")
    print()
    print("   Suggested strategies:")
    for strategy in ta.suggested_strategies:
        print(f"     • {strategy}")
    print()
    
    print("3. MCP TOOL ORCHESTRATION")
    print("-" * 60)
    orch = result.orchestration_result
    print(f"   Selected tools: {', '.join(orch['selected_tools'])}")
    print(f"   Success rate: {orch['success_rate']:.2%}")
    print(f"   Total execution time: {orch['total_execution_time']:.4f}s")
    print()
    
    print("4. STRATEGIC CONVERSION")
    print("-" * 60)
    sc = result.strategic_conversion
    print(f"   Weaknesses identified: {sc['total_weaknesses']}")
    print(f"   Advantages generated: {sc['total_advantages']}")
    print(f"   Conversion confidence: {sc['conversion_confidence']:.2%}")
    print()
    for conversion in sc['conversions']:
        print(f"   Weakness: {conversion['weakness']}")
        print(f"   → Advantage: {conversion['advantage']}")
        print(f"   → Strategy: {conversion['strategy']}")
        print()
    
    # Test zero-shot generalization
    print("=" * 60)
    print("ZERO-SHOT GENERALIZATION TEST")
    print("=" * 60)
    print()
    
    query_embedding = np.random.rand(embedding_dim)
    task_context = {
        "task": "object_manipulation",
        "environment": "outdoor",
        "object_type": "unknown"
    }
    
    gen_result = soma.adaptive_generalization(query_embedding, task_context)
    
    print(f"Similar experiences found: {gen_result['similar_experiences_found']}")
    print(f"Generalization confidence: {gen_result['generalization_confidence']:.2%}")
    print()
    print("Pattern analysis:")
    pa = gen_result['pattern_analysis']
    print(f"  - Total experiences: {pa['total_experiences']}")
    print(f"  - Success rate: {pa['success_rate']:.2%}")
    print()
    print("Recommendations:")
    for rec in gen_result['recommendations']:
        print(f"  • {rec}")
    print()
    
    # Get comprehensive summary
    print("=" * 60)
    print("COMPREHENSIVE SYSTEM SUMMARY")
    print("=" * 60)
    print()
    
    summary = soma.get_comprehensive_summary()
    
    print("Eyes (Memory-Augmented RAG):")
    print(f"  - Total experiences: {summary['eyes']['total_experiences']}")
    print(f"  - Failure experiences: {summary['eyes']['failure_experiences']}")
    print()
    
    print("Brain (Strategic LLM):")
    brain_summary = summary['brain']
    if 'total_attributions' in brain_summary:
        print(f"  - Total attributions: {brain_summary['total_attributions']}")
        print(f"  - Average confidence: {brain_summary['average_confidence']:.2%}")
    print()
    
    print("MCP Tools:")
    mcp_summary = summary['mcp_tools']
    if 'total_executions' in mcp_summary:
        print(f"  - Total executions: {mcp_summary['total_executions']}")
        print(f"  - Overall success rate: {mcp_summary['overall_success_rate']:.2%}")
    print()
    
    print("Overall Performance:")
    overall = summary['overall']
    print(f"  - Total orchestrations: {overall['total_orchestrations']}")
    print(f"  - Success rate: {overall['success_rate']:.2%}")
    print(f"  - Avg conversion confidence: {overall['average_conversion_confidence']:.2%}")
    print()
    
    print("=" * 60)
    print("SOMA orchestration completed successfully! ✓")
    print("=" * 60)


if __name__ == "__main__":
    main()
