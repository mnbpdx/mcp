#!/usr/bin/env python3

import subprocess
import asyncio
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger("mac-notification-mcp")

async def send_notification(title: str, message: str, subtitle: str = None):
    """Send a notification to macOS Notification Center."""
    try:
        # Log the notification details
        logger.info(f"Sending notification:")
        logger.info(f"Title: {title}")
        logger.info(f"Message: {message}")
        if subtitle:
            logger.info(f"Subtitle: {subtitle}")

        # Escape double quotes
        message = message.replace('"', '\\"')
        title = title.replace('"', '\\"')
        if subtitle:
            subtitle = subtitle.replace('"', '\\"')
        
        # Build the AppleScript command
        applescript = f'display notification "{message}"'
        if title:
            applescript += f' with title "{title}"'
        if subtitle:
            applescript += f' subtitle "{subtitle}"'
        
        # Execute the AppleScript command
        process = await asyncio.create_subprocess_exec(
            'osascript', '-e', applescript,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        
        stdout, stderr = await process.communicate()
        
        if process.returncode != 0:
            error_msg = stderr.decode().strip()
            logger.error(f"Failed to send notification: {error_msg}")
            return False
        
        logger.info("Notification sent successfully")
        return True
            
    except Exception as e:
        logger.exception("Error sending notification")
        return False

async def main():
    """Test the notification functionality."""
    # Test notification
    await send_notification(
        title="Test Notification",
        message="This is a test message",
        subtitle="Test Subtitle"
    )

if __name__ == "__main__":
    asyncio.run(main()) 