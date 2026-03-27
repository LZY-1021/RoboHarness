<div align="center">
  <h1>SOMA: Strategic Orchestration and Memory-Augmented System for Vision-Language-Action Model Robustness via In-Context Adaptation</h1>
  
  <p>
    <a href="https://arxiv.org/abs/2603.24060"><img src="https://img.shields.io/badge/Paper-arXiv%20-red.svg" alt="Paper"></a>
    <a href="https://lzy-1021.github.io/SOMA/"><img src="https://img.shields.io/badge/Page-SOMA%20-blue.svg" alt="Paper"></a>
    <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License"></a>
  </p>

  <p><i>SOMA upgrades frozen Vision-Language-Action (VLA) policies for robust in-context adaptation without parameter fine-tuning, via contrastive Dual-Memory RAG, an attribution-driven LLM orchestrator, dynamic MCP interventions, and offline memory consolidation.</i></p>
  <p><i>Across <b>LIBERO-PRO</b> and <b>LIBERO-SOMA</b>, SOMA delivers an average absolute success-rate gain of <b>56.6%</b>, including a <b>89.1%</b> absolute improvement on long-horizon task chaining.</i></p>
</div>

<br/>

## 🚀 Highlights & Demos

### 🎥 SOMA FrameWork (VLM RAG & Visual Intervention)
*Here, we demonstrate how SOMA preceive visual imput and retrival historical experience to handle iamge/task prompt without requiring VLA fine-tuning, leading to a higher success rate.*

<div align="center">
  <img src="docs/framework.jpg" alt="SOMA Framework" width="800"/>
  <br/>
  <p><sub><b>Figure 1:</b> SOMA Framework.</sub></p>
</div>

### 📊 SOMA Generalization Performance
*Our Experiments are based on LIBERO Benchmark, we modified LIBERO to create our own benchmark named LIBERO-SOMA to test our SOMA with the baseline VLA policy compared to frozen VLA policy.*
"We also utilize a portion of the LIBERO-PRO benchmark to evaluate the performance of our SOMA on position and task-related challenges."

<div align="center">
  <table style="width:100%; text-align:center; vertical-align: middle;">
    <tr>
      <th width="12%">🧰 MCP Tool</th>
      <th width="22%">🗣️ Task Prompt</th>
      <th width="22%">🖼️ Origin Image</th>
      <th width="22%">🛠️ Modified Image</th>
      <th width="22%">🎬 Success Output</th>
    </tr>
    <tr>
      <td><b>Visual Overlay</b></td>
      <td><i>"Pick the red bowl from center of the cross formation and place it on the plate"</i></td>
      <td><img src="docs/visual/original.jpg" alt="Origin" width="100%"/></td>
      <td><img src="docs/visual/modified.jpg" alt="Modified" width="100%"/></td>
      <td><video src="https://github.com/user-attachments/assets/88531590-1b4b-43a0-bf23-ff3958561c04" width="100%" autoplay loop muted playsinline></video></td>
    </tr>
    <tr>
      <td><b>Distractor Remove</b></td>
      <td><i>"Pick the black bowl from left of the cross formation and place it on the plate"</i></td>
      <td><img src="docs/distractor/original.jpg" alt="Origin" width="100%"/></td>
      <td><img src="docs/distractor/modified.jpg" alt="Modified" width="100%"/></td>
      <td><video src="https://github.com/user-attachments/assets/676b413f-d165-4454-9cf3-e68fce8ba1ae" width="100%" autoplay loop muted playsinline></video></td>
    </tr>
  </table>
  <table style="width:100%; text-align:center; vertical-align: middle;">
    <tr>
      <th width="12%">🧰 MCP Tool</th>
      <th width="22%">🗣️ Task Prompt</th>
      <th width="22%">🛠️ Modified Prompt</th>
      <th width="22%">🖼️ Origin Image</th>
      <th width="22%">🎬 Success Output</th>
    </tr>
    <tr>
      <td><b>Prompt Simplify</b></td>
      <td><i>"Hey, umm... look down there. Can you grab that bottle? You know, the one for fries? Yeah, put it in the basket."</i></td>
      <td><i>"Pick the red sauce bottle and place it in the basket"</i></td>
      <td><img src="docs/noisy-prompt/original.jpg" alt="Origin" width="100%"/></td>
      <td><video src="https://github.com/user-attachments/assets/b8b34fd3-c33a-41af-899b-1d8c25e7ac75" width="100%" autoplay loop muted playsinline></video></td>
    </tr>
    <tr>
      <td><b>Task Decompose</b></td>
      <td><i>"Sort the items: milk and cream cheese into the basket"</i></td>
      <td align="left">
        <b>[SubTask-1]</b> <i>"Pick the milk and place it in the basket."</i><br/>
        <b>[SubTask-2]</b> <i>"Pick the cream cheese and place it in the basket."</i>
      </td>
      <td><img src="docs/long-task/original.jpg" alt="Origin" width="100%"/></td>
      <td><video src="https://github.com/user-attachments/assets/432ad762-ad57-4fd9-96cf-44e0e4b6854c" width="100%" autoplay loop muted playsinline></video></td>
    </tr>
  </table>
</div>

<details>
<summary><b>🔥 Click to see more Experiment Results</b></summary>
<br/>

<div align="center">
  <sub>
    <b>Benchmark Scope</b>:
    <code>LIBERO-SOMA + LIBERO-PRO</code>
    <code>Backbones: π₀, π₀.₅, SmolVLA</code>
    <code>Zero-shot In-Context Adaptation</code>
  </sub><br/>
  <sub>
    <b>Tags</b>: 
    <code>OOD-Generalization</code> 
    <code>Dual-Memory RAG</code> 
    <code>Tool-Orchestrated Adaptation</code>
  </sub>
</div>

<br/>

<div style="overflow-x:auto; border:1px solid #d0d7de; border-radius:12px; padding:10px;">
<table>
  <thead>
    <tr>
      <th>Quick Glance KPI</th>
      <th>Baseline</th>
      <th>SOMA</th>
      <th>Gain</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>LIBERO-PRO Avg (Pos)</td><td>2.33%</td><td><b>57.2%</b></td><td><b>+54.87%</b></td></tr>
    <tr><td>LIBERO-PRO Avg (Task)</td><td>0.86%</td><td><b>55.2%</b></td><td><b>+54.34%</b></td></tr>
    <tr><td>Dual-Memory Avg Turns</td><td>7.40 (No Memory)</td><td><b>1.07</b></td><td><b>-85.5%</b></td></tr>
  </tbody>
</table>
</div>

<br/>

### 📊 LIBERO-SOMA (OOD Challenge Suite)

<div align="center">
  <img src="docs/result.png" alt="LIBERO-SOMA Results" width="90%" style="border:1px solid #d0d7de; border-radius:12px; box-shadow:0 6px 18px rgba(31,35,40,0.12);"/>
  <br/>
  <sub><b>Figure:</b> Main performance comparison across visual, linguistic, and long-horizon OOD challenges.</sub>
</div>

<p>
<b>SOMA consistently reduces sensitivity to sensory noise, linguistic ambiguity, execution instability, and long-horizon error accumulation</b>, restoring robust performance across major OOD failure modes.
</p>

<br/>

### 📊 LIBERO-PRO (Position / Task Shifts, π₀.₅)

<div style="overflow-x:auto; border:1px solid #d0d7de; border-radius:12px; padding:8px;">
<table>
  <thead>
    <tr>
      <th colspan="4" align="left"><b>LIBERO-PRO (Pos)</b></th>
    </tr>
    <tr>
      <th>Category</th>
      <th>Task (Symbolic Form)</th>
      <th>π₀.₅ BASE</th>
      <th>w/ SOMA</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>Spat.</td><td>P.(btw(p, r), pl.)</td><td>2%</td><td><b>63.0%</b></td></tr>
    <tr><td>Spat.</td><td>P.(center, pl.)</td><td>0%</td><td><b>97.0%</b></td></tr>
    <tr><td>Spat.</td><td>P.(drw_top(cab_w), pl.)</td><td>0%</td><td><b>20.2%</b></td></tr>
    <tr><td>Spat.</td><td>P.(next_to(p), pl.)</td><td>0%</td><td><b>57.0%</b></td></tr>
    <tr><td>Spat.</td><td>P.(next_to(r), pl.)</td><td>12%</td><td><b>71.0%</b></td></tr>
    <tr><td>Obj.</td><td>P.(soup, bskt.)</td><td>0%</td><td><b>35.0%</b></td></tr>
    <tr><td><b>Average (Pos)</b></td><td>—</td><td>2.33%</td><td><b>57.2%</b></td></tr>
  </tbody>
</table>
</div>

<br/>

<div style="overflow-x:auto; border:1px solid #d0d7de; border-radius:12px; padding:8px;">
<table>
  <thead>
    <tr>
      <th colspan="4" align="left"><b>LIBERO-PRO (Task)</b></th>
    </tr>
    <tr>
      <th>Category</th>
      <th>Task (Symbolic Form)</th>
      <th>π₀.₅ BASE</th>
      <th>w/ SOMA</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>Spat.</td><td>P.(btw(p, r), pl.)</td><td>0%</td><td><b>78.0%</b></td></tr>
    <tr><td>Spat.</td><td>P.(center, pl.)</td><td>2%</td><td><b>82.0%</b></td></tr>
    <tr><td>Spat.</td><td>P.(next_to(ck.), pl.)</td><td>2%</td><td><b>97.0%</b></td></tr>
    <tr><td>Spat.</td><td>P.(next_to(p), pl.)</td><td>0%</td><td><b>73.0%</b></td></tr>
    <tr><td>Spat.</td><td>P.(next_to(r), pl.)</td><td>2%</td><td><b>98.0%</b></td></tr>
    <tr><td>Spat.</td><td>P.(on(ck.), pl.)</td><td>0%</td><td><b>12.0%</b></td></tr>
    <tr><td>Spat.</td><td>P.(on(r), pl.)</td><td>2%</td><td><b>100.0%</b></td></tr>
    <tr><td>Spat.</td><td>P.(on(stove), pl.)</td><td>0%</td><td><b>13.0%</b></td></tr>
    <tr><td>Spat.</td><td>P.(on(cab_w), pl.)</td><td>0%</td><td><b>95.0%</b></td></tr>
    <tr><td>Obj.</td><td>P.(soup, bskt.)</td><td>0%</td><td><b>16.0%</b></td></tr>
    <tr><td>Obj.</td><td>P.(bbq, bskt.)</td><td>2%</td><td><b>32.0%</b></td></tr>
    <tr><td>Obj.</td><td>P.(juice, bskt.)</td><td>2%</td><td><b>41.0%</b></td></tr>
    <tr><td>Obj.</td><td>P.(dressing, bskt.)</td><td>0%</td><td><b>13.0%</b></td></tr>
    <tr><td>Obj.</td><td>P.(tomato, bskt.)</td><td>0%</td><td><b>23.0%</b></td></tr>
    <tr><td><b>Average (Task)</b></td><td>—</td><td>0.86%</td><td><b>55.2%</b></td></tr>
  </tbody>
</table>
</div>

<p>
<b>SOMA substantially improves spatial grounding and compositional generalization under layout and semantic shifts</b>, lifting near-zero baseline performance to strong OOD robustness without fine-tuning.
</p>

<hr/>

### 🔍 Ablation Study

#### 🧠 Dual-Memory Ablation (Reasoning Efficiency)

<div align="center">
  <img src="docs/ablation_dual_memory.png" alt="Dual-Memory Ablation" width="70%" style="border:1px solid #d0d7de; border-radius:12px; box-shadow:0 6px 18px rgba(31,35,40,0.12);"/>
</div>

<div style="overflow-x:auto; border:1px solid #d0d7de; border-radius:12px; padding:8px;">

<table>
  <thead>
    <tr>
      <th>Memory Setting</th>
      <th>Avg. Turns-to-Success</th>
      <th>First-Turn Score</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>No Memory</td><td>7.40</td><td>60.0</td></tr>
    <tr><td>Failure Only</td><td>7.33</td><td>73.75</td></tr>
    <tr><td>Success Only</td><td>1.47</td><td>91.07</td></tr>
    <tr><td><b>SOMA (Dual)</b></td><td><b>1.07</b></td><td><b>96.3</b></td></tr>
  </tbody>
</table>

</div>

<p>
<b>Dual-memory retrieval (success + failure) provides stable, low-cost intervention planning</b>, minimizing reasoning rounds while maximizing first-turn decision reliability.
</p>

<br/>

#### 🧩 Dual-Stage Memory Consolidation (RAG Richness)

<div align="center">
  <img src="docs/ablation2.png" alt="Reasoning Depth Scores" width="65%" style="border:1px solid #d0d7de; border-radius:12px; box-shadow:0 6px 18px rgba(31,35,40,0.12);"/>
</div>

<div style="overflow-x:auto; border:1px solid #d0d7de; border-radius:12px; padding:8px;">

<table>
  <thead>
    <tr>
      <th>RAG Config</th>
      <th>Key Reasoning & Actions</th>
      <th>Success Rate</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>No-RAG</td><td>Ambiguous ID, shadow errors, simple highlighting</td><td>19.2%</td></tr>
    <tr><td>Limited-RAG</td><td>Failure guidance + redundant background replacement</td><td>48.8%</td></tr>
    <tr><td><b>Rich-RAG (SOMA)</b></td><td><b>Precise failure-aware distractor removal, clean strategy</b></td><td><b>60.1%</b></td></tr>
  </tbody>
</table>

</div>

<p>
<b>Rich RAG (SOMA’s dual-stage consolidation) delivers sharper causal reasoning, shorter tool chains, and higher success</b> than No-RAG / Limited-RAG baselines.
</p>

</details>


<br/>

---

## 📖 Evaluation Guide

**SOMA** is a framework that decouples high-level Vision-Language Models (VLMs) from low-level continuous control policies. By utilizing a Client-Server (CS) architecture for heavy visual foundations (like SAM3), SOMA provides robotic agents with dynamic perceptual interventions, automatic rollback (Encore) mechanisms, and multi-stage task chaining capabilities—all while maintaining high-frequency execution in the primary control loop.

This guide details how to run policy evaluations using the SOMA framework within the LeRobot environment.

## 0. Quick Start

### 0.1 Start SAM3 Service (In a separate terminal)
To ensure high-frequency control, the heavy vision model runs as an independent HTTP service.
```bash
python /path/to/sam3_service.py \
  --host 0.0.0.0 \
  --port 5001 \
  --device cuda \
  --sam3_weight_path /path/to/sam/sam3.pt
```

**Health Check:**
```bash
curl [http://127.0.0.1:5001/health](http://127.0.0.1:5001/health) | cat
```

### 0.2 Register LIBERO Tasks (`SOMA/libero-modified`)
Copy the `libero_soma` tasks located in `bddl_files` and `init_files` into your local LIBERO repository. Afterward, replace the contents of the `benchmark` folder to register the `libero_soma` tasks.

If you need to generate init states for new BDDL task files:
```bash
python sample_init_states.py \
  --bddl_file /path/to/bddl_files/libero_soma/soma_xxx_challenge.bddl \
  --save_path /path/to/init_files/libero_soma/soma_xxx_challenge.init
```

### 0.3 Run Inference / Evaluation Entry Point (`soma_eval.py`)
```bash
export SOMA_SAM3_URL=[http://127.0.0.1:5001](http://127.0.0.1:5001)
# Optional: Enable memory if you already have a populated memory database
export SOMA_ENABLE_MEMORY=0

python soma_eval.py \
  --policy.path=/path/to/pretrained_model \
  --env.type=libero \
  --env.task=libero_soma \
  --eval.batch_size=1 \
  --eval.n_episodes=10 \
  --rename_map="{'agentview_image':'observation.images.empty_camera_0'}" # pi05/smolvla/pi0 need to rename
```

---

## 1. Directory Structure & File Descriptions

### 1.1 Inference Entry & Core Glue
- **`soma_eval.py`**
  - **Entry Script**: Initializes the environment, policy, pre/post-processors, and SOMA perception.
  - Inside the rollout loop:
    - Periodically calls `PerceptionModule.process_frame()` to obtain `processed_img`, `refined_task`, and `control_flags`.
    - Writes `processed_img` back into `observation[visual_key]` (Visual input for the policy).
    - Injects `refined_task` via `add_envs_task(..., task_desc=...)` (Text input for the policy).
    - Consumes `control_flags` to execute control flow maneuvers:
      - `encore`: Rollback / Kinematic reset.
      - `key_step_retry`: Redo key steps (triggered by historical success step thresholds).
      - `task_decompose`: Subtask decomposition (Reset before advancing to the next task).

- **`soma_control_flow.py`**
  - Control flow state machine implementations:
    - `RollbackState`: Action executor for reverse and buffer phases.
    - `TaskDecomposeState`: Subtask list and index management.
    - `KeyStepRetryState`: Retains control flow parameters (Currently triggered in `soma_eval.py` using `success_max_step/key_frame_start` from memory).

### 1.2 Online Orchestrator
- **`soma_perception.py`**
  - `PerceptionModule`: The online cognitive orchestrator.
  - **Input**: `image(HWC uint8) + current_task + step + rag_context(optional)`
  - **Output**: `processed_image + refined_task + control_flags`
  - **Internal Workflow**:
    1. Calls `orchestrate_perception()` in `soma_vlm.py` to receive a JSON plan (`tool_chain`, `params`, `refined_task`, `task_plan`).
    2. Routes visual tools to `soma_tools.py` (HTTP requests to the SAM3 service).
    3. Outputs `control_flags` for control flow tools (handled by the state machine in `soma_eval.py`).

### 1.3 MCP Tools (Visual Tools via SAM3 Service)
- **`soma_tools.py`**
  - `MCPTools`: The visual MCP client (**Does NOT load SAM3 locally**).
  - Invokes `sam3_service.py` via `Sam3HttpClient`:
    - `visual_overlay`: Highlights target objects.
    - `remove_distractor`: Erases distracting elements (inpainting).
    - `replace_texture`: Replaces object textures (for similar-object substitution).
    - `replace_background`: Replaces background environments (floor/table textures).

- **`sam3_service.py`**
  - A Flask backend hosting the heavy SAM3 model.
  - Exposes an HTTP API: accepts base64 PNGs and returns processed base64 PNGs.
  - Endpoints: `GET /health`, `POST /visual_overlay`, `POST /remove_distractor`, `POST /replace_texture`, `POST /replace_background`.

### 1.4 VLM (Strategic Planning)
- **`soma_vlm.py`**
  - `Qwen3VLAPIClient`
  - Core functions:
    - `orchestrate_perception(...)`: Outputs strict JSON tool-chain plans.
    - `generate_failure_report(...)`: Generates failure attribution reports during post-episode reviews (used by the logger).
    - `generate_success_description(...)`: Generates execution summaries for successful episodes.

Required Environment Variables:
```bash
export SOMA_VLM_API_KEY="sk-xxx"
export SOMA_VLM_BASE_URL="https://xxx.com/api/v1"
export SOMA_VLM_MODEL="..."
```

### 1.5 Memory / Encoder / Logger
- **`soma_encoder.py`**: `AdvancedEmbeddingEncoder` (CLIP vision vector + Text vector + Hash concatenation) for RAG retrieval and experience vectorization.
- **`soma_memory.py`**: `MemoryBank` (Local vector database partitioned by success/failure). Stores `metadata.jsonl` and `vectors.npy`. Retrieves control flow statistics (e.g., rollback steps, success max steps) via `info.task_plan`.
- **`soma_logger.py`**: `ExperienceLogger` samples video keyframes, calls VLM for attribution, generates embeddings, and saves to memory.
- **`soma_agent.py`**: A Facade class that encapsulates VLM, Encoder, Memory, Perception, and Logger into a unified object.

### 1.6 Testing Scripts
- **`test_sam3_mcp_tools.py`**: Minimum Viable Test (MVT) script. Verifies end-to-end execution of the 4 visual tools between `sam3_service` and `MCPTools`, outputting debug images.

---

## 2. Pipeline Data Flow

Critical execution path for a single step:

1. `env.step()` → Returns `observation`.
2. `preprocess_observation(observation)` → Normalizes to PyTorch tensors.
3. Every $N$ steps (default 10), trigger perception:
   - Extract visual key (contains `image` or `rgb`).
   - Tensor → uint8 HWC → `PerceptionModule.process_frame(...)`.
   - Returns `processed_img`, `refined_task`, and `control_flags`.
   - Overwrite `observation[visual_key]` with `processed_img`.
4. `add_envs_task(..., task_desc=refined_task)` → Injects refined text prompt.
5. `preprocessor(observation)` → Aligns device tensors and handles renaming.
6. `policy.select_action(observation)` → Outputs action predictions.
7. `postprocessor(action)` → Post-processes the action.
8. `env.step(action_numpy)` → Steps the physical/simulated environment.
9. `soma_eval.py` consumes `control_flags` to execute control flows (rollback, task switch, or key step retries).

---

## 3. Control Flow MCP Tools (Non-SAM3) Current Implementation

### 3.1 `encore`
- **Semantics**: Immediate request for a kinematic rollback/reset.
- **Execution**: `soma_eval.py` sums the current accumulated actions and reverses the trajectory (`reverse_steps` + `buffer_steps`).

### 3.2 `key_step_retry`
- **Semantics**: If the current step exceeds the historical `success_max_step` without succeeding, rollback to the keyframe starting point.
- **Trigger Source**: Extracted from memory via `info.task_plan.success_max_step`.
- **Rollback Window**: `sum(action_hist[key_frame_start : now])`.
- **Execution**: Calculates `reverse_action = -window_sum / reverse_steps`, executes for `reverse_steps`, and follows up with stabilization buffer steps.

### 3.3 `task_decompose`
- **Semantics**: Decomposes long-horizon tasks into a sequential list of `subtasks`.
- **Progression Logic**: Advances on `success_any=True`, but **forces a kinematic reset** before moving to the next subtask.
- **Rollback Window**: `sum(action_hist[subtask_start_step : now])`.
- **Execution Sequence**:
  1. Execute reverse + buffer.
  2. Increment `subtask_idx += 1`.
  3. Update `subtask_start_step`.

---

## 4. Dependencies & Installation

**Minimal Dependencies (Inference Side):**
- `numpy`, `torch`, `Pillow`, `requests`, `gymnasium`, `einops`, `tqdm`

**SAM3 Server Additional Dependencies:**
- `flask`, `flask_cors`, `sam3` (via your specific SAM3 installation method)

**VLM Additional Dependencies:**
- `openai` (Compatible with OpenAI API format services)
- Network-accessible VLM endpoint

---

## 5. Visual MCP Tools Quick Validation
```bash
python test_sam3_mcp_tools.py \
  --sam3_url [http://127.0.0.1:5001](http://127.0.0.1:5001) \
  --image path/to/xxx.png \
  --target "ketchup" \
  --distractor "tomato sauce" \
  --floor_prompt "floor" \
  --texture path/to/xxx_texture.png \
  --out_dir path/to/output_dir
```

The output directory will contain:
- `0_input.png`
- `1_overlay.png`
- `2_remove_distractor.png`
- `3_replace_texture.png`
- `4_replace_background.png`

---

## 6. Visual MCP Tools Attention-Score Heatmap Evaluation
```bash
python image_attn_map.py \
  --attn_raw_img "/path/to/original.jpg" \
  --attn_soma_img "/path/to/modified.jpg" \
  --attn_raw_task "Pick up the bowl on the far right of the cross formation and place it on the plate." \
  --attn_soma_task "Pick up the green bowl and place it on the plate." \
  --policy.path=/path/to/pretrained_model \  
  --env.type=libero \   
  --env.task=libero_soma \  
  --eval.batch_size=1 \ 
  --eval.n_episodes=10 \
  --rename_map="{'agentview_image':'observation.images.empty_camera_0'}" 
```

The output directory (`output_dir/soma_debug_dir`) will contain A/B testing visual comparisons:
- `attn_step_000_compare.jpg`
- `attn_step_010_compare.jpg`
- `attn_step_020_compare.jpg`
- `attn_step_030_compare.jpg`
...

---

## 7. Multi-Stage Task Chain Evaluation

This pipeline evaluates a policy's performance on **long-horizon tasks** by decomposing them into a sequential chain of subtasks. The agent automatically transitions to the next subtask upon reaching the step limit, utilizing the **Task-Switch Encore** mechanism to reset the kinematic pose and clear accumulated errors between stages.

### Task Configuration
You can define the sequence of subtasks by editing the `TASK_CHAIN` list in `eval_chain_step.py` (around line 715):

```python
# Example Task Chain Configuration
TASK_CHAIN = [
    {"desc": "Pick up the cream cheese and place it in the basket.", "max_steps": 280},
    {"desc": "Pick up the milk and place it in the basket.", "max_steps": 280},
    {"desc": "Pick up the chocolate pudding and place it on the plate.", "max_steps": 300},
]
```
### Evaluation
Run the evaluation with the following command. You can optionally enable the SOMA agent to provide perceptual interventions for each subtask:
```bash
python eval_chain_step.py \
  --policy.path=/path/to/pretrained_model \
  --env.type=libero \
  --env.task=libero_soma \
  --eval.batch_size=1 \
  --eval.n_episodes=1 \
  --rename_map="{'agentview_image':'observation.images.empty_camera_0'}"
```

---

## 8. FAQ & Troubleshooting

- **I don't see any output images**
  - Verify that the `--out_dir` path is correct and accessible.
  - Run `ls -lah <out_dir>` to check directory permissions.
- **Visual tools have no effect, but HTTP returns 200 OK**
  - This usually indicates a prompt mismatch (the segmentation mask is empty).
  - Try calling `.strip()` on your prompts, or use more generalized nouns like `bottle`, `floor`, or `table`.
- **VLM API is unavailable/failing**
  - You can temporarily hardcode `tool_chain=[]` in the perception module to bypass the VLM and run standard evaluations without orchestration.
- **I can't tell if the Control Flow is triggering**
  - Check your terminal logs for `[CTRL] Rollback start reason=...` and watch the `tqdm` progress bar postfix for `rollback=True/False`.

---

## 9.Core CLI Arguments Reference (SOMA Extensions)
All SOMA-enhanced evaluation scripts support the following dynamic command-line arguments. These parameters are injected into environment variables to ensure compatibility with LeRobot's core configuration system.
| Argument | Type | Description | Default |
| :--- | :--- | :--- | :--- |
| `--enable_soma` | Flag | Enables the SOMA Agent for dynamic perception and control. | Disabled |
| `--vlm_api_key` | str | API key for the Vision-Language Model provider. | `""` |
| `--vlm_base_url` | str | Base URL for the VLM API endpoint. | `""` |
| `--vlm_model_id` | str | Specific Model ID (e.g., qwen3-vl-32b-instruct). | `""` |
| `--attn_raw_img` | str | (Viz Only) Path to the raw environment observation. | `""` |
| `--attn_soma_img` | str | (Viz Only) Path to the SOMA-modified observation. | `""` |
| `--attn_raw_task` | str | (Viz Only) Original base task description. | `""` |
| `--attn_soma_task` | str | (Viz Only) Refined task description generated by SOMA. | `""` |

---

## 10.Repository Structure
```Plaintext
SOMA/
├── libero-modified/                  # Modified LIBERO simulation environment
│   ├── bddl_files/libero_soma/       # BDDL task definitions for SOMA challenges
│   │   ├── soma_chain_step_challenge.bddl
│   │   ├── soma_distractor_challenge.bddl
│   │   └── ... (other task variants)
│   ├── benchmark/                    # Benchmark registration and task mapping
│   │   ├── _init_.py                 # Init file to register LIBERO benchmarks
│   │   ├── libero_suite_task_map.py  # Maps BDDL files to LIBERO benchmarks
│   │   └── mu_creation.py            # Environment setup and asset creation
│   ├── init_files/libero-soma/       # Pre-sampled initial states (.init) for tasks
│   │   ├── soma_chain_step_challenge.init
│   │   ├── soma_distractor_challenge.init
│   │   └── ... (other task variants)
│   └── sample_init_states.py         # Script to generate initial state files
├── src/                              # Core SOMA Framework Source Code
│   ├── outputs/                      
│   ├── chain_step_eval.py            # Eval pipeline for multi-stage sequential tasks
│   ├── image_attn_map.py             # Script for VLA attention weight visualization
│   ├── RAG_ablation_study.py         # Script for testing memory bank impact
│   ├── sam3_service.py               # Flask server hosting the SAM3 vision model
│   ├── soma_agent.py                 # Unified facade for the SOMA cognitive agent
│   ├── soma_control_flow.py          # State machine for Rollback/Encore/Decomposition
│   ├── soma_encoder.py               # Multimodal embedding generator (CLIP + Text)
│   ├── soma_eval.py                  # Primary evaluation entry point for SOMA
│   ├── soma_logger.py                # Automated experience recording and diagnosis
│   ├── soma_memory.py                # Persistent vector database for episodic memory
│   ├── soma_perception.py            # Strategic orchestrator for VLM perception loop
│   ├── soma_tools.py                 # Client for visual MCP tools (SAM3 HTTP calls)
│   ├── soma_vlm.py                   # Client for Vision-Language Model reasoning
│   └── test_sam3_mcp_tools.py        # Standalone verification for visual tools
└── README.md                         # Project documentation and usage guide
```
---




# Acknowledgements

This repository builds upon and extends the excellent open-source ecosystems of **LIBERO-PRO** and **LeRobot**.  
We sincerely thank the original authors and maintainers for their foundational contributions.

- **LIBERO-PRO**: robust and fair evaluation beyond memorization for VLA models.  
- **LeRobot**: open-source infrastructure for end-to-end robot learning.

---

<!-- # Citation

If you find this repository useful, please cite **SOMA** and the upstream projects below:

```bibtex
@misc{li2026somastrategicorchestrationmemoryaugmented,
      title={SOMA: Strategic Orchestration and Memory-Augmented System for Vision-Language-Action Model Robustness via In-Context Adaptation}, 
      author={Zhuoran Li and Zhiyang Li and Kaijun Zhou and Jinyu Gu},
      year={2026},
      eprint={2603.24060},
      archivePrefix={arXiv},
      primaryClass={cs.RO},
      url={https://arxiv.org/abs/2603.24060}, 
}

@misc{zhou2025liberoprorobustfairevaluation,
  title={LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization},
  author={Xueyang Zhou and Yangming Xu and Guiyao Tie and Yongchao Chen and Guowen Zhang and Duanfeng Chu and Pan Zhou and Lichao Sun},
  year={2025},
  eprint={2510.03827},
  archivePrefix={arXiv},
  primaryClass={cs.CV},
  url={https://arxiv.org/abs/2510.03827}
}

@inproceedings{cadenelerobot,
  title={LeRobot: An Open-Source Library for End-to-End Robot Learning},
  author={Cadene, Remi and Alibert, Simon and Capuano, Francesco and Aractingi, Michel and Zouitine, Adil and Kooijmans, Pepijn and Choghari, Jade and Russi, Martino and Pascal, Caroline and Palma, Steven and Shukor, Mustafa and Moss, Jess and Soare, Alexander and Aubakirova, Dana and Lhoest, Quentin and Gallou{'}edec, Quentin and Wolf, Thomas},
  booktitle={The Fourteenth International Conference on Learning Representations},
  year={2026},
  url={https://arxiv.org/abs/2602.22818}
}
```

--- -->

<!-- # License

| Component | License |
|---|---|
| Codebase | [MIT License](LICENSE) |

--- -->
