# Coworking Space Service Extension

The Coworking Space Service is a set of APIs that enables users to request one-time tokens and administrators to authorize access to a coworking space. This service follows a microservice pattern and the APIs are split into distinct services that can be deployed and managed independently of one another.

## Overview

There are 2 services / APIs: analytics API and its database. Since the database is installed via Helm, which also creates the DB service and pod/s, there is only one codebuild pipeline which is for the analytics API. The deployment files contain the needed deployment template to deploy the service as well as db configuration and secret files.

## Deployment Process and Changes

After the cluster and node group has been set up, helm is installed, then the analytics service is deployed with the command `kubectl apply -f deployment/ --force`. The same command can be used to update the services since the --force flag will replace the existing service and pod/s with the new ones.

## Versioning

Each of the deploymnets use semantic versioning. The buildspec.yml files contain the logic to automatically update the build version. Minor and major versions are updated manually in the buildspec files.
