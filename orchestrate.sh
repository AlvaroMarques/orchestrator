#!/usr/bin/bash
tmpdir=$(mktemp -d)
metadata="metadata.json"
number_of_files=2
prompt_basename="01.md"

# First project, 
uv run --project=scraper cvm $number_of_files $tmpdir $metadata
echo "saved on $tmpdir"
uv run --project=ai-journal-api api $prompt_basename "$tmpdir/$metadata" "$tmpdir/output.json"
