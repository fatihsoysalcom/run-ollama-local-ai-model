# Run Ollama Local AI Model

This example demonstrates how to interact with the Ollama server using its Python client library. It shows how to check for, pull, and generate text with a local AI model (e.g., Llama2). The script highlights the initial setup steps and resource usage, echoing the article's discussion on the 'hidden costs' of running AI models locally.

## Language

`python`

## How to Run

1. Install Ollama server from `ollama.com` and ensure it's running (e.g., `ollama serve` or desktop app).
2. Install the Python client: `pip install ollama`.
3. Run the script: `python main.py`. You can optionally specify a different model with `OLLAMA_MODEL=mistral python main.py`.

## Original Article

This example accompanies the Turkish article: [Ollama ile Yerel Çin Modelleri Desteği: Kimi ve DeepSeek'i Çalıştırmanın Gizli Maliyeti](https://fatihsoysal.com/blog/ollama-ile-yerel-cin-modelleri-destegi-kimi-ve-deepseeki-calistirmanin-gizli-maliyeti/).

## License

MIT — see [LICENSE](LICENSE).
