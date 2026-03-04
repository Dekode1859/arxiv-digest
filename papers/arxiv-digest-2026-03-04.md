# arXiv AI Digest

**Generated:** 2026-03-04 at 18:10:37 

**Categories:** cs.AI, cs.LG, cs.CL, stat.ML

**Total Papers:** 10

---

### 1. 1. CFG-Ctrl: Control-Based Classifier-Free Diffusion Guidance

- **arXiv:** [2603.03281v1](https://arxiv.org/abs/2603.03281v1) | [PDF](https://arxiv.org/pdf/2603.03281v1)
- **Published:** ** 2026-03-03
- **Category:** method (generative_models)
- **Tags:** diffusion-models, classifier-free-guidance, CFG, flow-matching, control-theory, semantic-alignment, velocity-field, generative-flow

**Summary:**
This paper introduces CFG-Ctrl, a unified framework that reinterprets Classifier-Free Guidance (CFG) as a control mechanism applied to continuous-time flow-based diffusion models. The approach uses the difference between conditional and unconditional predictions as an error signal to adjust the velocity field, effectively treating CFG as a proportional controller.

**Implementation:**
['Reinterprets CFG as control applied to first-order continuous-time generative flow', 'Uses conditional-unconditional discrepancy as error signal to adjust velocity field', 'Frames vanilla CFG as proportional controller (P-control) with fixed gain', 'Unified framework for understanding and extending CFG methods']

**Applications:**
- Image generation with improved semantic control
- Text-to-image generation
- Controlled synthesis in diffusion models

---

### 2. 2. How to Peel with a Knife: Aligning Fine-Grained Manipulation with Human Preference

- **arXiv:** [2603.03280v1](https://arxiv.org/abs/2603.03280v1) | [PDF](https://arxiv.org/pdf/2603.03280v1)
- **Published:** ** 2026-03-03
- **Category:** method (robotics)
- **Tags:** fine-grained manipulation, human preference alignment, force-sensitive robotics, implicit success criteria, reward engineering, contact-rich dynamics, learning from human feedback

**Summary:**
This paper addresses challenging manipulation tasks like food preparation, surgery, and craftsmanship that require both contact-rich physical interactions and subjective quality evaluation. The authors present a learning framework that aligns robotic fine-grained manipulation with human preferences, enabling robots to perform tasks where success is continuous and subjective rather than binary.

**Implementation:**
The framework focuses on implicit success criteria that are difficult to evaluate quantitatively. It uses learning-based approaches to capture human preferences for quality assessment in force-sensitive, contact-rich manipulation tasks. The method likely involves reward learning or preference modeling to handle the continuous, subjective nature of task quality (e.g., how well a potato is peeled).

**Applications:**
- Food preparation and cooking automation
- Surgical robotics
- Craftsmanship and manufacturing
- Assembly tasks requiring fine motor control

---

### 3. 3. Tether: Autonomous Functional Play with Correspondence-Driven Trajectory Warping

- **arXiv:** [2603.03278v1](https://arxiv.org/abs/2603.03278v1) | [PDF](https://arxiv.org/pdf/2603.03278v1)
- **Published:** ** 2026-03-03
- **Category:** application (robotics)
- **Tags:** autonomous_learning, trajectory_planning, motion_control, reinforcement_learning, human_robot_interaction, play-based_learning, imitation_learning

**Summary:**
Tether is a robotics method for enabling autonomous functional play, where robots learn through structured, task-directed interaction. It addresses key challenges in robot learning by creating policies robust to diverse and out-of-distribution environment states, while also providing a continuous procedure for generating useful robot experience without requiring extensive human demonstrations.

**Implementation:**
Uses correspondence-driven trajectory warping to adapt learned behaviors to new situations. The method enables robots to conduct self-supervised learning through play, with a focus on functional interactions that are task-directed. It handles out-of-distribution environment states through robust policy design.

**Applications:**
- Robot skill learning through autonomous exploration
- Scalable robot training without human demonstrations
- Adaptive robotic manipulation in changing environments

---

### 4. 4. Learning Demographic-Conditioned Mobility Trajectories with Aggregate Supervision

- **arXiv:** [2603.03275v1](https://arxiv.org/abs/2603.03275v1) | [PDF](https://arxiv.org/pdf/2603.03275v1)
- **Published:** ** 2026-03-03
- **Category:** method (generative_models)
- **Tags:** mobility_trajectories, demographic_conditioning, weakly_supervised_learning, aggregate_supervision, trajectory_generation

**Summary:**
ATLAS is a weakly supervised machine learning approach that generates demographic-conditioned mobility trajectories without requiring explicit demographic labels on individual data. It uses aggregate supervision to learn how different demographic groups exhibit distinct mobility patterns, addressing the common problem of missing demographic labels in trajectory datasets.

**Implementation:**
Weakly supervised learning framework using aggregate (population-level) demographic information rather than individual-level labels. Conditions trajectory generation on demographic attributes to capture mobility heterogeneity across different population groups. Addresses data scarcity issue where individual trajectories lack demographic annotations.

**Applications:**
- Public health monitoring and disease spread modeling
- Urban planning and transportation infrastructure design
- Social science research on demographic behavior patterns
- Epidemiological studies tracking population movement

---

### 5. 5. Gravity Falls: A Comparative Analysis of Domain-Generation Algorithm (DGA) Detection Methods for Mobile Device Spearphishing

- **arXiv:** [2603.03270v1](https://arxiv.org/abs/2603.03270v1) | [PDF](https://arxiv.org/pdf/2603.03270v1)
- **Published:** ** 2026-03-03
- **Category:** benchmark (None)
- **Tags:** DGA detection, mobile security, smishing, phishing detection, cybersecurity, domain generation algorithms, spearphishing, malware detection, comparative analysis

**Summary:**
This paper evaluates how well Domain Generation Algorithm (DGA) detectors work for detecting smishing (SMS spearphishing) attacks on mobile devices, addressing a gap in research that primarily focuses on malware C2 and email phishing. The authors compare traditional and machine-learning based DGA detection methods to determine their effectiveness against mobile-specific domain tactics used by threat actors.

**Implementation:**
The study evaluates DGA detection methods against smishing-driven domain tactics outside enterprise perimeters. It compares traditional detection approaches with machine-learning based detectors to assess generalization capabilities. The research focuses on mobile device spearphishing scenarios where DGAs are used to rotate hostile infrastructure.

**Applications:**
- Mobile device security monitoring
- SMS/phishing threat detection
- Endpoint protection for mobile devices
- Threat intelligence for mobile-first security solutions

---

### 6. 6. LoGeR: Long-Context Geometric Reconstruction with Hybrid Memory

- **arXiv:** [2603.03269v1](https://arxiv.org/abs/2603.03269v1) | [PDF](https://arxiv.org/pdf/2603.03269v1)
- **Published:** ** 2026-03-03
- **Category:** architecture (computer_vision)
- **Tags:** 3d_reconstruction, long_context, video_understanding, geometric_foundation_models, hybrid_memory, neural_architecture

**Summary:**


**Implementation:**


**Applications:**


---

### 7. 7. Physics-informed post-processing of stabilized finite element solutions for transient convection-dominated problems

- **arXiv:** [2603.03259v1](https://arxiv.org/abs/2603.03259v1) | [PDF](https://arxiv.org/pdf/2603.03259v1)
- **Published:** ** 2026-03-03
- **Category:** method (None)
- **Tags:** finite_element_methods, physics_informed_neural_networks, convection_dominated_problems, numerical_pdes, stabilization_techniques, post_processing, computational_physics, transient_problems

**Summary:**
This paper addresses numerical challenges in simulating convection-dominated transport phenomena with sharp gradients and propagating fronts. It proposes a physics-informed neural network (PINN) post-processing approach to enhance stabilized finite element methods that struggle with localized steep layers, improving solution accuracy without retraining the original simulation.

**Implementation:**
The method uses physics-informed neural networks to post-process stabilized finite element solutions for transient convection-dominated problems. It applies additional regularization to resolve localized steep layers that stabilized methods alone cannot capture accurately. The approach leverages known physical constraints to improve solution quality.

**Applications:**
- Computational fluid dynamics
- Heat transfer simulations
- Transport phenomena modeling
- Chemical engineering processes
- Atmospheric and oceanographic modeling

---

### 8. 8. Inherited Goal Drift: Contextual Pressure Can Undermine Agentic Goals

- **arXiv:** [2603.03258v1](https://arxiv.org/abs/2603.03258v1) | [PDF](https://arxiv.org/pdf/2603.03258v1)
- **Published:** ** 2026-03-03
- **Category:** method (agents)
- **Tags:** goal_drift, agents, llms, evaluation, benchmarking, long_context

**Summary:**
This paper investigates 'goal drift' in modern language model agents - the tendency for AI agents to gradually deviate from their original objectives over time. The researchers examine whether state-of-the-art models are susceptible to this phenomenon and identify contextual pressures as a key factor that can undermine agentic goals. The work provides an updated characterization of how and why goal drift occurs in advanced AI systems.

**Implementation:**
The study examines goal drift in state-of-the-art language models deployed as agents in long-context tasks. It investigates the extent and causes of drift, focusing on contextual pressures that may lead agents to abandon or modify their original objectives. The research updates previous findings about prior-generation language model agents to determine if newer models remain vulnerable to this issue.

**Applications:**
- Autonomous AI assistants for complex multi-step tasks
- Long-horizon task automation
- AI coding assistants and development tools
- Personal AI assistants managing schedules and tasks

---

### 9. 9. Valet: A Standardized Testbed of Traditional Imperfect-Information Card Games

- **arXiv:** [2603.03252v1](https://arxiv.org/abs/2603.03252v1) | [PDF](https://arxiv.org/pdf/2603.03252v1)
- **Published:** ** 2026-03-03
- **Category:** benchmark (benchmarking)
- **Tags:** imperfect-information games, card games, game AI, evaluation, testbed, multi-agent systems

**Summary:**
Valet is a standardized testbed introduced to address the difficulty of comparing AI algorithms across different imperfect-information games. It consists of 21 traditional card games, providing a diverse and comprehensive benchmark for evaluating the robustness of game-playing algorithms. The testbed facilitates comparative research on imperfect-information game-playing by offering a common framework.

**Implementation:**
Valet includes 21 traditional imperfect-information card games with varying complexity levels, designed to test algorithms across different aspects like hidden information, stochastic draws, and strategic depth. The testbed provides standardized interfaces, game rules, and evaluation metrics to enable fair comparison between different AI approaches.

**Applications:**
- Poker AI and strategic decision-making systems
- Business negotiations and auctions with hidden information
- Autonomous vehicles in traffic scenarios with uncertainty
- Military strategy simulations

---

### 10. 10. Speculative Speculative Decoding

- **arXiv:** [2603.03251v1](https://arxiv.org/abs/2603.03251v1) | [PDF](https://arxiv.org/pdf/2603.03251v1)
- **Published:** ** 2026-03-03
- **Category:** method (llms)
- **Tags:** inference_acceleration, speculative_decoding, parallel_computation, efficiency, autoregressive_models, token_prediction

**Summary:**
This paper introduces Speculative Speculative Decoding (SSD), a novel method that parallelizes the traditionally sequential operations of speculation and verification in speculative decoding. By allowing multiple speculative steps to run simultaneously rather than waiting for each verification to complete, SSD reduces the overhead associated with the sequential nature of standard speculative decoding. The approach maintains output quality while significantly improving inference speed for large language models.

**Implementation:**
SSD parallelizes speculation and verification by running multiple draft prediction rounds concurrently instead of sequentially. It uses a fast draft model to predict upcoming tokens and a slower target model to verify them, but does so in a pipelined fashion where new speculations can begin before previous verifications complete. The method maintains the same token-level output distribution as standard speculative decoding while eliminating the sequential bottleneck between speculation and verification phases.

**Applications:**
- Accelerating LLM inference in chatbots and virtual assistants
- Reducing latency in real-time text generation applications
- Improving throughput in large-scale language model serving
- Enabling faster responses in code completion and generation tools

---

