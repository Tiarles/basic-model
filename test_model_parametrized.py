# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY
# KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS FOR A
# PARTICULAR PURPOSE.

""" Basic example of a test using a very simple loopback Typhoon HIL schematic,
showing the most important concepts when writing a tests.

All the fundamental concepts shown here can be extended to more complex models. """

import typhoon.api.hil as hil
from typhoon.api.schematic_editor import SchematicAPI

import pytest
import logging
from pathlib import Path


logger = logging.getLogger(__name__)
model = SchematicAPI()

name = "model"
dirpath = Path(__file__).parent
sch = str(dirpath / "model.tse")
cpd = model.get_compiled_model_file(sch)


@pytest.mark.parametrize("set_point", [-10, 0, 10])
def test_basic_model(set_point):
    model.load(filename=sch)
    model.compile()
    hil.load_model(file=cpd, vhil_device=True)
    hil.start_simulation()
    
    hil.set_scada_input_value(scadaInputName='Input', 
                              value=set_point, 
                              )
    read_value = hil.read_analog_signal(name='Probe1')
    
    assert read_value == set_point
    