# -*- encoding: utf-8 -*-
# Copyright (c) 2021 Bloomberg LP
#
# Authors: Ajay Tikoo <atikoo@bloomberg.net>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from oslo_config import cfg

timeout_help_message = """
Number of seconds to wait for migration to complete.

After Watcher executes the instance migrate action, it polls for the
status of the instance to check whether migration has completed or
failed. This value sets the the maximum number number of seconds for
which Watcher will poll instance status. If migration does not
complete of fail within this time, Watcher will assume that it failed.
"""

nova_helper = cfg.OptGroup(name='nova_helper',
                           title='Configuration Options for nova_helper module')

NOVA_HELPER_OPTS = [
    cfg.IntOpt('live_migration_timeout',
               default='120',
               min=120,
               help=timeout_help_message)]


def register_opts(conf):
    conf.register_group(nova_helper)
    conf.register_opts(NOVA_HELPER_OPTS, group=nova_helper)


def list_opts():
    return [(nova_helper, NOVA_HELPER_OPTS)]

