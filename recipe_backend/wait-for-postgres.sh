# /bin/bash^M: bad interpreter: No such file or directory - Unix line endings
#! /bin/bash
# wait-for-postgres.sh

set -e

host="$1"

until psql -h "$host" -U "postgres" -c '\q'; do
    >&2 echo "Postgres is unavailable - sleeping"
    sleep 1
done