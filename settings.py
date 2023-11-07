import os
import sys

BASE_DIR            = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR_NAME    = 'project'
NAMESPACES_DIR_NAME = f'{PROJECT_DIR_NAME}/namespaces'
PODSETS_DIR_NAME    = f'{PROJECT_DIR_NAME}/podsets'

sys.path.append(BASE_DIR)