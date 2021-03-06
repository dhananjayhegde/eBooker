#!/usr/bin/env python3

#Imports
import os
import sys
from extras import getInput, isPython3, isNix

# Define Tester class
class Tester(object):
    def test(self, n):
        try:
            assert (
                # Test for Python files and LICENSE.txt
                os.path.exists("tester.py") and
                os.path.exists("extras.py") and
                os.path.exists("commands.py") and
                os.path.exists("internals.py") and
                os.path.exists("ebooker.py") and
                os.path.exists("LICENSE.txt") and
                type(self) is Tester
            )
            if n:
                assert (
                    # If running in CircleCI...
                    # Test for docs/ and contents...
                    # And README.md and CONTRIBUTING.md
                    os.path.exists("README.md") and
                    os.path.exists("CONTRIBUTING.md") and
                    os.path.exists("docs/downloads.html") and
                    os.path.exists("docs/about.html") and
                    os.path.exists("docs/octocat1.png") and
                    os.path.exists("docs/octocat2.png") and
                    os.path.exists("docs/stylesheet.css") and
                    os.path.exists("docs/index.html") and
                    os.path.exists("docs") and
                    type(self) is Tester
                )
        except:
            # Tests failed
            print("\nAn important project file is missing!")
            print("Program execution stopped. Type RETURN to exit. Run \"debug\" command when you next open eBooker to report this problem.")
            print("If you didn't already, always cd into eBooker's folder before running this program.")
            
            # Wait for RETURN, then exit
            getInput("")
            sys.exit(1)

if __name__ == "__main__":
    # Running in CircleCI
    Tester().test(1)
    sys.exit(0)