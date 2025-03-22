from typing import Any
import requests
from mcp.server.fastmcp import FastMCP
import os
from dotenv import load_dotenv
from mcp import types
from pprint import pprint, pformat

# Load environment variables
load_dotenv()

# initialize FastMCP server
mcp = FastMCP("price")

@mcp.tool()
def amazon_search(
    query: str,
    domain: str = "com",
    start_page: int = 1,
    pages: int = 1
) -> list[types.TextContent]:
    """
    Query Amazon search results using the Oxylabs API.
    
    Args:
        query (str): The search query
        domain (str): The Amazon domain (e.g., 'com', 'nl', 'de')
        start_page (int): The starting page number for results
        pages (int): Number of pages to fetch
        
    Returns:
        list[types.TextContent]: The search results from Amazon formatted as MCP content
        
    Raises:
        ValueError: If the API credentials are not set
        requests.RequestException: If the API request fails
    """
    username = os.getenv("OXYLABS_USERNAME")
    password = os.getenv("OXYLABS_PASSWORD")
    
    if not username or not password:
        raise ValueError("OXYLABS_USERNAME and OXYLABS_PASSWORD environment variables must be set")
    
    payload = {
        'source': 'amazon_search',
        'domain': domain,
        'query': query,
        'start_page': start_page,
        'pages': pages,
        'parse': True
    }
    
    try:
        response = requests.post(
            'https://realtime.oxylabs.io/v1/queries',
            auth=(username, password),
            json=payload
        )
        response.raise_for_status()
        result = response.json()
        
        # Format the result as a readable string
        formatted_result = pformat(result, indent=2)
        return [
            types.TextContent(
                type="text",
                text=f"Amazon search results for query '{query}':\n\n{formatted_result}"
            )
        ]
    except requests.RequestException as e:
        raise requests.RequestException(f"Failed to fetch Amazon search data: {str(e)}")

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')
