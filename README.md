# FlowBar AI — Python SDK

<p align="center">
  <a href="https://flowbarai.com"><strong>flowbarai.com</strong></a> ·
  <a href="https://github.com/flowbar-api/flowbar-sdk-node">Node.js SDK</a>
</p>

<p align="center">
  <a href="https://github.com/flowbar-api/flowbar-sdk-python"><img src="https://img.shields.io/github/stars/flowbar-api/flowbar-sdk-python?style=flat-square&color=yellow" alt="GitHub stars"></a>
  <a href="https://github.com/flowbar-api/flowbar-sdk-python/blob/master/LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square" alt="License: MIT"></a>
  <a href="https://flowbarai.com"><img src="https://img.shields.io/badge/website-flowbarai.com-6c5ce7.svg?style=flat-square" alt="Website"></a>
  <img src="https://img.shields.io/badge/python-3.9+-3776ab.svg?style=flat-square" alt="Python 3.9+">
</p>

One API key for **50+ frontier AI models**. GPT · Claude · Gemini · DeepSeek · Qwen · GLM · Kimi. Fully OpenAI-compatible.

> **Pay however you want** — Waffo (430+ local methods, Apple Pay / Google Pay), WeChat, Alipay, USDT/USDC, PayPal. No foreign card required.

## Install

```bash
pip install flowbarai
```

Or from source:

```bash
git clone https://github.com/flowbar-api/flowbar-sdk-python
cd flowbar-sdk-python
pip install -e .
```

## Quick start

```python
from flowbar import FlowBar

client = FlowBar(api_key="sk-...")

# Simple chat
reply = client.chat("deepseek-v4-flash", "Explain quantum computing.")
print(reply)

# With a system prompt
reply = client.chat("gpt-5.6", "What is 2+2?", system="You are a helpful assistant.")
print(reply)

# Streaming
for chunk in client.stream_chat("gpt-5.6", "Tell me a joke."):
    print(chunk, end="")

# Generate an image
images = client.generate_image("A cat in a spacesuit")
print(images[0].url)

# Embeddings
emb = client.embed("Hello world")

# List all available models
for m in client.list_models():
    print(f"  {m.id}")
```

The API key defaults to the `FLOWBAR_API_KEY` environment variable.

## Features

- **OpenAI-compatible** — drop-in base URL `https://api.flowbarai.com/v1`, keep the OpenAI SDK shape
- **50+ frontier models** — one key for chat, reasoning, vision, image, and embedding models
- **Streaming** — `stream_chat()` yields content chunks as they arrive
- **Multi-turn** — `chat_with_history()` for full conversation context
- **Images & embeddings** — `generate_image()` and `embed()`
- **Model aliases** — `MODELS` dict with typed keys and special aliases (`cheapest`, `most_capable`)

## Models

| Model ID | Description |
|----------|-------------|
| `gpt-5.6` | Latest frontier reasoning |
| `gpt-5.5-luna` | Balanced speed / power |
| `claude-opus-4-8` | Strongest Deep Research |
| `claude-sonnet-5` | Fast daily driver |
| `gemini-3.5-flash` | Fastest Google |
| `deepseek-v4-pro` | Best Chinese model |
| `deepseek-v4-flash` | Cheapest ($0.55/1M) |
| `qwen-3.7-max` | Alibaba strongest |
| `kimi-k3` | Moonshot reasoning |
| `glm-5.1` | Zhipu AI |
| `minimax-m2.7` | MiniMax |

Use `from flowbar import MODELS` for typed model IDs (e.g. `MODELS["gpt56"]`).

## API

### `FlowBar(api_key=None, base_url=..., timeout=120.0, max_retries=2)`

| Param | Type | Default | Description |
|-------|------|---------|-------------|
| `api_key` | `str` | `FLOWBAR_API_KEY` | Your FlowBar API key |
| `base_url` | `str` | `https://api.flowbarai.com/v1` | Override the base URL |
| `timeout` | `float` | `120.0` | Request timeout (seconds) |
| `max_retries` | `int` | `2` | Max retries on failure |

### Methods

| Method | Returns | Description |
|--------|---------|-------------|
| `chat(model, prompt, system=None, ...)` | `str` | Single-turn chat |
| `chat_with_history(model, messages, ...)` | `ChatCompletion` | Multi-turn conversation |
| `stream_chat(model, prompt, ...)` | `Generator[str]` | Streaming chat |
| `generate_image(prompt, ...)` | `List[Image]` | Image generation |
| `embed(input, model=...)` | `List[Embedding]` | Embeddings |
| `list_models()` | `List[Model]` | List available models |
| `get_best_deal(category="chat")` | `str` | Best-value model by category |

## Pricing

FlowBar is **5–10% below OpenRouter** on Chinese frontier models (DeepSeek, Qwen, GLM, Kimi). Top-up bonuses: $10 → +8%, $30 → +18%, $80 → +28%, $200 → +38%.

## License

MIT © [FlowBar AI](https://flowbarai.com)
