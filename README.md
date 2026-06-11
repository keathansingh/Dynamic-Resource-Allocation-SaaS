# Dynamic Resource Allocation for SaaS Applications

## Overview
This project demonstrates dynamic CPU resource allocation in a multi-tenant SaaS environment using Docker containers and Python.

## Problem Statement
In multi-tenant environments, one tenant may consume excessive resources and affect other tenants, leading to the Noisy Neighbor Problem.

## Solution
A Python-based Nano Controller continuously monitors CPU utilization of Docker containers and dynamically adjusts CPU allocation based on workload demand.

## Technologies Used
- Docker
- Python
- WSL2 Ubuntu
- Pandas
- Matplotlib
- Linux Stress Tool

## Features
- Multi-tenant container environment
- Real-time CPU monitoring
- Dynamic CPU allocation
- CPU usage logging
- Graph visualization
- Noisy Neighbor Problem mitigation

## Project Workflow
1. Create tenant containers.
2. Monitor CPU usage.
3. Apply stress workload.
4. Dynamically adjust CPU resources.
5. Log CPU data.
6. Generate performance graphs.

## Results
The system successfully allocates CPU resources based on workload demand and improves resource utilization in a shared environment.
