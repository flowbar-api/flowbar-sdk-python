"""FlowBar AI — Official Python SDK

One API key for 50+ frontier AI models.
GPT · Claude · Gemini · DeepSeek · Qwen · GLM · Kimi
OpenAI-compatible. Pay with Waffo, WeChat, Alipay, USDT, PayPal.

Usage::

    from flowbar import FlowBar
    client = FlowBar(api_key="sk-...")
    reply = client.chat("deepseek-v4-flash", "Explain quantum computing.")

Website: https://flowbarai.com
License: MIT
"""

from openai import OpenAI
from typing import Optional, List, Dict, Any, AsyncGenerator, Literal

__version__ = "1.0.0"

MODELS = {
    # Latest frontier models (2026-07)
    "gpt56": "gpt-5.6",
    "gpt55_luna": "gpt-5.5-luna",
    "claude_opus48": "claude-opus-4-8",
    "claude_sonnet5": "claude-sonnet-5",
    "gemini35_flash": "gemini-3.5-flash",
    "deepseek_v4_pro": "deepseek-v4-pro",
    "deepseek_v4_flash": "deepseek-v4-flash",
    "qwen37_max": "qwen-3.7-max",
    "kimi_k3": "kimi-k3",
    "glm51": "glm-5.1",
    "minimax_m27": "minimax-m2.7",
    # Special aliases
    "cheapest": "deepseek-v4-flash",
    "most_capable": "gpt-5.6",
}


class FlowBar:
    """FlowBar AI unified API client.

    Args:
        api_key: Your FlowBar API key. Defaults to FLOWBAR_API_KEY env var.
        base_url: Override base URL (default: https://api.flowbarai.com/v1).
        timeout: Request timeout in seconds (default: 120).
        max_retries: Max retries on failure (default: 2).
    """

    def __init__(
        self,
        api_key: Optional[str] = None,
        base_url: str = "https://api.flowbarai.com/v1",
        timeout: float = 120.0,
        max_retries: int = 2,
    ):
        import os
        api_key = api_key or os.environ.get("FLOWBAR_API_KEY", "sk-your-api-key")
        self.client = OpenAI(
            api_key=api_key,
            base_url=base_url,
            timeout=timeout,
            max_retries=max_retries,
        )

    # ── Chat ──────────────────────────────────────────

    def chat(
        self,
        model: str,
        prompt: str,
        system: Optional[str] = None,
        temperature: float = 0.7,
        max_tokens: int = 2048,
        **kwargs,
    ) -> str:
        """Simple single-turn chat.

        Args:
            model: Model ID (e.g. 'deepseek-v4-flash').
            prompt: User message text.
            system: Optional system prompt.
            temperature: Sampling temperature.
            max_tokens: Max output tokens.

        Returns:
            Model response text.
        """
        messages = []
        if system:
            messages.append({"role": "system", "content": system})
        messages.append({"role": "user", "content": prompt})

        resp = self.client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,
            **kwargs,
        )
        return resp.choices[0].message.content or ""

    def chat_with_history(
        self,
        model: str,
        messages: List[Dict[str, str]],
        temperature: float = 0.7,
        max_tokens: int = 4096,
        **kwargs,
    ):
        """Multi-turn conversation with full message history."""
        return self.client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,
            **kwargs,
        )

    def stream_chat(
        self,
        model: str,
        prompt: str,
        system: Optional[str] = None,
        temperature: float = 0.7,
        max_tokens: int = 4096,
        **kwargs,
    ):
        """Stream chat — yields content chunks."""
        messages = []
        if system:
            messages.append({"role": "system", "content": system})
        messages.append({"role": "user", "content": prompt})

        stream = self.client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,
            stream=True,
            **kwargs,
        )

        for chunk in stream:
            delta = chunk.choices[0].delta.content if chunk.choices else None
            if delta:
                yield delta

    # ── Images ────────────────────────────────────────

    def generate_image(
        self,
        prompt: str,
        model: str = "qwen-image-2.0",
        n: int = 1,
        size: str = "1024x1024",
        quality: Literal["standard", "hd"] = "standard",
    ) -> List[Any]:
        """Generate image(s). Returns list of image data objects with .url or .b64_json."""
        resp = self.client.images.generate(
            model=model,
            prompt=prompt,
            n=n,
            size=size,
            quality=quality,
        )
        return resp.data

    # ── Embeddings ────────────────────────────────────

    def embed(
        self,
        input: str | List[str],
        model: str = "text-embedding-3-small",
    ) -> List[Any]:
        """Create embedding(s)."""
        resp = self.client.embeddings.create(model=model, input=input)
        return resp.data

    # ── Models ────────────────────────────────────────

    def list_models(self) -> List[Any]:
        """List all available models on FlowBar."""
        return self.client.models.list().data

    def get_best_deal(self, category: str = "chat") -> str:
        """Return the best value model for a given category."""
        best = {
            "chat": MODELS["deepseek_v4_flash"],
            "code": MODELS["claude_sonnet5"],
            "vision": MODELS["gemini35_flash"],
            "image": MODELS["cheapest"],
            "embedding": "text-embedding-3-small",
        }
        return best.get(category, MODELS["cheapest"])
