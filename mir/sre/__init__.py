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

"""This module implements structural regular expressions.

Read Rob Pike's paper and the manual page for the sam editor for more
context.

Functions:

x_iter()
y_iter()
x_join()
y_join()
"""

__version__ = '0.1.0'

import re


def x_iter(pattern, string, flags=0):
    """Return an iterable over regexp matches."""
    yield from (m.group(0) for m in re.finditer(pattern, string, flags))


def y_iter(pattern, string, flags=0):
    """Return an iterable over the strings around regexp matches."""
    pattern = f'({pattern})'
    for i, substring in enumerate(re.split(pattern, string, flags)):
        if not i % 2:
            yield substring


def x_join(pattern, string, func, flags=0):
    """Apply a function to regexp matches.

    Each regexp match in string is substituted with the return value of
    func when called with the matched substring.
    """
    pattern = f'({pattern})'
    parts = []
    for i, substring in enumerate(re.split(pattern, string, flags)):
        if i % 2:
            parts.append(func(substring))
        else:  # Includes first and last
            parts.append(substring)
    return ''.join(parts)


def y_join(pattern, string, func, flags=0):
    """Apply a function to the strings around regexp matches.

    The substrings before, between, and after each regexp match in
    string is substituted with the return value of func when called with
    said substring.
    """
    pattern = f'({pattern})'
    parts = []
    for i, substring in enumerate(re.split(pattern, string, flags)):
        if i % 2:
            parts.append(substring)
        else:  # Includes first and last
            parts.append(func(substring))
    return ''.join(parts)
