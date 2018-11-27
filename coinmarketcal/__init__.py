# Author: mfuellbier
# This file is part of python-coinmarketcal.
#
# python-coinmarketcal is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# python-coinmarketcal is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with python-coinmarketcal.  If not, see <http://www.gnu.org/licenses/>.


import logging
logger=logging.getLogger("python-coinmarketcal")
logger.setLevel(logging.WARNING)
ch = logging.StreamHandler()
ch.setLevel(logging.WARNING)
logger.addHandler(ch)

import sys
from coinmarketcal.client import Coinmarketcal
