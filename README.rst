Monitoringy
===============================

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

Add a function and custom resource to your SAM template:

```YAML
  MonitoringFunction:
    Type: AWS::Serverless::Function
    Properties:
      Handler: handler_monitoring.handle
      CodeUri: ./MonitoringFunction
      Description: Monitoring Stack Resources
      Role: !GetAtt LambdaExecutionRole.Arn

  MonitoringFunctionRunner:
    Type: AWS::CloudFormation::CustomResource
    Version: "1.0"
    Properties:
      ServiceToken: !GetAtt MonitoringFunction.Arn
      Region: !Ref AWS::Region
      Location: "./MonitoringFunction/dashboard.yaml"
      AppName: !Ref AppName
      AppEnv: !Ref AppEnv
```

Then create a YAML configuration file in location accessible to the function (in this case, `./MonitoringFunction/dashboard.yaml`):

```YAML
dashboards:
  - name: main
    title: Microserservice 002A Dashboard
    description: MS002A Gets users birthday and returns it as a unix timestamp, also runs a cron job to send a birthday email
    github: https://github.com/your/repo
    stack_name: ms002a
    sections:
      - title: Get Birthday
        description: Gets the users birthday and returns it as a unix timestamp
        documentation:
          name: ADR
          link: https://github.com/your/repo/blob/main/docs/adr/0001-get-birthday.md
        functions:
          - template_resource_name: GetBirthdayFunction
```

The idea here is create a new section for each set of resources used by a single feature/ADR/epic/whatever. 