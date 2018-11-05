#!/usr/bin/env bash

if [ "$SLAMBOOK_ENV" = "Test" ]; then
    psql -U postgres -p 9011 -c "drop database slambook_test"
    psql -U postgres -p 9011 -c "create database slambook_test owner slambook;"
    psql -U postgres -p 9011 -d slambook_test -c "create extension postgis; create extension tablefunc; CREATE EXTENSION pg_trgm;"
    export SMARTCOOK_ENV=Test
else
    psql -U postgres -p 9011 -c "drop database slambook_dev"
    psql -U postgres -p 9011 -c "create database slambook_dev owner slambook;"
    psql -U postgres -p 9011 -d slambook_dev -c "create extension postgis; create extension tablefunc; CREATE EXTENSION pg_trgm;"
    export SMARTCOOK_ENV=Dev
fi