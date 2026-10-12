# BSAI-viggle_turbo

[English](#english) | 中文

---

## 中文

Qwen-Image-2.1 Viggle Turbo 节点（官方移植），为 Qwen-Image-2.1 提供 6 步快速采样调度和非破坏性 LoRA 加载。

### 功能
- **Viggle Turbo Sigmas**：6 步采样调度，分辨率自适应 shift
- **Viggle Turbo LoRA (unmerged)**：运行时侧分支 LoRA，不合并权重，无损质量
- 支持文生图（t2i）和图生图（edit）工作流

### 安装
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/xm6018924/BSAI-viggle_turbo.git
```

### 要求
- Qwen-Image-2.1 模型
- ComfyUI 0.36+

---

## English

Qwen-Image-2.1 Viggle Turbo nodes (official port). Provides 6-step fast sampling schedule and non-destructive LoRA loading for Qwen-Image-2.1.

### Features
- **Viggle Turbo Sigmas**: 6-step sampling schedule with resolution-adaptive shift
- **Viggle Turbo LoRA (unmerged)**: runtime side-branch LoRA, non-lossy, no weight merging
- Supports t2i and edit workflows

### Installation
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/xm6018924/BSAI-viggle_turbo.git
```

### Requirements
- Qwen-Image-2.1 model
- ComfyUI 0.36+
