import ollama
import sys
import os

# Define the model to use. The article discusses Kimi and DeepSeek, but for a
# universally runnable example, we use a commonly available model like 'llama2'.
# The process of interacting with Ollama is identical for any model.
MODEL_NAME = os.getenv("OLLAMA_MODEL", "llama2") # Default to llama2, can be overridden

def main():
    print(f"Attempting to interact with Ollama using model: {MODEL_NAME}\n")
    print("Ensure the Ollama server is running in the background.")
    print("You can pre-download models using `ollama pull {MODEL_NAME}` or let the script pull it.")
    print("-" * 50)

    try:
        # Check if Ollama server is reachable by listing local models
        # This implicitly checks if the server is running and accessible.
        ollama.list()
        print("Ollama server is reachable.")
    except ollama.ResponseError as e:
        if "connection refused" in str(e).lower() or "failed to connect" in str(e).lower():
            print("\nError: Ollama server is not running or not accessible.")
            print("Please start the Ollama server first (e.g., by running `ollama serve` or starting the desktop app).")
            sys.exit(1)
        else:
            print(f"\nAn unexpected Ollama error occurred: {e}")
            sys.exit(1)
    except Exception as e:
        print(f"\nAn unexpected error occurred while checking Ollama server: {e}")
        sys.exit(1)

    # --- Step 1: Ensure the model is available locally ---
    # The article discusses the "hidden costs" of running models locally,
    # which includes the time and resources (network, disk space) to download them.
    # This step simulates checking for and potentially pulling the model.
    print(f"\nChecking if model '{MODEL_NAME}' is available locally...")
    try:
        local_models = ollama.list()['models']
        model_found = any(m['name'].startswith(MODEL_NAME) for m in local_models)

        if not model_found:
            print(f"Model '{MODEL_NAME}' not found locally. Attempting to pull it.")
            print("This might take some time and consume network/disk resources (a 'hidden cost').")
            # Stream the pull process to show progress
            for progress in ollama.pull(MODEL_NAME, stream=True):
                if 'total' in progress and 'completed' in progress:
                    percent = (progress['completed'] / progress['total']) * 100
                    print(f"\rPulling {MODEL_NAME}: {percent:.2f}%", end='', flush=True)
                elif 'status' in progress:
                    # Clear line and print status for non-percentage updates
                    sys.stdout.write('\r' + ' ' * 80 + '\r') # Clear current line
                    print(f"Pulling {MODEL_NAME}: {progress['status']}", end='', flush=True)
            print(f"\nModel '{MODEL_NAME}' pulled successfully.")
        else:
            print(f"Model '{MODEL_NAME}' is already available locally.")

    except ollama.ResponseError as e:
        print(f"\nError pulling model '{MODEL_NAME}': {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\nAn unexpected error occurred during model pull check: {e}")
        sys.exit(1)

    # --- Step 2: Generate a response using the local model ---
    # This demonstrates running a local AI model, which is the core
    # functionality discussed in the article. Generating responses
    # consumes CPU/GPU and memory (another 'hidden cost').
    prompt = "Tell me a short, interesting fact about Turkey."
    print(f"\nSending prompt to '{MODEL_NAME}': '{prompt}'")
    print("Generating response (this uses local compute resources)...\n")

    try:
        response = ollama.generate(model=MODEL_NAME, prompt=prompt)
        print("--- Model Response ---")
        print(response['response'].strip())
        print("----------------------")
    except ollama.ResponseError as e:
        print(f"\nError generating response with model '{MODEL_NAME}': {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\nAn unexpected error occurred during response generation: {e}")
        sys.exit(1)

    print("\nExample finished successfully.")

if __name__ == "__main__":
    main()
