import pytest
from library.seed_error import SeedError

def test_seed_error():
    # Test default message
    with pytest.raises(SeedError, match='A custom error occurred'):
        raise SeedError()

    # Test custom message
    custom_message = 'Something specific went wrong'
    with pytest.raises(SeedError, match=custom_message):
        raise SeedError(custom_message)
