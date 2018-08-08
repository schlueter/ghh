# Copyright 2018 Brandon Schlueter
# This file is part of ghh.
#
# Ghh is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from boron import WSGIApp


class GhhWSGIApp(WSGIApp):

    def handle_http_get(self, environ, start_response):
        """
        Handle POSTs

        Delegates POST requests for known GitHub events to their handlers.

        Unknown events are responded to with 400
        """
        response_headers = [
            ('Content-type', 'text/html'),
        ]
        start_response('200 Accepted', response_headers)
        return """
        <div style="margin: 0 auto; font-size: 24px; position: relative; top: 50vp; width: 500px;">
            This is a {method}. I can handle this!
        """ .format(method=environ['REQUEST_METHOD'])
