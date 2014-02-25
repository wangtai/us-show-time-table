#!/bin/bash

cd 1
svn st | grep \? | awk '{print $2}' | xargs svn add
svn ci -m 'deploy'
