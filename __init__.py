"""Qwen-Image-2.1 Viggle Turbo nodes (official port from Viggle/Qwen-Image-2.1-viggle-turbo).

Adds:
- Qwen-Image-2.1 Viggle Turbo Sigmas        (6-step schedule, resolution-shifted)
- Qwen-Image-2.1 Viggle Turbo LoRA (unmerged) (runtime side-branch LoRA, non-lossy)
"""
from .viggle_turbo import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
