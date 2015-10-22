# -*- encoding: utf-8 -*-
# Copyright (c) 2015 b<>com
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from watcher.decision_engine.framework.model.named_element import NamedElement
from watcher.decision_engine.framework.model.vm_state import VMState


class VM(NamedElement):
    def __init__(self):
        self._state = VMState.ACTIVE.value

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state):
        self._state = state
