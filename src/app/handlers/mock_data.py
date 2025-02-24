import uuid

mock_campaigns = [
    {
        "id": "d9e7f6ef-da2b-4836-8b06-f2aecfe9bb55",
        "title": "Fantasy High",
        "url": "https://www.dropout.tv/dimension-20/season:1",
        "description": "A modern fantasy teen adventure at Aguefort Adventuring Academy.",
        "year": 2019,
        "reviews": [
            {"source": "AV Club", "url": "https://avclub.example/fantasy-high-review"}
        ],
        "is_sequel": False,
    },
    {
        "id": str(uuid.uuid4()),
        "title": "Fantasy High: Sophomore Year",
        "url": "https://www.dropout.tv/fantasy-high-sophomore-year",
        "description": "The Bad Kids return for a second year of adventures.",
        "year": 2020,
        "reviews": [],
        "is_sequel": True,
        "previous_campaign_id": None,  # Or the UUID of the previous campaign if you have one
    },
]

mock_episodes = [
    {
        "id": str(uuid.uuid4()),
        "campaign_id": mock_campaigns[0]["id"],
        "title": "Welcome to Aguefort",
        "episode_number": 1,
        "url": "https://www.dropout.tv/fantasy-high/episode-1",
        "air_date": "2019-06-10",
        "description": "The Bad Kids arrive at Aguefort.",
    }
]
