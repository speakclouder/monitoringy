# Monitoringy

.. image:: https://github.com/speakclouder/monitoringy/workflows/ci/badge.svg?branch=main
    :target: https://github.com/speakclouder/monitoringy/actions?workflow=ci
    :alt: CI

.. image:: https://img.shields.io/readthedocs/python-project-skeleton/latest?label=Read%20the%20Docs
    :target: https://python-project-skeleton.readthedocs.io/en/latest/index.html
    :alt: Read the Docs

Summary
-------

Monitoringy is a python library used to create AWS Cloudwatch dashboards for your resources using a YAML configuration file.

Motivation
----------

If you're anything like me, you'll create resources in your SAM template, get the new feature into production and then forget about it until it's broken.

This package - and the process of creating a configuration file itself - is designed to help you think about _what_ resources are being
created, how you're monitoring them, and how you're alerted when something goes wrong.

Installation and usage
----------------------

This package is deisgned to be used within a Lambda function that is triggered as a custom resource in your cloudformation template. 

```YAML
  MonitoringFunction:
    Type: AWS::Serverless::Function
    Properties:
      Handler: handler_monitoring.handle
      CodeUri: ./functions/MonitoringFunction
      Description: Monitoring Stack Resources
      FunctionName: !Sub "${AppName}-monitoring-${AppEnv}"
      Role: !GetAtt LambdaExecutionRole.Arn

  MonitoringFunctionRunner:
    Type: AWS::CloudFormation::CustomResource
    Version: "1.0"
    Properties:
      ServiceToken: !GetAtt MonitoringFunction.Arn
      Region: !Ref AWS::Region
      Location: "./monitoring/dashboard.yaml"
      AppName: !Ref AppName
      AppEnv: !Ref AppEnv
```


Issues and Discussions
----------------------

As usual for any GitHub-based project, raise an `issue`_ if you find any bug or
want to suggest an improvement, or open a `discussion`_ if you want to discuss
or chat :wink:

Projects using this skeleton
----------------------------

Below, a list of the projects using this repository as template or as base for
their CI implementations:

* `julie-forman-kay-lab/IDPConformerGenerator <https://github.com/julie-forman-kay-lab/IDPConformerGenerator>`_
* `haddocking/HADDOCK3 <https://github.com/haddocking/haddock3>`_
* `THGLab/MCSCE <https://github.com/THGLab/MCSCE>`_
* `joaomcteixeira/taurenmd <https://github.com/joaomcteixeira/taurenmd>`_
* `MDAnalysis/mdacli <https://github.com/MDAnalysis/mdacli>`_

If you use this repository as a reference for your works, let me know, so I
list your work above, as well.

Version
-------

v0.11.3

.. _GitHub Actions: https://github.com/features/actions
.. _PyPI: https://pypi.org
.. _blog post: https://blog.ionelmc.ro/2014/05/25/python-packaging/
.. _bump2version: https://github.com/c4urself/bump2version
.. _cookiecutter-pylibrary: https://github.com/ionelmc/cookiecutter-pylibrary
.. _cookiecutter: https://cookiecutter.readthedocs.io/en/latest/index.html
.. _discussion: https://github.com/speakclouder/monitoringy/discussions
.. _documentation: https://python-project-skeleton.readthedocs.io/
.. _even for scientific software: https://github.com/MolSSI/cookiecutter-cms
.. _hypothesis: https://hypothesis.readthedocs.io/en/latest/
.. _ionel: https://github.com/ionelmc
.. _issue: https://github.com/speakclouder/monitoringy/issues
.. _latest branch: https://github.com/speakclouder/monitoringy/tree/latest
.. _master branch: https://github.com/speakclouder/monitoringy/tree/master
.. _pdb-tools: https://github.com/haddocking/pdb-tools/blob/2a070bbacee9d6608b44bb6d2f749beefd6a7690/.github/workflows/bump-version-on-push.yml
.. _project's documentation: https://python-project-skeleton.readthedocs.io/en/latest/index.html
.. _pytest: https://docs.pytest.org/en/stable/
.. _python-nameless: https://github.com/ionelmc/python-nameless
.. _structlog: https://github.com/hynek/structlog
.. _test.pypi.org: https://test.pypi.org
.. _tox-gh-actions: https://github.com/ymyzk/tox-gh-actions
.. _tox: https://tox.readthedocs.io/en/latest/
.. _ReadTheDocs: https://readthedocs.org/
