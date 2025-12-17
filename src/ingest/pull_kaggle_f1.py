from __future__ import annotations

import shutil
import subprocess
from datetime import datetime
from pathlib import Path


DATASET_SLUG = "jtrotman/formula-1-race-data"


def run(cmd: list[str]) -> None:
    """Run a command and raise a helpful error if it fails."""
    result = subprocess.run(cmd, capture_output=True, text=True, shell=False)
    if result.returncode != 0:
        raise RuntimeError(
            "Command failed:\n"
            f"  {' '.join(cmd)}\n\n"
            "STDOUT:\n"
            f"{result.stdout}\n\n"
            "STDERR:\n"
            f"{result.stderr}"
        )


def main() -> None:
    # Create a dated folder for each pull (raw data versioning)
    run_date = datetime.utcnow().strftime("%Y-%m-%d")
    raw_dir = Path("data") / "raw" / run_date
    extract_dir = raw_dir / "files"

    # Start fresh if you re-run on the same day
    if raw_dir.exists():
        shutil.rmtree(raw_dir)

    extract_dir.mkdir(parents=True, exist_ok=True)

    # Download + unzip with Kaggle CLI
    run(
        [
            "kaggle",
            "datasets",
            "download",
            "-d",
            DATASET_SLUG,
            "-p",
            str(extract_dir),
            "--unzip",
        ]
    )

    # Print a simple summary
    files = sorted([p for p in extract_dir.glob("*.csv") if p.is_file()])

    print("\n✅ Ingestion complete")
    print(f"Dataset: {DATASET_SLUG}")
    print(f"Output:  {extract_dir.resolve()}")
    print(f"Files:   {len(files)}")

    for f in files:
        size_mb = f.stat().st_size / (1024 * 1024)
        print(f" - {f.name} ({size_mb:.2f} MB)")

    if len(files) == 0:
        print("\n⚠️ No CSV files found. Check dataset contents or download location.")


if __name__ == "__main__":
    main()