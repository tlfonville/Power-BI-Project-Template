#-------------------------------------------------------------------------------
# exampleScript.py
# Author Name
# Version 1.0 | Standard project script structure example
#-------------------------------------------------------------------------------
#
# Purpose:
#   Demonstrates the standard Python script structure for team Power BI projects.
#
#   This script is intentionally simple and can be used as a template for:
#     - Data extraction scripts
#     - File cleanup scripts
#     - API pull scripts
#     - Report prep scripts
#     - Scheduled automation scripts
#
# Output:
#   data/ExampleOutput.xlsx
#
# Columns:
#   Report Date, Source System, Category, Metric Name, Metric Value, Notes

# =============================================================================
# IMPORTS
# =============================================================================

import os
from pathlib import Path
from datetime import datetime

import pandas as pd
from dotenv import load_dotenv


# =============================================================================
# CONFIGURATION
# =============================================================================

# Project folder structure:
#   project_root/
#       config/
#           .env
#       data/
#       src/
#           ExampleScript.py

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / "config" / ".env")

# --- Environment Variables ---
# Example only. Add real values to config/.env when needed.
ENVIRONMENT_NAME = os.getenv("ENVIRONMENT_NAME", "DEV")

# --- Output Configuration ---
OUTPUT_PATH = BASE_DIR / "data" / "ExampleOutput.xlsx"
OUTPUT_SHEET_NAME = "ExampleOutput"

# --- Script Configuration ---
SOURCE_SYSTEM = "Example System"
REPORT_DATE = datetime.now().strftime("%Y-%m-%d")


# =============================================================================
# HELPER FUNCTIONS
# =============================================================================

def ensure_output_folder_exists(output_path: Path) -> None:
    """
    Create the output folder if it does not already exist.
    """
    output_path.parent.mkdir(parents=True, exist_ok=True)


def validate_required_columns(df: pd.DataFrame, required_columns: list[str]) -> None:
    """
    Validate that the DataFrame contains all required columns.

    Fails clearly instead of allowing bad data to silently flow into Power BI.
    """
    missing_columns = [col for col in required_columns if col not in df.columns]

    if missing_columns:
        raise ValueError(f"Missing required columns: {missing_columns}")


def clean_text(value) -> str:
    """
    Standard text cleanup helper.

    Converts blanks/nulls to an empty string and trims extra spaces.
    """
    if pd.isna(value):
        return ""

    return str(value).strip()


# =============================================================================
# EXTRACT
# =============================================================================

def extract_data() -> list[dict]:
    """
    Extract source data.

    For this example, data is manually created.
    In a real script, this section could pull from:
      - Excel
      - CSV
      - SQL
      - SharePoint
      - An API
      - Another internal system
    """
    rows = [
        {
            "Report Date": REPORT_DATE,
            "Source System": SOURCE_SYSTEM,
            "Category": "Operations",
            "Metric Name": "Example Completed Tasks",
            "Metric Value": 25,
            "Notes": "Demo row for SOP structure.",
        },
        {
            "Report Date": REPORT_DATE,
            "Source System": SOURCE_SYSTEM,
            "Category": "Operations",
            "Metric Name": "Example Open Items",
            "Metric Value": 7,
            "Notes": "Demo row for SOP structure.",
        },
        {
            "Report Date": REPORT_DATE,
            "Source System": SOURCE_SYSTEM,
            "Category": "Quality",
            "Metric Name": "Example Accuracy Rate",
            "Metric Value": 98.5,
            "Notes": "Demo row for SOP structure.",
        },
    ]

    return rows


# =============================================================================
# TRANSFORM
# =============================================================================

def transform_data(rows: list[dict]) -> pd.DataFrame:
    """
    Transform extracted rows into a clean Power BI-ready DataFrame.
    """
    df = pd.DataFrame(rows)

    required_columns = [
        "Report Date",
        "Source System",
        "Category",
        "Metric Name",
        "Metric Value",
        "Notes",
    ]

    validate_required_columns(df, required_columns)

    # Standard cleanup
    df["Report Date"] = pd.to_datetime(df["Report Date"], errors="coerce").dt.date
    df["Source System"] = df["Source System"].apply(clean_text)
    df["Category"] = df["Category"].apply(clean_text)
    df["Metric Name"] = df["Metric Name"].apply(clean_text)
    df["Metric Value"] = pd.to_numeric(df["Metric Value"], errors="coerce").fillna(0)
    df["Notes"] = df["Notes"].apply(clean_text)

    # Sort output for consistent Power BI refresh behavior
    df = df.sort_values(
        by=["Report Date", "Source System", "Category", "Metric Name"],
        ascending=True,
    )

    return df


# =============================================================================
# LOAD / OUTPUT
# =============================================================================

def write_output_file(df: pd.DataFrame) -> None:
    """
    Write final output to Excel.

    Uses a temporary file first, then replaces the final file.
    This helps prevent a corrupted output file if the script fails during write.
    """
    ensure_output_folder_exists(OUTPUT_PATH)

    temp_output_path = OUTPUT_PATH.with_suffix(".tmp.xlsx")

    df.to_excel(
        temp_output_path,
        index=False,
        engine="openpyxl",
        sheet_name=OUTPUT_SHEET_NAME,
    )

    os.replace(temp_output_path, OUTPUT_PATH)

    print(f"Wrote {len(df)} rows.")
    print(f"Output saved to: {OUTPUT_PATH}")


# =============================================================================
# MAIN
# =============================================================================

def main() -> None:
    """
    Main script execution.
    """
    try:
        print("Starting example script...")
        print(f"Environment: {ENVIRONMENT_NAME}")

        rows = extract_data()
        df = transform_data(rows)

        if df.empty:
            print("No records returned. Nothing to write.")
            return

        write_output_file(df)

        print("Script completed successfully.")

    except Exception as error:
        print(f"Error during execution: {error}")
        raise


if __name__ == "__main__":
    main()
