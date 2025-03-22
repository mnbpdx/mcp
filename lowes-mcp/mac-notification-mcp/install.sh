#!/bin/bash

# Mac Notification MCP Server Installer
# This script installs and configures the Mac Notification MCP server for Claude Desktop

# Get the absolute path of the script directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Make the notification server executable
chmod +x "$SCRIPT_DIR/src/notification_server.py"

# Check if Claude Desktop is installed
CLAUDE_APP_SUPPORT="$HOME/Library/Application Support/Claude"
CLAUDE_CONFIG="$CLAUDE_APP_SUPPORT/config.json"

if [ ! -d "$CLAUDE_APP_SUPPORT" ]; then
  echo "Claude Desktop doesn't appear to be installed or hasn't been run yet."
  echo "Please install Claude Desktop and run it at least once before continuing."
  exit 1
fi

# Create or update the Claude Desktop config
if [ -f "$CLAUDE_CONFIG" ]; then
  # Config exists, check if it already has our server
  if grep -q "mac-notification" "$CLAUDE_CONFIG"; then
    echo "Mac Notification MCP server is already configured in Claude Desktop."
  else
    # Backup the existing config
    cp "$CLAUDE_CONFIG" "$CLAUDE_CONFIG.bak"
    echo "Backed up existing Claude Desktop config to $CLAUDE_CONFIG.bak"
    
    # Update the config to add our server
    # This is a simple approach that might not work for all config files
    # A more robust approach would use jq or a similar tool
    if grep -q "\"mcpServers\"" "$CLAUDE_CONFIG"; then
      # mcpServers section exists, add our server to it
      sed -i '' -e '/"mcpServers"[[:space:]]*:[[:space:]]*{/ a\
    "mac-notification": {\
      "command": "python3",\
      "args": ["'"$SCRIPT_DIR"'/src/notification_server.py"]\
    },
' "$CLAUDE_CONFIG"
    else
      # mcpServers section doesn't exist, add it
      sed -i '' -e '/{/ a\
  "mcpServers": {\
    "mac-notification": {\
      "command": "python3",\
      "args": ["'"$SCRIPT_DIR"'/src/notification_server.py"]\
    }\
  },
' "$CLAUDE_CONFIG"
    fi
    
    echo "Added Mac Notification MCP server to Claude Desktop config."
  fi
else
  # Create a new config file
  mkdir -p "$CLAUDE_APP_SUPPORT"
  cat > "$CLAUDE_CONFIG" << EOF
{
  "mcpServers": {
    "mac-notification": {
      "command": "python3",
      "args": ["$SCRIPT_DIR/src/notification_server.py"]
    }
  }
}
EOF
  echo "Created new Claude Desktop config with Mac Notification MCP server."
fi

echo "Installation complete!"
echo "You may need to restart Claude Desktop for the changes to take effect."
echo ""
echo "To test the notification server, run:"
echo "python3 $SCRIPT_DIR/test_notification.py" 