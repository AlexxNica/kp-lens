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

import platform

from lens.app import App

app = App()

# load the app entry page
app.namespaces.append('./sample-data/app-dbus')

@app.bind('close')
def _close_app_cb(*args):
  app.close()

@app.bind('get-hostname')
def _get_hostname_cb(*args):
  app.emit('update-config', platform.node())

@app.bind('update-hostname')
def _update_hostname_cb(message):
  print(message)

@app.bind('toggle-window-maximize')
def _maximize_cb(*args):
  app.toggle_window_maximize()

@app.bind('toggle-window-fullscreen')
def _fullscreen_cb(*args):
  app.toggle_window_fullscreen()

@app.bind('dbus.list-names')
def _list_names(error, names):
    for name in names:
        print(name)

daemon = app.dbus_system_interface('org.freedesktop.DBus', '/org/freedesktop/DBus')
app.dbus_async_call('list-names', daemon.ListNames)

app.start()

