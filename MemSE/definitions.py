from pathlib import Path
import enum
import torch
import torch.nn as nn
import MemSE.nn as nnM

ROOT = Path(__file__).parent.parent

class WMAX_MODE(enum.Enum):
	ALL = enum.auto()
	LAYERWISE = enum.auto()
	COLUMNWISE = enum.auto()

UNSUPPORTED_OPS = [
	nn.BatchNorm2d,
	nn.ReLU,
	nn.GELU,
]

SUPPORTED_OPS = {
	nn.Linear: nnM.linear,
	nn.Softplus: nnM.softplus,
	nn.AvgPool2d: nnM.avgPool2d,
	nnM.Conv2DUF: nnM.Conv2DUF.memse
}
