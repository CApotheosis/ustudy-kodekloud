# MLOps for AIOps: Build, Track, and Orchestrate AI Models with MLflow & Kubeflow

- Source: https://kodekloud.com/courses/mlops-for-aiops-build-track-and-orchestrate-ai-models-with-mlflow-kubeflow
- Part of: AIOps - Learn By Doing learning path (Advanced tier)
- Fetched: 2026-09-05
- Status at fetch time: not yet released ("get a notification when course is released")

## Metadata

- Level: Advanced (per parent learning-path grouping); page copy suggests intermediate difficulty given prerequisites
- Modules: 4
- Topics: 9 total
- Duration: not specified on the page
- Course includes: Certificate, Cloud Labs, Story format, Videos, Case Studies, Demos, Labs, Mock Exams, Quizzes, Discord Community Support
- Categories/Tags: AI, DevOps, Learn by Doing; also tagged MLflow, MinIO, Kubeflow, AIOps Pipelines (from learning-path card)
- Instructor: Nourhan Mohamed — DevOps Lead | Cloud Native Enthusiast | Golden Kubestronaut; DevOps Instructor at KodeKloud specializing in Kubernetes, Docker, CI/CD, cloud-native tech
- Ratings/students: none shown

## Overview

Helps learners move beyond ad-hoc notebooks toward production-style MLOps workflows tailored for AIOps use cases such as anomaly detection, using MLflow and Kubeflow Pipelines on Kubernetes to build reproducible, trackable, and deployable models.

## Requirements

- Python Basics
- Kubernetes Basics
- Machine Learning Fundamentals

## Course Content

### Module 1: Why MLOps Is Critical for AIOps (1 topic)
- From Notebook to Production — Lab 1.1: convert an anomaly detection notebook into a `train.py` script; add CLI arguments, random seeds, reproducibility practices; run multiple configs manually.

### Module 2: Experiment Tracking & Model Packaging with MLflow (3 topics)
- Setting Up MLflow and MinIO — Lab 2.1: deploy MinIO/MLflow Tracking Server, verify UI/connectivity.
- Logging Parameters, Metrics and Artifacts — Lab 2.2: instrument `train.py` with MLflow Tracking API, explore MLflow UI.
- Packaging Models For Reproducibility — Lab 2.3: create `MLproject` and `conda.yaml`, define entry points, re-run via MLflow CLI.

### Module 3: Deploying & Serving AIOps Models (2 topics)
- Serving Models With MLflow — Lab 3.1: serve model locally, register in Model Registry, test via curl/Python requests.
- Containerizing and Deploying to Kubernetes — Lab 3.2: Dockerize serving app, deploy via Kubernetes Deployment/Service, verify REST API access.

### Module 4: Orchestrating AIOps Pipelines with Kubeflow (3 topics)
- Exploring Kubeflow Pipelines — Lab 4.1: access UI, inspect/run sample pipelines, view execution graphs.
- Building the Training & Registration Components — Lab 4.2: create train/register components, run 2-step pipeline.
- Building the Full Train → Validate → Deploy Pipeline — Lab 4.3: add validate/deploy components, compile/upload/trigger 4-step pipeline.
