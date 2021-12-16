#!/usr/bin/env sh

set -xe

alembic revision --autogenerate -m "Add user table"
alembic upgrade head
python create_users.py
