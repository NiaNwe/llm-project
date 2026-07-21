"""Entry point for the llm_agent package."""

import argparse


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="LLM Agent starter CLI")
    parser.add_argument(
        "--prompt",
        "-p",
        default="Hello from llm agent",
        help="A prompt string to process",
    )
    return parser.parse_args()


def generate_response(prompt: str) -> str:
    """Generate a placeholder response for the given prompt."""
    return f"Echo: {prompt}"


def main() -> int:
    args = parse_args()
    print(generate_response(args.prompt))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
