from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Weather")

@mcp.tool()
async def get_weather(city: str) -> str:
    """Get the current weather for a given city."""
    # Simulate fetching weather data
    # In a real application, you would call an external API to get the weather data
    return f"The current weather in {city} is sunny with a temperature of 25°C."

if __name__ == "__main__":
    mcp.run(transport = "streamable-http")