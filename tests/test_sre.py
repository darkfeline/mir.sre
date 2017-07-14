# Copyright (C) 2017 Allen Li
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

from mir import sre


def test_x_join():
    got = sre.x_join(r'\w+', 'foo bar baz', lambda s: 'spam' + s)
    assert got == 'spamfoo spambar spambaz'


def test_y_join():
    got = sre.y_join(r' +', 'foo bar baz', lambda s: 'spam' + s)
    assert got == 'spamfoo spambar spambaz'


def test_x_iter():
    got = list(sre.x_iter(r'\w+', 'foo bar baz'))
    assert got == ['foo', 'bar', 'baz']


def test_y_iter():
    got = list(sre.y_iter(r' +', 'foo bar baz'))
    assert got == ['foo', 'bar', 'baz']
