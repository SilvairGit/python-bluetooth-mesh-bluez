#
# python-bluetooth-mesh - Bluetooth Mesh for Python
#
# Copyright (C) 2019  SILVAIR sp. z o.o.
#
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
#
#
import asyncio

import pytest
import pytest_asyncio

from bluetooth_mesh.messages.generic.onoff import GenericOnOffOpcode


@pytest_asyncio.fixture
async def event_loop():
    return asyncio.get_running_loop()


@pytest.fixture(name="status_parsed")
def fixture_status_parsed():
    return {
        "opcode": GenericOnOffOpcode.GENERIC_ONOFF_STATUS,
        "generic_onoff_status": {"present_onoff": 0},
    }


@pytest.fixture(name="status_encoded")
def fixture_status_encoded():
    return b"\x82\x04\x00"


@pytest.fixture(name="get_encoded")
def fixture_get_encoded():
    return b"\x82\x01"


@pytest.fixture(name="source")
def fixture_source():
    return 0x0001


@pytest.fixture(name="destination")
def fixture_destination():
    return 0x0010


@pytest.fixture(name="app_index")
def fixture_app_index():
    return 0


@pytest.fixture(name="net_index")
def fixture_net_index():
    return 0


@pytest.fixture(name="element_path")
def fixture_element_path():
    return "test_element_path_string"
