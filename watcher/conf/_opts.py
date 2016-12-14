# -*- encoding: utf-8 -*-
# Copyright 2014
# The Cloudscaling Group, Inc.
# Copyright (c) 2016 Intel Corp
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

from keystoneauth1 import loading as ka_loading

from watcher.common import clients
from watcher.conf import api as conf_api
from watcher.conf import applier as conf_applier
from watcher.conf import db
from watcher.conf import decision_engine as conf_de
from watcher.conf import exception
from watcher.conf import paths
from watcher.conf import planner as conf_planner
from watcher.conf import utils


def list_opts():
    """Legacy aggregation of all the watcher config options"""
    return [
        ('DEFAULT',
         (conf_api.AUTH_OPTS +
          exception.EXC_LOG_OPTS +
          paths.PATH_OPTS +
          utils.UTILS_OPTS)),
        ('api', conf_api.API_SERVICE_OPTS),
        ('database', db.SQL_OPTS),
        ('watcher_planner', conf_planner.WATCHER_PLANNER_OPTS),
        ('watcher_applier', conf_applier.APPLIER_MANAGER_OPTS),
        ('watcher_decision_engine',
         (conf_de.WATCHER_DECISION_ENGINE_OPTS +
          conf_de.WATCHER_CONTINUOUS_OPTS)),
        ('nova_client', clients.NOVA_CLIENT_OPTS),
        ('glance_client', clients.GLANCE_CLIENT_OPTS),
        ('cinder_client', clients.CINDER_CLIENT_OPTS),
        ('ceilometer_client', clients.CEILOMETER_CLIENT_OPTS),
        ('neutron_client', clients.NEUTRON_CLIENT_OPTS),
        ('watcher_clients_auth',
         (ka_loading.get_auth_common_conf_options() +
          ka_loading.get_auth_plugin_conf_options('password') +
          ka_loading.get_session_conf_options()))
    ]
