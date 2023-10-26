import pytest
from library.no_op import NoOp

def test_no_op_functionality():
    # Initialize the NoOp object
    no_op_instance = NoOp()

    # Test some functionality, for example:
    assert isinstance(no_op_instance.some_method(), NoOp)
