#!/usr/bin/python3
#
# Copyright 2012-2017 "Korora Project" <dev@kororaproject.org>
#
# This program is free software: you can redistribute it and/or modify
# it under the temms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#

import logging

from lens.app import App

class MyApp(App):
  def __init__(self):
    App.__init__(self, name="Lens. 3D", inspector=True)

    self.namespaces = ['./sample-data/app-3d']

    self.on('close', self._close_app_cb)

  def _close_app_cb(self, *args):
    self.close()

logging.basicConfig(level=logging.DEBUG)

app = MyApp()

app.start()

