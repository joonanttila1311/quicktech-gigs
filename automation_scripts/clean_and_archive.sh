#!/bin/bash
TARGET_DIR="${1:-./sample_folder}"
ARCHIVE_DIR="$TARGET_DIR/archive_$(date +%Y%m%d)"
mkdir -p "$ARCHIVE_DIR"
find "$TARGET_DIR" -type f -empty -delete
find "$TARGET_DIR" -type f -mtime +30 -not -path "$ARCHIVE_DIR/*" -exec mv {} "$ARCHIVE_DIR" \;
find "$TARGET_DIR" -type f | while read f; do
  newname="$(echo "$f" | sed 's/ /_/g')"
  [ "$f" != "$newname" ] && mv "$f" "$newname"
done
echo "✅ Cleanup complete. Archived files moved to $ARCHIVE_DIR"
