#!/bin/sh

PORT=8082 docker-compose  --env-file .env -f docker/docker-compose.yml up --force-recreate --build