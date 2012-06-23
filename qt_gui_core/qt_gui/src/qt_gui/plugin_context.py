# Copyright (c) 2011, Dirk Thomas, Dorian Scholz, TU Darmstadt
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#   * Redistributions of source code must retain the above copyright
#     notice, this list of conditions and the following disclaimer.
#   * Redistributions in binary form must reproduce the above
#     copyright notice, this list of conditions and the following
#     disclaimer in the documentation and/or other materials provided
#     with the distribution.
#   * Neither the name of the TU Darmstadt nor the names of its
#     contributors may be used to endorse or promote products derived
#     from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

from . import qt_binding_helper #@UnusedImport
from QtCore import QObject

class PluginContext(QObject):

    """
    Plugin context providing information to the plugin and exposing methods for the plugin to interact with the framework.
    It relays all methods to the corresponding `PluginHandler`.
    """

    def __init__(self, handler):
        super(PluginContext, self).__init__(handler)
        self.setObjectName('PluginContext')

        self._handler = handler

    def serial_number(self):
        """
        Return the serial number of the plugin.
        @return: the serial number
        @rtype: int
        """
        return self._handler.instance_id().serial_number

    def add_widget(self, widget):
        """
        Add a widget to the UI.
        @param widget: the widget
        @type widget: QWidget
        """
        self._handler.add_widget(widget)

    def remove_widget(self, widget):
        """
        Remove a widget from the UI.
        @param widget: the widget
        @type widget: QWidget
        """
        self._handler.remove_widget(widget)

    def close_plugin(self):
        """
        Close the plugin.
        The framework will call `Plugin.shutdown_plugin()` and unload it afterwards.
        """
        self._handler.close_plugin()
