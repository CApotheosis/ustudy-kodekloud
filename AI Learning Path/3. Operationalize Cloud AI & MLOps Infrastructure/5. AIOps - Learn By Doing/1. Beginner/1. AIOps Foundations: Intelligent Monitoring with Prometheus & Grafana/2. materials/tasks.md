## Welcome to Module 2: Collecting the Data Fuel
🎯 What You'll Learn
In this lab, you'll master the foundation of observability: configuring Prometheus to collect metrics. You'll learn the pull-based scrape model, edit configuration files, deploy a Node Exporter for system metrics, and verify that data is flowing correctly into your time-series database.

📚 Lab Journey
Understand the Prometheus pull model and exposition format
Edit prometheus.yml to define scrape targets
Deploy Prometheus and Node Exporter with Docker Compose
Verify targets are UP and metrics are flowing
Query collected metrics using the Prometheus expression browser
💡 Key Concepts
This lab builds the data foundation for AIOps. Without reliable metrics collection, AI models have nothing to analyze. You're learning the critical first step that enables all intelligent operations.

---

## Understanding the Prometheus Pull Model
How Prometheus Collects Metrics
Unlike traditional monitoring systems where agents push data to a central server, Prometheus uses a pull-based model. This means Prometheus actively scrapes (fetches) metrics from targets on a regular schedule.

The Pull Model Workflow
Targets expose HTTP endpoints (e.g., http://target:9090/metrics)
Prometheus scrapes these endpoints every scrape_interval (e.g., 15 seconds)
Metrics are parsed and stored in Prometheus's time-series database
Health checks track whether each target is UP or DOWN
✅ Advantages of the Pull Model
Prometheus controls timing - No "thundering herd" of agents reporting simultaneously
Service discovery - Prometheus can automatically find new targets as infrastructure scales
Simpler targets - Just expose an HTTP endpoint, no complex client libraries needed
Centralized configuration - All scrape settings in one place (prometheus.yml)
Network resilience - Prometheus retries failed scrapes automatically

---

##

---

##

---

## 