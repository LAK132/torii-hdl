# SPDX-License-Identifier: BSD-2-Clause

from .intel      import IntelPlatform
from .lattice    import (
	LatticeECP5Platform, LatticeICE40Platform, LatticeMachXO2Platform, LatticeMachXO3LPlatform
)
from .quicklogic import QuicklogicPlatform
from .xilinx     import XilinxPlatform

__all__ = (
	'IntelPlatform',

	'LatticeECP5Platform',
	'LatticeICE40Platform',
	'LatticeMachXO2Platform',
	'LatticeMachXO3LPlatform',

	'QuicklogicPlatform',

	'XilinxPlatform',
)
