# Scripts

This directory contains utility scripts and sample scripts related to the AutoMashupper project.

## audascript.py

A script for testing Audacity's script pipe functionality.

### Usage

1. Start Audacity and enable mod-script-pipe
2. Prepare a CSV file (must contain a `file` column with audio file paths)
3. Run the script:

```bash
python scripts/audascript.py <csv_file>
```

### Requirements

- Audacity must be running
- mod-script-pipe feature must be enabled
- Python 2.7 or later (Python 3 strongly recommended)
