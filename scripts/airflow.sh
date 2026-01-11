#!/usr/bin/env bash
set -e
export AIRFLOW_HOME="$(pwd)/.airflow"
export AIRFLOW__CORE__DAGS_FOLDER="$(pwd)/dags"
uv run airflow "$@"
