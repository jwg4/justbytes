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

""" Test for error classes. """
import unittest

from justbytes._errors import SizeFractionalResultError
from justbytes._errors import SizeNonsensicalBinOpError
from justbytes._errors import SizeNonsensicalBinOpValueError
from justbytes._errors import SizePowerResultError
from justbytes._errors import SizeValueError

class ErrorTestCase(unittest.TestCase):
    """ Exercise methods of error classes. """

    def testSizeValueError(self):
        """ Miscellaneous tests for the method. """
        self.assertIsNotNone(str(SizeValueError("junk", "junk", "junk")))
        self.assertIsNotNone(str(SizeValueError("junk", "junk")))

    def testSizeFractionalResultError(self):
        """ Miscellaneous tests for the method. """
        self.assertIsNotNone(str(SizeFractionalResultError()))

    def testSizeNonsensicalBinOpError(self):
        """ Miscellaneous tests for the method. """
        self.assertIsNotNone(str(SizeNonsensicalBinOpError("+", 2)))

    def testSizeNonsensicalBinOpValueError(self):
        """ Miscellaneous tests for the method. """
        self.assertIsNotNone(str(SizeNonsensicalBinOpValueError("+", 2)))

    def testSizePowerResultError(self):
        """ Miscellaneous tests for the method. """
        self.assertIsNotNone(str(SizePowerResultError()))
