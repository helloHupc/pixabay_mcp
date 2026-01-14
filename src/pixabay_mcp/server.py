"""Pixabay MCP Server - 搜索Pixabay图片和视频的MCP服务"""

import os
from typing import Any

import httpx
from mcp.server.fastmcp import FastMCP

API_KEY = os.environ.get("PIXABAY_API_KEY")
BASE_URL = "https://pixabay.com/api/"

mcp = FastMCP("Pixabay")


@mcp.tool()
async def search_images(
    query: str,
    image_type: str = "all",
    orientation: str = "all",
    category: str = "",
    colors: str = "",
    per_page: int = 20,
    page: int = 1,
    safesearch: bool = True,
) -> dict[str, Any]:
    """
    Search for images on Pixabay.

    Args:
        query: Search term (e.g., "yellow flowers", "cat")
        image_type: Filter by type - "all", "photo", "illustration", "vector"
        orientation: Filter by orientation - "all", "horizontal", "vertical"
        category: Filter by category - backgrounds, fashion, nature, science, education, feelings, health, people, religion, places, animals, industry, computer, food, sports, transportation, travel, buildings, business, music
        colors: Filter by colors (comma-separated) - grayscale, transparent, red, orange, yellow, green, turquoise, blue, lilac, pink, white, gray, black, brown
        per_page: Number of results per page (3-200)
        page: Page number
        safesearch: Enable safe search filter

    Returns:
        Search results with image URLs and metadata
    """
    if not API_KEY:
        return {"error": "PIXABAY_API_KEY environment variable not set"}

    params = {
        "key": API_KEY,
        "q": query,
        "image_type": image_type,
        "orientation": orientation,
        "per_page": min(max(per_page, 3), 200),
        "page": page,
        "safesearch": str(safesearch).lower(),
    }
    if category:
        params["category"] = category
    if colors:
        params["colors"] = colors

    async with httpx.AsyncClient(trust_env=False) as client:
        response = await client.get(BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()

    return {
        "total": data.get("total", 0),
        "totalHits": data.get("totalHits", 0),
        "images": [
            {
                "id": hit["id"],
                "tags": hit.get("tags", ""),
                "previewURL": hit.get("previewURL", ""),
                "webformatURL": hit.get("webformatURL", ""),
                "largeImageURL": hit.get("largeImageURL", ""),
                "user": hit.get("user", ""),
                "pageURL": hit.get("pageURL", ""),
            }
            for hit in data.get("hits", [])
        ],
    }


@mcp.tool()
async def search_videos(
    query: str,
    video_type: str = "all",
    category: str = "",
    per_page: int = 20,
    page: int = 1,
    safesearch: bool = True,
) -> dict[str, Any]:
    """
    Search for videos on Pixabay.

    Args:
        query: Search term (e.g., "nature", "city")
        video_type: Filter by type - "all", "film", "animation"
        category: Filter by category - backgrounds, fashion, nature, science, education, feelings, health, people, religion, places, animals, industry, computer, food, sports, transportation, travel, buildings, business, music
        per_page: Number of results per page (3-200)
        page: Page number
        safesearch: Enable safe search filter

    Returns:
        Search results with video URLs and metadata
    """
    if not API_KEY:
        return {"error": "PIXABAY_API_KEY environment variable not set"}

    params = {
        "key": API_KEY,
        "q": query,
        "video_type": video_type,
        "per_page": min(max(per_page, 3), 200),
        "page": page,
        "safesearch": str(safesearch).lower(),
    }
    if category:
        params["category"] = category

    async with httpx.AsyncClient(trust_env=False) as client:
        response = await client.get(f"{BASE_URL}videos/", params=params)
        response.raise_for_status()
        data = response.json()

    return {
        "total": data.get("total", 0),
        "totalHits": data.get("totalHits", 0),
        "videos": [
            {
                "id": hit["id"],
                "tags": hit.get("tags", ""),
                "duration": hit.get("duration", 0),
                "pageURL": hit.get("pageURL", ""),
                "user": hit.get("user", ""),
                "videos": {
                    size: {
                        "url": info.get("url", ""),
                        "width": info.get("width", 0),
                        "height": info.get("height", 0),
                    }
                    for size, info in hit.get("videos", {}).items()
                },
            }
            for hit in data.get("hits", [])
        ],
    }


def main():
    """Run the MCP server."""
    mcp.run()


if __name__ == "__main__":
    main()