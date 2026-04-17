from fastmcp import FastMCP

mcp = FastMCP("coursera")

COURSES = [
    {"id": "python-for-everybody", "name": "Python for Everybody", "category": "computer-science", "difficulty": "beginner", "description": "Learn Python programming from scratch."},
    {"id": "machine-learning", "name": "Machine Learning", "category": "data-science", "difficulty": "intermediate", "description": "ML fundamentals by Andrew Ng."},
    {"id": "deep-learning-specialization", "name": "Deep Learning Specialization", "category": "data-science", "difficulty": "advanced", "description": "Master deep learning techniques."},
    {"id": "google-data-analytics", "name": "Google Data Analytics", "category": "data-science", "difficulty": "beginner", "description": "Professional data analytics certificate."},
    {"id": "ibm-data-science", "name": "IBM Data Science", "category": "data-science", "difficulty": "intermediate", "description": "End-to-end data science professional certificate."},
    {"id": "intro-to-finance", "name": "Introduction to Finance", "category": "business", "difficulty": "beginner", "description": "Core financial concepts and analysis."},
    {"id": "algorithms-part1", "name": "Algorithms Part I", "category": "computer-science", "difficulty": "intermediate", "description": "Fundamental algorithms and data structures."},
    {"id": "cloud-computing", "name": "Cloud Computing Basics", "category": "computer-science", "difficulty": "beginner", "description": "Intro to cloud infrastructure and services."},
    {"id": "prompt-engineering", "name": "Prompt Engineering for AI", "category": "artificial-intelligence", "difficulty": "beginner", "description": "Learn to craft effective prompts for LLMs."},
    {"id": "llm-ops", "name": "LLMOps", "category": "artificial-intelligence", "difficulty": "advanced", "description": "Deploying and operating large language models."},
]


@mcp.tool()
def search_courses(query: str, limit: int = 5) -> list[dict]:
    """Search Coursera courses by keyword."""
    q = query.lower()
    matches = [
        c for c in COURSES
        if q in c["name"].lower() or q in c["description"].lower() or q in c["category"].lower()
    ]
    return matches[:limit]


@mcp.tool()
def get_course(course_id: str) -> dict:
    """Get details for a specific course by its ID."""
    for course in COURSES:
        if course["id"] == course_id:
            return course
    return {"error": f"Course '{course_id}' not found."}


@mcp.tool()
def list_popular_courses(category: str = "data-science", limit: int = 5) -> list[dict]:
    """List courses in a category (e.g. data-science, business, computer-science, artificial-intelligence)."""
    matches = [c for c in COURSES if c["category"] == category]
    return matches[:limit]


if __name__ == "__main__":
    mcp.run(transport="stdio")
