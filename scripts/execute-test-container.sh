#!/bin/sh
PORT=8082 docker-compose -f docker/execute-test-compose.yml up --force-recreate --build --remove-orphans --abort-on-container-exit