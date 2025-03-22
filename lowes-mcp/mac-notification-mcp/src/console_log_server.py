#!/usr/bin/env python3

import asyncio
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger("mac-notification-mcp")

async def log_to_console(title: str, message: str, subtitle: str = None):
    """Log a message to the console."""
    try:
        # Log the message details
        logger.info("=" * 50)
        logger.info(f"Title: {title}")
        if subtitle:
            logger.info(f"Subtitle: {subtitle}")
        logger.info(f"Message: {message}")
        logger.info("=" * 50)
        return True
            
    except Exception as e:
        logger.exception("Error logging message")
        return False

async def main():
    """Test the console logging functionality."""
    # Test logging
    await log_to_console(
        title="Test Console Log",
        message="This is a test message",
        subtitle="Test Subtitle"
    )

if __name__ == "__main__":
    asyncio.run(main()) 