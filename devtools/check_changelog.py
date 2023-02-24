"""
Certify the developer has input all requirements for PR.

Situations tested:

* additions are reported in CHANGELOG.rst
"""
import os
import sys
from pathlib import Path

folder = Path(__file__).resolve().parents[1]
changelog = Path(folder, 'CHANGELOG.rst')


class ChangelogError(Exception):
    pass


with open(changelog, 'r') as fin:
    for line in fin:
        if line.startswith('v'):
            msg = [
                '',
                'CHANGELOG.rst not updated:',
                'Please add a summary of your additions',
                '',
                ]
            sys.exit(os.linesep.join(msg))

        elif line.startswith('*'):
            break
