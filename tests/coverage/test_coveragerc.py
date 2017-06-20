import os

from parse import parse

from hatch.core import create_package
from hatch.coverage.coveragerc import TEMPLATE
from hatch.settings import DEFAULT_SETTINGS
from ..utils import read_file, temp_chdir


def test_package_name():
    with temp_chdir() as d:
        settings = DEFAULT_SETTINGS.copy()
        create_package(d, 'invalid-name', settings)

        contents = read_file(os.path.join(d, '.coveragerc'))
        parsed = parse(TEMPLATE, contents)

        assert parsed['package_name_normalized'] == 'invalid_name'