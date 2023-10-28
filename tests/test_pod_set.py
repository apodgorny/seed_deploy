import os
import pytest

from unittest.mock   import patch, mock_open, MagicMock
from library.pod_set import PodSet

def test_pod_set_creation_and_deletion():
	with patch('library.file.File.mkdir') as mock_mkdir, \
		 patch('library.file.File.rm') as mock_rm:

		# Initialize the PodSet object and call create
		pod_set = PodSet('test_pod_set')
		pod_set.create()

		# Check if mkdir was called with correct path
		mock_mkdir.assert_called_with(os.path.join('pod_sets', 'test_pod_set'))

		# Call delete and check if rm was called with correct path
		pod_set.delete()
		mock_rm.assert_called_with(os.path.join('pod_sets', 'test_pod_set'))


def test_create_and_delete_pod():
	with patch('library.file.File.mkdir') as mock_mkdir, \
	     patch('library.file.File.rm') as mock_rm, \
	     patch('builtins.open', mock_open()) as mock_file:

		# Initialize PodSet and create it
		pod_set = PodSet('test_pod_set').create()

		# Create a pod
		pod_set.create_pod('test_pod')

		# Verify mkdir calls
		mock_mkdir.assert_called()

		# Verify that open was called for constants.json
		mock_file.assert_any_call('pod_sets/test_pod_set/test_pod/conf/constants.json', 'w')
		# Verify that open was also called for variables.py
		mock_file.assert_any_call('pod_sets/test_pod_set/test_pod/conf/variables.py', 'w')

		# Delete a pod
		pod_set.delete_pod('test_pod')

		# Verify rm call
		mock_rm.assert_called()


def test_create_and_delete_template():
	with patch('library.file.File.exists') as mock_exists, \
	     patch('library.file.File.rm') as mock_remove, \
	     patch('os.listdir') as mock_listdir, \
	     patch('library.file.File.mkdir') as mock_mkdir, \
	     patch('builtins.open', mock_open()) as mock_file:

		# Simulate that the directory does exist
		mock_exists.return_value = True

		# Simulate the mkdir method to return True
		mock_mkdir.return_value = True

		# Simulate an empty list of pod names in the directory
		mock_listdir.return_value = []

		# Initialize PodSet and create it
		pod_set = PodSet('test_pod_set').create()

		# Create a pod
		pod = pod_set.create_pod('test_pod')

		# Assertions to confirm that the methods have been called
		mock_exists.assert_called()
		mock_mkdir.assert_any_call('pod_sets/test_pod_set')
		mock_listdir.assert_called_with('pod_sets/test_pod_set')

def test_get_pod():
	with patch('library.pod.Pod') as MockPod, \
	     patch('library.file.File.mkdir') as mock_mkdir, \
	     patch('library.file.File.rm') as mock_rm:

		# Initialize PodSet and create it
		pod_set = PodSet('test_pod_set').create()

		# Mock a Pod object
		mock_pod = MockPod()
		pod_set.pods['test_pod'] = mock_pod

		# Get a pod and assert it's the one we just added
		assert pod_set.get_pod('test_pod') == mock_pod

		# Get a non-existing pod and assert it returns None
		assert pod_set.get_pod('non_existing_pod') == None

def test_read_pods():
	with patch('library.file.File.exists') as mock_exists, \
	     patch('os.listdir') as mock_listdir, \
	     patch('os.path.isdir') as mock_isdir, \
	     patch('library.pod.Pod') as MockPod:

		# Simulate that the directory does exist
		mock_exists.return_value = True

		# Simulate a list of pod names in the directory
		mock_listdir.return_value = ['test_pod_1', 'test_pod_2']

		# Simulate os.path.isdir returns True
		mock_isdir.return_value = True

		# Create a mock instance for MockPod
		mock_pod_instance = MagicMock()
		MockPod.return_value = mock_pod_instance

		# Initialize PodSet
		pod_set = PodSet('test_pod_set')

		# Validate that _read_pods was called and behaved as expected
		mock_exists.assert_called_with('pod_sets/test_pod_set')
		mock_listdir.assert_called_with('pod_sets/test_pod_set')
		assert 'test_pod_1' in pod_set.pods

def test_podset_initialization_failure():
	with patch('library.file.File.exists') as mock_exists:
		mock_exists.return_value = False
		pod_set = PodSet('test_pod_set')
		assert pod_set.pods == {}

def test_empty_podset():
	with patch('library.file.File.exists') as mock_exists, \
	     patch('os.listdir') as mock_listdir:
		mock_exists.return_value = True
		mock_listdir.return_value = []
		pod_set = PodSet('test_pod_set')
		assert pod_set.pods == {}

def test_non_directory_files_in_podset():
	with patch('library.file.File.exists') as mock_exists, \
	     patch('os.listdir') as mock_listdir, \
	     patch('os.path.isdir') as mock_isdir:

		mock_exists.return_value = True
		mock_listdir.return_value = ['test_pod_1', 'file.txt']
		mock_isdir.side_effect = [True, False]
		
		pod_set = PodSet('test_pod_set')
		assert 'file.txt' not in pod_set.pods

def test_multiple_pods():
	with patch('library.file.File.exists') as mock_exists, \
	     patch('os.listdir') as mock_listdir, \
	     patch('os.path.isdir') as mock_isdir, \
	     patch('library.pod.Pod') as MockPod:

		# Simulate that the directory does exist
		mock_exists.return_value = True

		# Simulate a list of multiple pod names in the directory
		mock_listdir.return_value = ['test_pod_1', 'test_pod_2', 'test_pod_3']

		# Simulate os.path.isdir returns True
		mock_isdir.return_value = True

		# Create a mock instance for MockPod
		mock_pod_instance = MagicMock()
		MockPod.return_value = mock_pod_instance

		# Initialize PodSet
		pod_set = PodSet('test_pod_set')

		# Validate that _read_pods was called and behaved as expected
		mock_exists.assert_called_with('pod_sets/test_pod_set')
		mock_listdir.assert_called_with('pod_sets/test_pod_set')

		# Validate all test pods are in pod_set.pods
		assert 'test_pod_1' in pod_set.pods
		assert 'test_pod_2' in pod_set.pods
		assert 'test_pod_3' in pod_set.pods
