FROM postgres:16

# Set default values for environment variables for PostgreSQL
ENV POSTGRES_USER=devuser \
    POSTGRES_PASSWORD=devpass \
    POSTGRES_DB=devdb \
    PGDATA=/var/lib/postgresql/data/pgdata

# Ensure the data directory exists and has the correct permissions
COPY conf/postgresql.conf /etc/postgresql/postgresql.conf

# Adjust PostgreSQL configuration to use the custom config file
COPY init/*.sql /docker-entrypoint-initdb.d/

#Simple health check
HEALTHCHECK --interval=10s --timeout=5s --retries=10 \
    CMD pg_isready -U "$POSTGRES_USER" -d "$POSTGRES_DB" || exit 1

# Use original entrypoint and command, but with custom config file
CMD ["postgres", "-c", "config_file=/etc/postgresql/postgresql.conf"]
