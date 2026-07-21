from llm_agent.main import generate_response


def test_generate_response():
    prompt = "Test prompt"
    assert generate_response(prompt) == "Echo: Test prompt"
