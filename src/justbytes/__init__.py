# Copyright (C) 2015  Red Hat, Inc.
#
# This copyrighted material is made available to anyone wishing to use,
# modify, copy, or redistribute it subject to the terms and conditions of
# the GNU General Public License v.2, or (at your option) any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY expressed or implied, including the implied warranties of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General
# Public License for more details.  You should have received a copy of the
# GNU General Public License along with this program; if not, write to the
# Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
# 02110-1301, USA.  Any Red Hat trademarks that are incorporated in the
# source code or documentation are not subject to the GNU General Public
# License and may only be used or replicated with the express permission of
# Red Hat, Inc.
#
# Red Hat Author(s): Anne Mulhern <amulhern@redhat.com>

""" The public interface of the justbytes package.

    Contents:

    * Unit constants in SI and binary units
       - Universal:
          * B

       - SI:
          * KB
          * MB
          * GB
          * TB
          * PB
          * EB
          * ZB
          * YB

       - Binary:
          * KiB
          * MiB
          * GiB
          * TiB
          * PiB
          * EiB
          * ZiB
          * YiB

       - UNITS: :func:`._constants.UNITS`

    * Rounding constants, with meaning as for the Python decimal module:
       - ROUND_DOWN
       - ROUND_HALF_DOWN
       - ROUND_HALF_UP
       - ROUND_UP

       - ROUNDING_METHODS

    * Configuration classes:
       - StrConfig: :class:`._config.StrConfig`

    * Exception classes:
       - SizeError: :class:`._errors.SizeError`

    * Size classes:
       - Size: :class:`._size.Size`
       - AI: :class:`._sizes.AI`

    All parts of the public interface of justbytes must be imported directly
    from the top-level justbytes module, as::

        from justbytes import Size
        from justbytes import KiB
        from justbytes import SizeError

        s = Size(24, KiB)
        try:
            s + 32
        except SizeError as e:
            raise e
"""
# pylint: disable=invalid-name
# pylint: disable=wrong-import-position

# UNIT CONSTANTS
from ._constants import B

from ._constants import DecimalUnits as _DecimalUnits
KB = _DecimalUnits.KB
MB = _DecimalUnits.MB
GB = _DecimalUnits.GB
TB = _DecimalUnits.TB
PB = _DecimalUnits.PB
EB = _DecimalUnits.EB
ZB = _DecimalUnits.ZB
YB = _DecimalUnits.YB

from ._constants import BinaryUnits as _BinaryUnits
KiB = _BinaryUnits.KiB
MiB = _BinaryUnits.MiB
GiB = _BinaryUnits.GiB
TiB = _BinaryUnits.TiB
PiB = _BinaryUnits.PiB
EiB = _BinaryUnits.EiB
ZiB = _BinaryUnits.ZiB
YiB = _BinaryUnits.YiB

from ._constants import UNITS

# ROUNDING CONSTANTS
from ._constants import RoundingMethods as _RoundingMethods
ROUND_DOWN = _RoundingMethods.ROUND_DOWN
ROUND_HALF_DOWN = _RoundingMethods.ROUND_HALF_DOWN
ROUND_HALF_UP = _RoundingMethods.ROUND_HALF_UP
ROUND_UP = _RoundingMethods.ROUND_UP

from ._constants import ROUNDING_METHODS

# CONFIGURATION
from ._config import DisplayConfig
from ._config import InputConfig
from ._config import SizeConfig
from ._config import StrConfig

# EXCEPTIONS
from ._errors import SizeError

# SIZE
from ._size import Size
from ._sizes import getSizeFromInput
from ._sizes import AI
