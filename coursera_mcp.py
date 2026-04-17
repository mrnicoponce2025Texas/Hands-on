from fastmcp import FastMCP
import httpx

mcp = FastMCP("coursera")

COURSERA_API = "https://api.coursera.org/api"


@mcp.tool()
async def search_courses(query: str, limit: int = 10) -> list[dict]:
    """Search Coursera course catalog by keyword."""
    async with httpx.AsyncClient() as client:
        resp = await client.get(
            f"{COURSERA_API}/courses.v1",
            params={
                "q": "search",
                "query": query,
                "limit": limit,
                "fields": "name,slug,description,partnerLogo",
            },
        )
        resp.raise_for_status()
        data = resp.json()
    return data.get("elements", [])


@mcp.tool()
async def get_course(course_id: str) -> dict:
    """Get details for a specific Coursera course by its ID."""
    async with httpx.AsyncClient() as client:
        resp = await client.get(
            f"{COURSERA_API}/courses.v1/{course_id}",
            params={"fields": "name,slug,description,instructorIds,partnerIds"},
        )
        resp.raise_for_status()
        data = resp.json()
    elements = data.get("elements", [])
    return elements[0] if elements else {}


@mcp.tool()
async def list_popular_courses(category: str = "data-science", limit: int = 10) -> list[dict]:
    """List popular Coursera courses in a category (e.g. data-science, business, computer-science)."""
    async with httpx.AsyncClient() as client:
        resp = await client.get(
            f"{COURSERA_API}/courses.v1",
            params={
                "q": "search",
                "query": category,
                "limit": limit,
                "fields": "name,slug,description",
            },
        )
        resp.raise_for_status()
        data = resp.json()
    return data.get("elements", [])


if __name__ == "__main__":
    mcp.run()
