# Mac Notification MCP Server

A simple Model Context Protocol (MCP) server that allows AI assistants to send notifications to macOS Notification Center.

## Features

- Send notifications to macOS Notification Center
- Customize notification title, message, and subtitle
- Simple integration with Claude and other MCP-compatible assistants

## Requirements

- macOS (tested on macOS Ventura and later)
- Python 3.7 or higher

## Installation

1. Clone this repository or download the source code
2. Make the script executable:

```bash
chmod +x src/notification_server.py
```

## Usage

### Running the Server

You can run the server directly:

```bash
python3 src/notification_server.py
```

### Configuring with Claude Desktop

To use this server with Claude Desktop, add the following to your Claude Desktop configuration:

```json
{
  "mcpServers": {
    "mac-notification": {
      "command": "python3",
      "args": ["/path/to/mac-notification-mcp/src/notification_server.py"]
    }
  }
}
```

Replace `/path/to/mac-notification-mcp` with the actual path to the directory containing the server code.

### Using with Claude

Once configured, you can ask Claude to send notifications. For example:

"Please send me a notification with the title 'Reminder' and the message 'Time to take a break!'"

Claude will use the MCP server to send the notification to your macOS Notification Center.

## Tool Documentation

The server provides the following tool:

### send_notification

Sends a notification to macOS Notification Center.

**Parameters:**
- `title` (required): The title of the notification
- `message` (required): The message body of the notification
- `subtitle` (optional): A subtitle for the notification

## Troubleshooting

If you encounter issues:

1. Make sure the script has execute permissions
2. Check that macOS allows notifications from the terminal/script
3. Verify that the path in your Claude Desktop configuration is correct

## License

MIT License 