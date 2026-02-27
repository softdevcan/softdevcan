#!/bin/bash
# PostgreSQL and media backup script for softdevcan
# Usage: Run via cron: 0 3 * * * /srv/app/scripts/backup.sh

set -e

# Configuration - uses docker compose to find containers dynamically
COMPOSE_PROJECT="${COMPOSE_PROJECT_NAME:-softdevcan}"
BACKUP_DIR="/srv/backups/postgres"
MEDIA_BACKUP_DIR="/srv/backups/media"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
RETENTION_DAYS=30

# Database credentials from environment or defaults
DB_NAME="${POSTGRES_DB:-resume_db}"
DB_USER="${POSTGRES_USER:-resume_user}"

# Create backup directories if not exists
mkdir -p "$BACKUP_DIR"
mkdir -p "$MEDIA_BACKUP_DIR"

# Database backup using docker compose exec
echo "[$(date)] Starting database backup..."
docker compose -p "$COMPOSE_PROJECT" exec -T postgres pg_dump -U "$DB_USER" "$DB_NAME" | gzip > "$BACKUP_DIR/db_${TIMESTAMP}.sql.gz"
echo "[$(date)] Database backup completed: db_${TIMESTAMP}.sql.gz"

# Media backup
echo "[$(date)] Starting media backup..."
docker compose -p "$COMPOSE_PROJECT" cp app:/srv/app/media "$MEDIA_BACKUP_DIR/media_${TIMESTAMP}"
tar -czf "$MEDIA_BACKUP_DIR/media_${TIMESTAMP}.tar.gz" -C "$MEDIA_BACKUP_DIR" "media_${TIMESTAMP}"
rm -rf "$MEDIA_BACKUP_DIR/media_${TIMESTAMP}"
echo "[$(date)] Media backup completed: media_${TIMESTAMP}.tar.gz"

# Cleanup old backups
find "$BACKUP_DIR" -name "db_*.sql.gz" -mtime +$RETENTION_DAYS -delete
find "$MEDIA_BACKUP_DIR" -name "media_*.tar.gz" -mtime +$RETENTION_DAYS -delete

echo "[$(date)] Backup process completed. Old backups (>${RETENTION_DAYS} days) cleaned up."
