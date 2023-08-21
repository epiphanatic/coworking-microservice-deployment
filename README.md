# Coworking Space Service Extension

The Coworking Space Service is a set of APIs that enables users to request one-time tokens and administrators to authorize access to a coworking space. This service follows a microservice pattern and the APIs are split into distinct services that can be deployed and managed independently of one another.

## Overview

There are 5 separate git repositories: Admin API, Analytics API, User API, App DB, and Deployment files, where the first 4 have their own codebuild pipelines hooked into their respective repositories as well as 4 respective ECR repositories from which the deployment files pull from. The deployment files repository contains all the needed deployment templates to deploy the services.

## Deployment Process and Changes

After the cluster and node group has been set up, helm is installed, then the services are deployed with the command `kubectl apply -f deployment/ --force`. The same command can be used to update the services since the --force flag will replace the existing services with the new ones.

## Versioning

Each of the deploymnets use semantic versioning. The buildspec.yml files contain the logic to automatically update the build version. Minor and major versions are updated manually in the buildspec files.
