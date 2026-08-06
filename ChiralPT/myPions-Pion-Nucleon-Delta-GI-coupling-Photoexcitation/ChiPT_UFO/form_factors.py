# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 14.3.0 for Linux x86 (64-bit) (July 8, 2025)
# Date: Mon 3 Aug 2026 23:14:50


from __future__ import absolute_import
from .object_library import all_form_factors, FormFactor

from .function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot



FF1PA = FormFactor(name = 'FF1PA',
                   type = 'real',
                   value = 'F1p(-P(-1,3)**2)')

FF1NA = FormFactor(name = 'FF1NA',
                   type = 'real',
                   value = 'F1n(-P(-1,3)**2)')

FF2PA = FormFactor(name = 'FF2PA',
                   type = 'real',
                   value = 'F2p(-P(-1,3)**2)')

FF2NA = FormFactor(name = 'FF2NA',
                   type = 'real',
                   value = 'F2n(-P(-1,3)**2)')

