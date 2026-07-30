# FlowBar AI — Python SDK

One API key for 50+ frontier AI models. OpenAI-compatible.

```python
from flowbar import FlowBar

client = FlowBar(api_key="sk-...")

# Simple chat
reply = client.chat("deepseek-v4-flash", "Explain quantum computing.")
print(reply)

# Streaming
for chunk in client.stream_chat("gpt-5.6", "Tell me a joke."):
    print(chunk, end="")

# Generate an image
images = client.generate_image("A cat in a spacesuit")
print(images[0].url)

# List all available models
for m in client.list_models():
    print(f"  {m.id}")
```

## Installation

```bash
pip install flowbarai
```

Or from source:

```bash
git clone https://github.com/flowbar-api/flowbar-sdk-python
cd flowbar-sdk-python
pip install -e .
```

## Models

| Model ID | Description |
|----------|-------------|
| `gpt-5.6` | Latest frontier reasoning |
| `claude-opus-4-8` | Strongest Deep Research |
| `claude-sonnet-5` | Fast daily driver |
| `gemini-3.5-flash` | Fastest Google |
| `deepseek-v4-pro` | Best Chinese model |
| `deepseek-v4-flash` | Cheapest ($0.55/1M) |
| `qwen-3.7-max` | Alibaba strongest |
| `kimi-k3` | Moonshot reasoning |
| `glm-5.1` | Zhipu AI |

## Payment

Pay with Waffo (430+ local methods, Apple Pay, Google Pay), WeChat, Alipay, USDT/USDC, or PayPal.

[flowbarai.com](https://flowbarai.com)
