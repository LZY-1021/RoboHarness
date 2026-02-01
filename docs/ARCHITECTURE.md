# SOMA Architecture Documentation

## System Overview

SOMA (Strategic Orchestration and Memory-Augmented Agentic System) is designed for zero-shot VLA (Vision-Language-Action) generalization. It strategically converts identified model weaknesses into advantages through orchestrated tool chains.

## Core Components

### 1. Eyes (Memory-Augmented RAG)

**Purpose**: Provide contextual awareness through experience retrieval.

**Key Features**:
- Stores experience quintuples: (state, action, outcome, embedding, failure_attribution)
- Multimodal embedding-based retrieval
- Failure attribution tracking
- Cosine similarity search

**Data Structure**:
```python
ExperienceQuintuple(
    state: Dict[str, Any],
    action: Dict[str, Any],
    outcome: Dict[str, Any],
    embedding: np.ndarray,
    failure_attribution: Optional[Dict[str, Any]]
)
```

**API**:
- `store_experience(quintuple)`: Store new experience
- `retrieve_experiences(query_embedding, top_k)`: Retrieve similar experiences
- `get_contextual_awareness(query_embedding)`: Get comprehensive context

### 2. Brain (Strategic LLM)

**Purpose**: Perform theoretical attribution to diagnose root causes.

**Root Cause Types**:
- Causal Confusion
- Visual Bias
- Distributional Shift
- Spurious Correlation
- Overfitting/Underfitting

**Key Features**:
- Root cause diagnosis
- Weakness identification
- Strategic conversion (weaknesses → advantages)
- Strategy generation

**Data Structure**:
```python
TheoreticalAttribution(
    root_cause: RootCauseType,
    confidence: float,
    explanation: str,
    suggested_strategies: List[str],
    model_weaknesses: List[str],
    potential_advantages: List[str]
)
```

**API**:
- `diagnose_root_cause(context, failure_info)`: Diagnose failures
- `get_strategic_analysis()`: Get historical analysis

### 3. MCP Tools (Model Context Protocol)

**Purpose**: Provide dynamic tool chain for addressing issues.

**Available Tools**:
- **Domain Adaptation**: Handle distributional shifts
- **Causal Intervention**: Address causal confusion
- **Visual Augmentation**: Reduce visual biases
- **Counterfactual Reasoning**: Explore alternatives
- **Adversarial Robustness**: Build resilience

**Data Structure**:
```python
MCPToolResult(
    tool_type: MCPToolType,
    success: bool,
    output: Dict[str, Any],
    execution_time: float,
    metadata: Optional[Dict[str, Any]]
)
```

**API**:
- `select_tools(context, strategies)`: Select appropriate tools
- `execute_tool_chain(tools, input_data)`: Execute chain
- `orchestrate(context, strategies, input_data)`: Full orchestration

### 4. SOMA Orchestrator

**Purpose**: Main orchestration layer integrating all components.

**Orchestration Flow**:
```
1. Eyes: Retrieve contextual awareness
2. Brain: Diagnose root causes
3. Strategic Conversion: Convert weaknesses to advantages
4. MCP Orchestration: Execute tool chain
5. Result Synthesis: Compile results
```

**API**:
- `process_experience(...)`: Store new experience
- `orchestrate(query_embedding, context, failure_info)`: Main orchestration
- `adaptive_generalization(query_embedding, task_context)`: Zero-shot adaptation
- `get_comprehensive_summary()`: System performance summary

## Data Flow

```
Input (Query + Context)
    ↓
Eyes: Retrieve similar experiences
    ↓
Brain: Diagnose root causes
    ↓
Strategic Conversion: Weaknesses → Advantages
    ↓
MCP Tools: Execute adaptive chain
    ↓
Output (SOMAResult)
```

## Key Algorithms

### 1. Experience Retrieval (Eyes)

```python
def retrieve_experiences(query_embedding, top_k):
    # Compute cosine similarity
    similarities = cosine_similarity(query_embedding, all_embeddings)
    
    # Get top-k
    top_indices = argsort(similarities)[-top_k:]
    
    return [(experience[i], similarity[i]) for i in top_indices]
```

### 2. Root Cause Diagnosis (Brain)

```python
def diagnose_root_cause(context, failure_info):
    # Check causal confusion
    if check_causal_confusion(context, failure_info):
        return RootCauseType.CAUSAL_CONFUSION
    
    # Check visual bias
    if check_visual_bias(context, failure_info):
        return RootCauseType.VISUAL_BIAS
    
    # Check distributional shift
    if check_distributional_shift(context, failure_info):
        return RootCauseType.DISTRIBUTIONAL_SHIFT
    
    return RootCauseType.UNKNOWN
```

### 3. Strategic Conversion (Brain)

```python
def convert_weaknesses_to_advantages(weaknesses):
    advantages = []
    
    for weakness in weaknesses:
        # Identify opportunities in weaknesses
        if "correlation" in weakness:
            advantages.append("Pattern detection capability")
        elif "visual" in weakness:
            advantages.append("Visual feature sensitivity")
    
    return advantages
```

### 4. Tool Orchestration (MCP)

```python
def orchestrate(context, strategies, input_data):
    # Select appropriate tools
    tools = select_tools(context, strategies)
    
    # Execute chain
    results = []
    current_data = input_data
    
    for tool in tools:
        result = tool.execute(current_data)
        results.append(result)
        current_data.update(result.output)
    
    return compile_results(results)
```

## Extension Points

### Adding New Tools

```python
class CustomTool(MCPTool):
    def __init__(self):
        super().__init__(MCPToolType.CUSTOM)
    
    def execute(self, input_data):
        # Custom implementation
        return MCPToolResult(...)
    
    def can_handle(self, context):
        # Custom logic
        return True
```

### Custom Root Cause Detection

```python
# Extend RootCauseType enum
class RootCauseType(Enum):
    # ... existing types
    CUSTOM_CAUSE = "custom_cause"

# Add detection method in StrategicLLM
def _check_custom_cause(self, context, failure_info):
    # Custom detection logic
    return condition
```

## Performance Considerations

1. **Embedding Storage**: Uses NumPy arrays for efficient similarity computation
2. **Tool Execution**: Tools run sequentially with data passing
3. **Memory Management**: Experiences stored in-memory (consider persistence for production)
4. **Scalability**: Cosine similarity O(n) - consider approximate nearest neighbors for large scales

## Best Practices

1. **Experience Storage**: Store diverse experiences including failures
2. **Embedding Quality**: Use high-quality multimodal embeddings
3. **Tool Selection**: Ensure tools are relevant to diagnosed root causes
4. **Failure Attribution**: Provide detailed failure information for better diagnosis
5. **Monitoring**: Track orchestration success rates and tool performance

## Future Enhancements

1. Persistent storage for experience bank
2. Approximate nearest neighbor search for scalability
3. Advanced LLM integration for Brain component
4. Real-time learning and adaptation
5. Multi-agent orchestration capabilities
