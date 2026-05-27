# Smart Monitoring System

## Project Overview

This project is a real-time smart monitoring system using:

- Python
- FastAPI
- Apache Kafka
- AI Analysis Service
- Docker Containers

The system simulates sensor telemetry data,
streams it through Kafka,
analyzes it using AI,
and displays alerts in real time.

---

# Architecture

Sensor Simulator
↓
Kafka Producer
↓
Kafka Topic
↓
FastAPI Consumer
↓
AI Analysis Service
↓
Dashboard / Alerts / API

---

# Technologies Used

- Python
- FastAPI
- Apache Kafka
- Docker
- REST API
- AI Processing

---

# Project Structure

smart-monitoring-system/
│
├── api/
│   ├── main.py
│   ├── consumer.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── ai_service/
│   ├── ai_service.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── producer/
│   └── producer.py
│
├── dashboard/
│   └── dashboard.py
│
├── docker-compose.yml
│
└── README.md

---

# Installation

## 1. Clone Project

```bash
git clone <your-repo-url>
cd smart-monitoring-system