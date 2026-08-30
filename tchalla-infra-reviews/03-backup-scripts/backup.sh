#!/bin/bash
# backup.sh — PostgreSQL Automated Backup Script
# Team Iron SRE — Production

set -e

# ⚠️ ISSUE: Credentials hardcoded — use AWS Secrets Manager / env injection
DB_HOST="prod-rds.cluster-abc123.us-east-1.rds.amazonaws.com"
DB_USER="postgres"
DB_PASSWORD="Sup3rS3cur3P@ss!"
DB_NAME="openjarvis_prod"
BACKUP_BUCKET="s3://team-iron-backups/postgres"
RETENTION_DAYS=30

TIMESTAMP=$(date +%Y%m%d_%H%M%S)
BACKUP_FILE="/tmp/backup_${DB_NAME}_${TIMESTAMP}.sql.gz"

log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Create backup
log "Starting backup of ${DB_NAME}..."
PGPASSWORD="${DB_PASSWORD}" pg_dump \
    -h "${DB_HOST}" \
    -U "${DB_USER}" \
    -d "${DB_NAME}" \
    --format=plain \
    --no-password \
    --verbose \
    | gzip > "${BACKUP_FILE}"

log "Backup created: ${BACKUP_FILE} ($(du -sh ${BACKUP_FILE} | cut -f1))"

# Upload to S3
log "Uploading to ${BACKUP_BUCKET}..."
aws s3 cp "${BACKUP_FILE}" "${BACKUP_BUCKET}/$(basename ${BACKUP_FILE})" \
    --storage-class STANDARD_IA

# ⚠️ ISSUE: No verification that upload succeeded
# Should verify: aws s3api head-object --bucket ... --key ...

log "Upload complete. Cleaning up local file..."
rm -f "${BACKUP_FILE}"

# Cleanup old backups
log "Removing backups older than ${RETENTION_DAYS} days..."
aws s3 ls "${BACKUP_BUCKET}/" \
    | awk '{print $4}' \
    | while read file; do
        file_date=$(echo "${file}" | grep -oP '\d{8}')
        if [[ -n "${file_date}" ]]; then
            file_epoch=$(date -d "${file_date}" +%s 2>/dev/null || \
                         date -j -f "%Y%m%d" "${file_date}" +%s 2>/dev/null)
            cutoff_epoch=$(date -d "-${RETENTION_DAYS} days" +%s 2>/dev/null || \
                           date -v-${RETENTION_DAYS}d +%s 2>/dev/null)
            if [[ "${file_epoch}" -lt "${cutoff_epoch}" ]]; then
                log "Deleting old backup: ${file}"
                aws s3 rm "${BACKUP_BUCKET}/${file}"
            fi
        fi
    done

log "Backup process complete."
# ⚠️ ISSUE: No notification on failure — needs SNS/PagerDuty alert on exit code != 0
