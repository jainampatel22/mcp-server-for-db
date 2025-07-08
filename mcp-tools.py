# mcp.py
from mcp.server.fastmcp import FastMCP
import os
import json
from tool import delete, createTable
from dotenv import load_dotenv

load_dotenv()

DB_URL = os.getenv("DATABASE_URL")

mcp = FastMCP("DEMO")

@mcp.tool()
def create() -> str:
    """Create a table if it does not exist"""
    createTable()
    return 'Table created successfully'

@mcp.tool()
def drop() -> str:
    """Delete a row from the table using id"""
    try:
        delete()
        return f"Row with  deleted."
    except Exception as e:
        return f"Error deleting row: {str(e)}"

