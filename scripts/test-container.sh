#!/bin/sh
PORT=8082 docker-compose -f docker/testdb-compose.yml up --force-recreate --build --remove-orphans