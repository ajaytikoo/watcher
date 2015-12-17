# -*- encoding: utf-8 -*-
# Copyright (c) 2015 b<>com
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
import mock
from mock import MagicMock

from watcher.common import utils
from watcher.decision_engine.audit.default import DefaultAuditHandler
from watcher.decision_engine.messaging.audit_endpoint import AuditEndpoint
from watcher.metrics_engine.cluster_model_collector.manager import \
    CollectorManager
from watcher.tests import base
from watcher.tests.decision_engine.strategy.strategies.faker_cluster_state \
    import FakerModelCollector


class DefaultAuditHandlerMock(DefaultAuditHandler):
    def setUp(self):
        super(DefaultAuditHandlerMock, self).setUp()

    def executor(self):
        pass


class TestAuditEndpoint(base.TestCase):
    def setUp(self):
        super(TestAuditEndpoint, self).setUp()

    def test_do_trigger_audit(self):
        audit_uuid = utils.generate_uuid()
        model_collector = FakerModelCollector()
        audit_handler = DefaultAuditHandler(MagicMock(), model_collector)
        endpoint = AuditEndpoint(audit_handler, max_workers=2)

        with mock.patch.object(CollectorManager, 'get_cluster_model_collector') \
                as mock_call2:
            mock_call2.return_value = 0

            with mock.patch.object(DefaultAuditHandler, 'execute') \
                    as mock_call:
                mock_call.return_value = 0
                endpoint.do_trigger_audit(audit_handler, audit_uuid)
                # mock_call.assert_called_once_with()
            mock_call2.assert_called_once_with()

    def test_trigger_audit(self):
        audit_uuid = utils.generate_uuid()
        model_collector = FakerModelCollector()
        audit_handler = DefaultAuditHandlerMock(MagicMock(),
                                                model_collector)
        endpoint = AuditEndpoint(audit_handler, max_workers=2)

        with mock.patch.object(DefaultAuditHandlerMock, 'executor') \
                as mock_call:
            mock_call.return_value = 0
            endpoint.trigger_audit(audit_handler, audit_uuid)
