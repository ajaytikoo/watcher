# -*- encoding: utf-8 -*-
# Copyright (c) 2015 b<>com
#
# Authors: Jean-Emile DARTOIS <jean-emile.dartois@b-com.com>
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
#

"""
A :ref:`Solution <solution_definition>` is the result of execution of a
:ref:`strategy <strategy_definition>` (i.e., an algorithm).
Each solution is composed of many pieces of information:

- A set of :ref:`actions <action_definition>` generated by the strategy in
  order to achieve the :ref:`goal <goal_definition>` of an associated
  :ref:`audit <audit_definition>`.
- A set of :ref:`efficacy indicators <efficacy_indicator_definition>` as
  defined by the associated goal
- A :ref:`global efficacy <efficacy_definition>` which is computed by the
  associated goal using the aforementioned efficacy indicators.

A :ref:`Solution <solution_definition>` is different from an
:ref:`Action Plan <action_plan_definition>` because it contains the
non-scheduled list of :ref:`Actions <action_definition>` which is produced by a
:ref:`Strategy <strategy_definition>`. In other words, the list of Actions in
a :ref:`Solution <solution_definition>` has not yet been re-ordered by the
:ref:`Watcher Planner <watcher_planner_definition>`.

Note that some algorithms (i.e. :ref:`Strategies <strategy_definition>`) may
generate several :ref:`Solutions <solution_definition>`. This gives rise to the
problem of determining which :ref:`Solution <solution_definition>` should be
applied.

Two approaches to dealing with this can be envisaged:

- **fully automated mode**: only the :ref:`Solution <solution_definition>`
  with the highest ranking (i.e., the highest
  :ref:`Optimization Efficacy <efficacy_definition>`) will be sent to the
  :ref:`Watcher Planner <watcher_planner_definition>` and translated into
  concrete :ref:`Actions <action_definition>`.
- **manual mode**: several :ref:`Solutions <solution_definition>` are proposed
  to the :ref:`Administrator <administrator_definition>` with a detailed
  measurement of the estimated :ref:`Optimization Efficacy
  <efficacy_definition>` and he/she decides which one will be launched.
"""

import abc

from watcher.decision_engine.solution import efficacy


class BaseSolution(object, metaclass=abc.ABCMeta):
    def __init__(self, goal, strategy):
        """Base Solution constructor

        :param goal: Goal associated to this solution
        :type goal: :py:class:`~.base.Goal` instance
        :param strategy: Strategy associated to this solution
        :type strategy: :py:class:`~.BaseStrategy` instance
        """
        self.goal = goal
        self._strategy = strategy
        self.origin = None
        self.model = None
        self.efficacy = efficacy.Efficacy(self.goal, self.strategy)

    @property
    def global_efficacy(self):
        return self.efficacy.global_efficacy

    @property
    def efficacy_indicators(self):
        return self.efficacy.indicators

    @property
    def strategy(self):
        return self._strategy

    def compute_global_efficacy(self):
        """Compute the global efficacy given a map of efficacy indicators"""
        self.efficacy.compute_global_efficacy()

    def set_efficacy_indicators(self, **indicators_map):
        """Set the efficacy indicators mapping (no validation)

        :param indicators_map: mapping between the indicator name and its value
        :type indicators_map: dict {`str`: `object`}
        """
        self.efficacy.set_efficacy_indicators(**indicators_map)

    @abc.abstractmethod
    def add_action(self, action_type, resource_id, input_parameters=None):
        """Add a new Action in the Solution

        :param action_type: the unique id of an action type defined in
            entry point 'watcher_actions'
        :param resource_id: the unique id of the resource to which the
            `Action` applies.
        :param input_parameters: An array of input parameters provided as
            key-value pairs of strings. Each key-pair contains names and
            values that match what was previously defined in the `Action`
            type schema.
        """
        raise NotImplementedError()

    @abc.abstractproperty
    def actions(self):
        raise NotImplementedError()
