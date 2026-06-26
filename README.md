<div align="center">
  <h1>RoboHarness 🏇: A Memory-Augmented Policy Harness for Vision-Language-Action Model Robustness via In-Context Adaptation</h1>
  
  <p>
    <a href="https://arxiv.org/abs/2603.24060"><img src="https://img.shields.io/badge/Paper-arXiv%20-red.svg" alt="Paper"></a>
    <a href="https://lzy-1021.github.io/RoboHarness/"><img src="https://img.shields.io/badge/Page-RoboHarness%20-blue.svg" alt="Paper"></a>
    <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License"></a>
  </p>

  <p><i>RoboHarness is a memory-augmented policy harness that upgrades frozen Vision-Language-Action (VLA) policies for robust in-context adaptation without parameter fine-tuning, via contrastive Dual-Memory RAG, an attribution-driven vision-language orchestrator implemented with a multimodal large language model, dynamic MCP interventions, and offline memory consolidation.</i></p>
  <p><i>Across <b>LIBERO-PRO</b> and <b>LIBERO-RoboHarness</b>, RoboHarness delivers an average absolute success-rate gain of <b>56.6%</b>, including a <b>89.1%</b> absolute improvement on long-horizon task chaining.</i></p>
</div>

<br/>

## 🚀 Highlights & Demos

### 🎥 RoboHarness FrameWork (VLM RAG & Visual Intervention)
*Here, we demonstrate how RoboHarness preceive visual imput and retrival historical experience to handle iamge/task prompt without requiring VLA fine-tuning, leading to a higher success rate.*

<div align="center">
  <img src="docs/framework.jpg" alt="RoboHarness Framework" width="800"/>
  <br/>
  <p><sub><b>Figure 1:</b> RoboHarness Framework.</sub></p>
</div>

### 📊 RoboHarness Generalization Performance
*Our Experiments are based on LIBERO Benchmark, we modified LIBERO to create our own benchmark named LIBERO-RoboHarness to test our RoboHarness with the baseline VLA policy compared to frozen VLA policy.*
"We also utilize a portion of the LIBERO-PRO benchmark to evaluate the performance of our RoboHarness on position and task-related challenges."

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
    <code>LIBERO-RoboHarness + LIBERO-PRO</code>
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
      <th>RoboHarness</th>
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

### 📊 LIBERO-RoboHarness (OOD Challenge Suite)

<div align="center">
  <img src="docs/result.png" alt="LIBERO-RoboHarness Results" width="90%" style="border:1px solid #d0d7de; border-radius:12px; box-shadow:0 6px 18px rgba(31,35,40,0.12);"/>
  <br/>
  <sub><b>Figure:</b> Main performance comparison across visual, linguistic, and long-horizon OOD challenges.</sub>
</div>

<p>
<b>RoboHarness consistently reduces sensitivity to sensory noise, linguistic ambiguity, execution instability, and long-horizon error accumulation</b>, restoring robust performance across major OOD failure modes.
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
      <th>w/ RoboHarness</th>
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
      <th>w/ RoboHarness</th>
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
<b>RoboHarness substantially improves spatial grounding and compositional generalization under layout and semantic shifts</b>, lifting near-zero baseline performance to strong OOD robustness without fine-tuning.
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
    <tr><td><b>RoboHarness (Dual)</b></td><td><b>1.07</b></td><td><b>96.3</b></td></tr>
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
    <tr><td><b>Rich-RAG (RoboHarness)</b></td><td><b>Precise failure-aware distractor removal, clean strategy</b></td><td><b>60.1%</b></td></tr>
  </tbody>
</table>

</div>

<p>
<b>Rich RAG (RoboHarness’s dual-stage consolidation) delivers sharper causal reasoning, shorter tool chains, and higher success</b> than No-RAG / Limited-RAG baselines.
</p>

</details>


<br/>

---

## Repository Structure
```Plaintext
RoboHarness/
├── libero-modified/                  # Modified LIBERO simulation environment
│   ├── bddl_files/libero_roboharness/       # BDDL task definitions for RoboHarness challenges
│   │   ├── roboharness_chain_step_challenge.bddl
│   │   ├── roboharness_distractor_challenge.bddl
│   │   └── ... (other task variants)
│   ├── benchmark/                    # Benchmark registration and task mapping
│   │   ├── _init_.py                 # Init file to register LIBERO benchmarks
│   │   ├── libero_suite_task_map.py  # Maps BDDL files to LIBERO benchmarks
│   │   └── mu_creation.py            # Environment setup and asset creation
│   ├── init_files/libero-roboharness/       # Pre-sampled initial states (.init) for tasks
│   │   ├── roboharness_chain_step_challenge.init
│   │   ├── roboharness_distractor_challenge.init
│   │   └── ... (other task variants)
│   └── sample_init_states.py         # Script to generate initial state files
├── src/                              # Core RoboHarness Framework Source Code
│   ├── outputs/                      
│   ├── chain_step_eval.py            # Eval pipeline for multi-stage sequential tasks
│   ├── image_attn_map.py             # Script for VLA attention weight visualization
│   ├── RAG_ablation_study.py         # Script for testing memory bank impact
│   ├── sam3_service.py               # Flask server hosting the SAM3 vision model
│   ├── roboharness_agent.py                 # Unified facade for the RoboHarness cognitive agent
│   ├── roboharness_control_flow.py          # State machine for Rollback/Encore/Decomposition
│   ├── roboharness_encoder.py               # Multimodal embedding generator (CLIP + Text)
│   ├── roboharness_eval.py                  # Primary evaluation entry point for RoboHarness
│   ├── roboharness_logger.py                # Automated experience recording and diagnosis
│   ├── roboharness_memory.py                # Persistent vector database for episodic memory
│   ├── roboharness_perception.py            # Strategic orchestrator for VLM perception loop
│   ├── roboharness_tools.py                 # Client for visual MCP tools (SAM3 HTTP calls)
│   ├── roboharness_vlm.py                   # Client for Vision-Language Model reasoning
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

# Citation

If you find this repository useful, please cite **RoboHarness** and the upstream projects below:

```bibtex
@misc{li2026roboharnessmemoryaugmentedpolicyharness,
      title={RoboHarness 🏇: A Memory-Augmented Policy Harness for Vision-Language-Action Model Robustness via In-Context Adaptation},
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

---

# License

| Component | License |
|---|---|
| Codebase | [MIT License](LICENSE) |

---
