#!/usr/bin/env bash
# Run FII/DII Dashboard with clean Python path to avoid hermes venv contamination
cd "$(dirname "$0")" && PYTHONPATH="" streamlit run app.py
