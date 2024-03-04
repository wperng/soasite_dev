import logging

logger = logging.getLogger("test")

def my_cron_job():
    print("test")
    logger.info("crob job is called")