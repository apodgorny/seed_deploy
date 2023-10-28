import os
from unittest.mock import patch, call
from unittest.mock import MagicMock
from contextlib import contextmanager
from library.namespace import Namespace

@contextmanager
def fake_open(*args, **kwargs):
    print(f'open called with: {args}, {kwargs}')
    yield MagicMock()

def test_namespace_creation():
    with patch('library.file.File.mkdir', autospec=True) as mock_mkdir, \
        patch('builtins.open', new=fake_open):
        
        # Side effect (just to aid debugging)
        mock_mkdir.side_effect = lambda x: print(f"mkdir called with: {x}")

        # Initialize the Namespace object
        namespace = Namespace('test_namespace')
        namespace.create()

        # Assertions for checking mkdir calls
        expected_mkdir_call = os.path.join('ROOT_DIR', 'namespaces', 'test_namespace')
        mock_mkdir.assert_called_with(expected_mkdir_call)
