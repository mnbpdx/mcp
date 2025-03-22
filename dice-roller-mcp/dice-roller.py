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
mcp = FastMCP("dice-roller")

@mcp.tool()
def roll_dice(sides: int) -> int:
    """
    Roll a dice with the specified number of sides.
    
    Args:
        sides (int): The number of sides on the dice. Must be a positive integer.
        
    Returns:
        int: A random number between 1 and the number of sides, inclusive.
        
    Raises:
        ValueError: If sides is less than 1.
    """
    import random
    
    if sides < 1:
        raise ValueError("Number of sides must be at least 1")
    
    return random.randint(1, sides)

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')