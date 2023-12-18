#!/usr/bin/env bash

DB_NAME=initium_media_interview_db
createdb -U postgres ${DB_NAME}
pg_restore -U postgres -O -Fc --dbname=${DB_NAME} < /db/dev_data