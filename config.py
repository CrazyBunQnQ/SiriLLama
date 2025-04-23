# Parameters
MEMORY_SIZE = 10  # Number of messages to remember
ANSWER_SIZE_WORDS = 40  # Number of words in an answer
MAX_TOKENS = ANSWER_SIZE_WORDS / 0.75  # rough approximation
CHUNCK_SIZE = 4096  # of vetorstore
CHUNK_OVERLAP = 200  # of vetorstore

# Prompts
PROMPT_CHAT = f"你是高智商 Siri，一个比 Siri 更聪明的 AI。你正在帮助用户执行任务，对于任何问题，回答都非常简洁(回答大概是 {ANSWER_SIZE_WORDS} 个词）和信息。否则，要求用户提供更多信息。"
PROMPT_VISUAL_CHAT = "你是高智商 Siri，一个能够看到图像的 AI，并给出关于图像的答案。每当你被问到时都结合你看到的图像进行回答"

PROVIDER = "openai"  # "ollama" or "fireworks" or "openai"
# Models
# OpenAI
OPENAI_CHAT = "grok-3-fast-beta"
OPENAI_VISUAL_CHAT = "grok-2-vision-1212"
OPENAI_EMBEDDINGS_MODEL = "nomic-embed-text:latest"
OPENAI_BASE_URL = "https://api.x.ai/v1"
OPENAI_EMBEDDINGS_MODEL_URL = "http://127.0.0.1:11434"
OPENAI_API_KEY = "<API_KEY>"

# Ollama
OLLAMA_CHAT = "gemma3:12b"
OLLAMA_VISUAL_CHAT = "gemma3:12b"
OLLAMA_EMBEDDINGS_MODEL = "nomic-embed-text:latest"
OLLAMA_BASE_URL = "http://127.0.0.1:11434"

# Fireworks
FIREWORKS_CHAT = "accounts/fireworks/models/llama-v3p1-8b-instruct"
FIREWORKS_VISUAL_CHAT = "accounts/fireworks/models/phi-3-vision-128k-instruct"
FIREWORKS_API_KEY = "<API_KEY>"
FIREWORKS_EMBEDDINGS_MODEL = "nomic-ai/nomic-embed-text-v1.5"
