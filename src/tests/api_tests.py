# -*- coding: utf-8 -*-

import unittest
import os
import requests

import tests.context

from helpers import csvreader
from helpers import logger
import helpers.api_assertions
import helpers.api_crud
#from helpers import api_crud
#from helpers import api_assertions
import nose

path = "../data/input.csv"
input=helpers.csvreader.read_csv(None,path)

print ("Start executing API tests")

class test_api_ccc:
    ''' Run API automation '''
    helpers.logger.log_level()
    helpers.api_crud.api_methods_all(input)

if __name__ == '__main__':
    mytests = test_api_ccc()