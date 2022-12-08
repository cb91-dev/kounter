# ------------------------------------------------------------------
# Copyright (c) 2020 PyInstaller Development Team.
#
# This file is distributed under the terms of the GNU General Public
# License (version 2.0 or later).
#
# The full license is available in LICENSE.GPL.txt, distributed with
# this software.
#
# SPDX-License-Identifier: GPL-2.0-or-later
# ------------------------------------------------------------------


# This is hook for DNS python package dnspython.

from PyInstaller.utils.hooks import collect_submodules
hiddenimports = collect_submodules('dns.rdtypes')
