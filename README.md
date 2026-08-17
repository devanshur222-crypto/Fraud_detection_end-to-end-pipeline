# Real-Time Fraud Detection with End-to-End MLOps

> ⚠️ **Status: Work in Progress.** This repository is being built incrementally as part of a hands-on MLOps learning project. This README will evolve as each stage (data, training, serving, monitoring) is completed.

## Overview

This project implements a **fraud detection system** for online (card-not-present) e-commerce transactions, built around the [IEEE-CIS Fraud Detection dataset](https://www.kaggle.com/c/ieee-fraud-detection) from Vesta Corporation.

The goal isn't just to train an accurate model — it's to build the **full MLOps lifecycle** around it: data versioning, experiment tracking, reproducible pipelines, containerized deployment, real-time inference simulation, and drift monitoring.

## Problem Statement

Given a transaction's payment, device, and behavioral data, predict the probability that it is **fraudulent**. This is a binary classification problem with significant real-world constraints:

- **Severe class imbalance** — only ~3.5% of transactions are fraudulent
- **Time-ordered data** — patterns must be learned from the past and generalized to the future, not shuffled randomly
- **High-dimensional, partially anonymized features** — 434+ raw columns including masked/engineered signals, requiring genuine feature selection rather than relying on human-readable fields alone
- **Structural missingness** — identity and device data isn't always captured, mirroring real production data quality issues

## Why This Project

Most portfolio ML projects stop at "trained a model, got X% accuracy." This project intentionally keeps the modeling side simple (gradient-boosted trees, not exotic architectures) so the focus stays on what actually matters in production ML systems:

- Reproducible, versioned data and experiments
- Automated CI/CD for training and deployment
- Real-time-style inference via simulated transaction streaming
- Live monitoring for data drift and model degradation
- Clean, documented infrastructure a real team could hand off and maintain

## Planned Architecture

```
Raw Data (IEEE-CIS, versioned with DVC)
        │
        ▼
Preprocessing & Feature Engineering
        │
        ▼
Training (XGBoost/LightGBM, tracked with MLflow)
        │
        ▼
Model Registry (MLflow)
        │
        ▼
CI/CD (GitHub Actions) → Docker Image
        │
        ▼
Serving (FastAPI + Docker)
        │
        ▼
Simulated Real-Time Stream (Kafka/Redpanda replay of historical data)
        │
        ▼
Monitoring & Drift Detection (Evidently AI) → Dashboard (Streamlit/Grafana)
        │
        ▼
Retraining Trigger (Prefect)
```

## Tech Stack (planned)

| Layer | Tool |
|---|---|
| Data & model versioning | DVC |
| Experiment tracking | MLflow |
| Feature store | Feast *(stretch goal)* |
| Streaming simulation | Kafka / Redpanda |
| Modeling | XGBoost / LightGBM |
| Serving | FastAPI |
| Containerization | Docker, Docker Compose |
| CI/CD | GitHub Actions |
| Monitoring | Evidently AI |
| Dashboard | Streamlit or Grafana |
| Orchestration | Prefect |

## Dataset

- **Source:** [IEEE-CIS Fraud Detection (Kaggle)](https://www.kaggle.com/c/ieee-fraud-detection)
- **Size:** ~590,540 transactions, 434 columns (after joining `train_transaction.csv` and `train_identity.csv` on `TransactionID`)
- **Target:** `isFraud` (binary)
- Not included in this repository due to size/license — see `data/README.md` (TODO) for download instructions.

## Repository Structure

```
.
├── data/               # (gitignored) raw & processed data, tracked via DVC
├── notebooks/          # exploratory analysis
├── src/
│   ├── data/           # data loading & preprocessing scripts
│   ├── features/       # feature engineering
│   ├── models/         # training scripts
│   └── serving/        # FastAPI inference app
├── pipelines/          # Prefect flows
├── docker/             # Dockerfiles, docker-compose
├── monitoring/         # Evidently reports/config
├── .github/workflows/  # CI/CD pipelines
├── tests/
└── README.md
```
*(structure will be updated as the project develops)*

## Current Progress

- [x] Dataset selected and understood (EDA in progress)
- [ ] Data versioning setup (DVC)
- [ ] Baseline model + experiment tracking (MLflow)
- [ ] Feature engineering pipeline
- [ ] Model serving API (FastAPI + Docker)
- [ ] CI/CD pipeline
- [ ] Streaming simulation
- [ ] Drift monitoring & dashboard
- [ ] Automated retraining trigger

## Status

Actively in development — this is a learning-in-public project documenting a full MLOps build from data to deployment.

## License

TBD
