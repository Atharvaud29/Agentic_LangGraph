from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Math")

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two integers."""
    return a + b

@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two integers."""
    return a * b

#the transport="stdio" tells the server to:
# use standard input/output(stdin and stdout) to recive & respond to tool function calls

if __name__ == "__main__":
    mcp.run(transport = "stdio")