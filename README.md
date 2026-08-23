# 🛡️ ScrapeVerse: The Self-Healing Indie Game & Price Tracker

An intelligent, resilient web scraping tool built for the **Into the Scrape-Verse** hackathon (Powered by Bright Data).

## 💡 The Problem
Traditional web scrapers break the moment a website updates its layout, changes a CSS class, or alters HTML tags. Maintenance costs soar, and data pipelines fail.

## 🚀 Our Solution
**ScrapeVerse** features an integrated **AI Self-Healing Layer** (`ai_healer.py`). When a primary target selector fails or returns empty data, the system automatically detects the anomaly, analyzes the DOM structure, and executes smart fallback extraction patterns (like regex-based recovery) to keep data flowing seamlessly without crashing.

## 🛠️ Tech Stack
* **Python** (Core Logic)
* **Bright Data Proxy Infrastructure** (Anti-blocking & robust data gathering)
* **Custom AI Healer Engine** (Automated layout error-recovery)

## 🚀 Production Workflow
This project utilizes the **Bright Data CLI** for reliable, scalable data collection.
- **Authentication:** Authenticated via `bdata login --device` for secure cloud environment access.
- **Scraper Infrastructure:** Created using AI-powered `bdata scraper create`.
- **Execution:** Automated execution via `run_scraper.sh` using the official Collector ID.
- **Self-Healing:** Built to support `bdata scraper heal` to handle future website structural changes.

## ⚡ How to Run
1. Clone the repository:
   ```bash
   git clone [https://github.com/cruse1914/indie-game-tracker.git](https://github.com/cruse1914/indie-game-tracker.git)
   cd indie-game-tracker
