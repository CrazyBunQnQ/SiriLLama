<div align = "center">
<h1>
    <img src = "https://github.com/0ssamaak0/SiriLLama/blob/main/assets/icon.png?raw=true" width = 200 height = 200>
<br>

</h1>

<h3>
Siri LLama
</h3>
</div>

Siri LLama is apple shortcut that access locally running LLMs through Siri or the shortcut UI on any apple device connected to the same network of your host machine. It uses Langchain 🦜🔗 and supports open source models from both [Ollama](https://ollama.com/) 🦙 or [Fireworks AI](https://fireworks.ai/) 🎆

# Download Shortcut from [HERE](https://www.icloud.com/shortcuts/fd032a4e75cc4d81a6f9a742053d4c18)

🟣 [Simple Chat Video🎬](https://twitter.com/0ssamaak0/status/1772356905064665530)

🟣 [Multimodal Video 🎬](https://twitter.com/0ssamaak0/status/1782462691291890148)

🟣 [RAG Video 🎬](https://x.com/0ssamaak0/status/1825662881284653149)

# Getting Started
## Requirements

```bash
pip install -r requirements.txt
```

### Ollama Installation🦙
1. Install [Ollama](https://ollama.com/) for your machine, you have to run `ollama serve` in the terminal to start the server

2. pull the models you want to use, for example
```bash
ollama run llama3 # chat model
ollama run llava # multimodal
```

3. in `config.py` set `OLLAMA_CHAT`, `OLLAMA_VISUAL_CHAT`, and `OLLAMA_EMBEDDINGS_MODEL` to the models you pulled from Ollama
### Fireworks AI Installation🎆

1. get your [Fireworks API Key](http://fireworks.ai/) and put it in `fireworks_models.py`

2. in `config.py` set `FIREWORKS_CHAT`, `FIREWORKS_VISUAL_CHAT` and `FIREWORKS_EMBEDDINGS_MODEL` to the models you want to use from Fireworks AI. and set your and `FIREWORKS_API_KEY` 

## Config
in `confing.py` set `MEMORY_SIZE` (How many previous messages to remember) and `ANSWER_SIZE_WORDS` (How many words to generate in the answer)

## Running SiriLlama 🟣🦙

1. [Download](https://github.com/0ssamaak0/SiriLLama/archive/refs/heads/main.zip) or clone the repo 

2. [set the provider (Ollama / Fireworks)](https://github.com/0ssamaak0/SiriLLama/blob/d07ff97a0eb07db08601e5e3fe0254c6f05aee50/app.py#L18) in `app.py` 

3. Run the flask app using
```bash
>>> python3 app.py
```

4. On your Apple device, Download the shortcut from [here](https://www.icloud.com/shortcuts/fd032a4e75cc4d81a6f9a742053d4c18)
   Note that you must run the shortcut through Siri to "talk" to it, otherwise it will prompt you to type text.

5. Run the shortcut through Siri or the shortcut UI, in first time you run the shortcut you will be asked to enter your [IP address](https://stackoverflow.com/a/15864222) and the port number showing in terminal
```bash
>>> python app.py
...
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5001
 * Running on http://192.168.1.134:5001
Press CTRL+C to quit
```
In the example above, the IP address is `192.168.1.134` and the port is `5001` (default port is specified by Flask, change the line in main.py if needed)

6. If you are using Siri to interact with the shortcut, saying "Good Bye" will stop Siri.



# Common Issues 🐞
- Even we access the flask app (not Ollama server directly), Some windows users who have Ollama installed using `WSL` have to make sure **ollama servere** is exposed to the network, [Check this issue for more details](https://github.com/ollama/ollama/issues/1431)
- When running the shortcut for the first time from Siri, it should ask for permission to send data to the Flask server.
  If it doesn't work (especially on iOS 17.4), first try running the shortcut + sending a message from the iOS Shortcuts app to trigger the permissions dialog, then try running it through Siri again.

# Other LLM Providers 🤖🤖
Supposedly SiriLLama should work with any LLMs that including OpenAI, Claude, etc. but make sure first you installed the corresponding Langchain packages and set the models in `config.py`

# SiriLLama on public network 🌎
- Running SiriLLama outside your local network is possible with a tool called ngrok. It's going to expose one or multiple ports on your local machine. Step by step tutorial:
  1. Start the ngrok server from cmd/terminal with the following command:
```bash
ngrok http localhost:5001
```
  2. It will give you a https link, something like https://xyzz-xxx-xxx-xxx-xxx.ngrok-free.app
  3. In the shortcut you downloaded earlier insert the link from ngrok without https:// and leave the port number field empty
  4. Now you should be able to run SiriLLama outside from your network. (In case you are unable to get valid response or something went wrong, try paste the ngrok link into safari and allow the connection within the browser)

# Good to know 💡💡
- Using the multimodel feature is only possible with images that arent in HEIF format. You can change this in your camera settings (it wont affect your existing photos) under formats choose most compatible and you are good to go.

# Docker 部署 🐳

使用Docker可以更简单地部署SiriLLama，无需担心环境配置问题。以下是使用Docker运行SiriLLama的步骤：

1. 确保您的机器上已安装[Docker](https://www.docker.com/products/docker-desktop/)

2. 在项目根目录下构建Docker镜像
```bash
docker build -t sirillama .
```

3. 运行Docker容器
```bash
docker run -p 5001:5000 sirillama
docker run -itd --name sirillama --restart always -e TZ=Asia/Shanghai -p 5001:5000 sirillama
```

4. 现在您可以通过Apple设备上的快捷指令访问SiriLLama，与非Docker部署方式相同

## Docker与Ollama结合使用

如果您使用Ollama作为LLM提供商，并且Ollama运行在同一台机器上，您需要确保Docker容器可以访问Ollama服务：

```bash
# 假设Ollama运行在默认端口11434
docker run -p 5001:5001 --add-host=host.docker.internal:host-gateway sirillama
```

然后在`config.py`中设置Ollama的基础URL为：
```python
OLLAMA_BASE_URL = "http://host.docker.internal:11434"
```

## 使用Docker Compose

您也可以创建一个`docker-compose.yml`文件来简化部署：

```yaml
version: '3'
services:
  sirillama:
    build: .
    ports:
      - "5001:5001"
    environment:
      - FLASK_APP=app.py
      - FLASK_RUN_HOST=0.0.0.0
```

然后运行：
```bash
docker-compose up
```
