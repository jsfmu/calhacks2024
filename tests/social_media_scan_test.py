# tests/test_social_media_service.py

import pytest
from hello.services.social_media_service import SocialMediaService, SocialMediaPost

@pytest.mark.asyncio
async def test_analyze_social_media():
    # Initialize the service with a test seed phrase
    service = SocialMediaService(seed_phrase="test seed phrase")

    # Define test keywords
    keywords = ["help", "emergency", "flood"]

    # Run the analysis
    results = await service.analyze_social_media(keywords)

    # Check that we got the expected results
    assert len(results) == 2  # We expect 2 posts to match our keywords

    # Check that the returned objects are of the correct type
    assert all(isinstance(post, SocialMediaPost) for post in results)

    # Check that the matched posts contain our keywords
    assert any("help" in post.text.lower() for post in results)
    assert any("emergency" in post.text.lower() for post in results)
    assert any("flood" in post.text.lower() for post in results)

    # Check that the post without keywords was not included
    assert all("picnic" not in post.text.lower() for post in results)

    # Check that the posts have the expected structure
    for post in results:
        assert isinstance(post.text, str)
        assert isinstance(post.location, dict)
        assert "lat" in post.location and "lon" in post.location
        assert isinstance(post.timestamp, str)

if __name__ == "__main__":
    pytest.main()