#!/usr/bin/env python3

import json
import sys
import subprocess
import time

def send_mcp_message(message):
    """Send a message to the MCP server and return the response."""
    # Convert the message to JSON
    message_json = json.dumps(message)
    
    # Create a subprocess to run the server
    process = subprocess.Popen(
        ["python3", "src/notification_server.py"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    
    # Send the message to the server
    process.stdin.write(message_json + "\n")
    process.stdin.flush()
    
    # Read the response
    response_json = process.stdout.readline()
    
    # Parse the response
    try:
        response = json.loads(response_json)
    except json.JSONDecodeError:
        response = {"error": "Failed to parse response"}
    
    # Terminate the process
    process.terminate()
    
    return response

def main():
    # Initialize the server
    init_message = {
        "type": "initialize",
        "options": {}
    }
    
    init_response = send_mcp_message(init_message)
    print("Initialization response:", init_response)
    
    # List available tools
    list_tools_message = {
        "type": "listTools"
    }
    
    list_tools_response = send_mcp_message(list_tools_message)
    print("List tools response:", list_tools_response)
    
    # Call the send_notification tool
    call_tool_message = {
        "type": "callTool",
        "name": "send_notification",
        "arguments": {
            "title": "Test Notification",
            "message": "This is a test notification from the MCP server",
            "subtitle": "MCP Test"
        }
    }
    
    call_tool_response = send_mcp_message(call_tool_message)
    print("Call tool response:", call_tool_response)

if __name__ == "__main__":
    main() 