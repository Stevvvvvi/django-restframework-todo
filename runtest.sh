#!/bin/bash
echo 'Running test generate report' 
coverage run manage.py test && coverage report && coverage html