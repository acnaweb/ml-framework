"""
General app's level configuration items.
"""

import logging

RAW_DATASET = "data/raw/dataset.csv"
PROCESSED_DATASET = "data/processed/dataset.csv"
RAW_REPORT_PROFILER = "reports/profiler_raw.html"
PROCESSED_REPORT_PROFILER = "reports/profiler_processed.html"
CREATE_PROFILER = True


def print_settings():
    logging.info("*** dataset settings ***")

    logging.info("RAW_DATASET={}".format(RAW_DATASET))
    logging.info("PROCESSED_DATASET={}".format(PROCESSED_DATASET))
    logging.info("CREATE_PROFILER={}".format(CREATE_PROFILER))
    logging.info("PROCESSED_REPORT_PROFILER={}".format(PROCESSED_REPORT_PROFILER))
    logging.info("RAW_REPORT_PROFILER={}".format(RAW_REPORT_PROFILER))
