# Copyright 2020 ros2_control development team
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from ros2cli.node.direct import add_arguments
from ros2cli.verb import VerbExtension

from ros2controlcli.api import add_controller_mgr_parsers, configure_start_controller, \
    ControllerNameCompleter


class ConfigureStartControllerVerb(VerbExtension):
    """Configure and Start a controller in a controller manager."""

    def add_arguments(self, parser, cli_name):
        add_arguments(parser)
        arg = parser.add_argument(
            'controller_name', help='Name of the controller')
        arg.completer = ControllerNameCompleter()
        add_controller_mgr_parsers(parser)

    def main(self, *, args):
        print("deprecated warning: Please use either 'load --state' or 'set_state'")
        response = configure_start_controller(args.controller_manager, args.controller_name)
        if not response.ok:
            return 'Error configuring and starting controller, check controller_manager logs'
        return 'Successfully configured and started controller {}'.format(args.controller_name)
