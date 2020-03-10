#!/usr/bin/env python3

import os
import sys
import argparse

targetBinary = "dyn_analysis-0-x64"
remenissionsDir = "/Hackery/remenissions/"
dynamicAnalyzerName = "dynamic_analyzer.py"

if __name__ == "__main__":
	cmd = "python %s%s -b %s" % (remenissionsDir, dynamicAnalyzerName, targetBinary)
	print("Cmd is: %s" % cmd)