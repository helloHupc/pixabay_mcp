# Pixabay MCP Server

[English](#english) | [中文](#中文)

---

## English

A Model Context Protocol (MCP) server that enables AI assistants to search for images and videos on [Pixabay](https://pixabay.com).

### Features

- 🖼️ **search_images** - Search for photos, illustrations, and vectors
- 🎬 **search_videos** - Search for videos and animations

### Prerequisites

Before installing, make sure you have [uv](https://github.com/astral-sh/uv) installed:

```bash
# On macOS and Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# On Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### Installation

#### Method 1: Clone from Gitee (Recommended for Chinese users)

```bash
# Clone the repository
git clone <your-gitee-repo-url>
cd pixabay_mcp
```

Then configure your MCP client using the "Run from Cloned Repository" method below.

#### Method 2: Install from PyPI using uv

```bash
uv pip install pixabay-mcp
```

#### Method 3: Install from PyPI using pip

```bash
pip install pixabay-mcp
```

### Configuration

#### Get Your API Key

1. Create a free account at [Pixabay](https://pixabay.com/accounts/register/)
2. Go to [API Documentation](https://pixabay.com/api/docs/) and copy your API key

#### Configure MCP Client

**Option 1: Run from Cloned Repository**

After cloning the repository, add this to your MCP settings (e.g., `mcp_settings.json`):

```json
{
  "mcpServers": {
    "pixabay": {
      "command": "uv",
      "args": [
        "run",
        "--directory", "/path/to/pixabay_mcp",
        "python", "src/pixabay_mcp/server.py"
      ],
      "env": {
        "PIXABAY_API_KEY": "your-api-key-here"
      }
    }
  }
}
```

Make sure to replace `/path/to/pixabay_mcp` with the actual path to the cloned repository.

**Option 2: Run using uv with --with flag**

```json
{
  "mcpServers": {
    "pixabay": {
      "command": "uv",
      "args": [
        "run",
        "--with", "mcp[cli]",
        "--with", "httpx",
        "/path/to/pixabay_mcp/src/pixabay_mcp/server.py"
      ],
      "env": {
        "PIXABAY_API_KEY": "your-api-key-here"
      }
    }
  }
}
```

**Option 3: Run installed package using uv**

```json
{
  "mcpServers": {
    "pixabay": {
      "command": "uv",
      "args": ["run", "--with", "pixabay-mcp", "pixabay-mcp"],
      "env": {
        "PIXABAY_API_KEY": "your-api-key-here"
      }
    }
  }
}
```

**Option 4: Run installed package using pip**

```json
{
  "mcpServers": {
    "pixabay": {
      "command": "pixabay-mcp",
      "env": {
        "PIXABAY_API_KEY": "your-api-key-here"
      }
    }
  }
}
```

### Quick Start

1. **Get the code:**
   ```bash
   git clone <your-gitee-repo-url>
   cd pixabay_mcp
   ```

2. **Get your API key:**
   - Register at [Pixabay](https://pixabay.com/accounts/register/)
   - Copy your API key from [API Documentation](https://pixabay.com/api/docs/)

3. **Configure MCP Client:**
   - Add the configuration from "Option 1" above to your MCP settings
   - Replace `/path/to/pixabay_mcp` with your actual path
   - Replace `your-api-key-here` with your Pixabay API key

4. **Start using:**
   - Restart your AI client or MCP server connection
   - Ask your AI assistant to search for images or videos

### Project Structure

```
pixabay_mcp/
├── src/
│   └── pixabay_mcp/
│       ├── __init__.py
│       └── server.py          # Main MCP server implementation
├── pyproject.toml              # Project configuration
├── uv.lock                     # Dependency lock file
├── README.md                   # This file
├── LICENSE                     # MIT License
└── .gitignore                  # Git ignore rules
```

### Usage Examples

Once configured, you can ask your AI assistant:

- "Search for photos of yellow flowers"
- "Find some nature videos"
- "Look for vector illustrations of cats"

### License

MIT License

---

## 中文

一个 MCP (Model Context Protocol) 服务，让 AI 助手能够在 [Pixabay](https://pixabay.com) 上搜索图片和视频。

### 功能

- 🖼️ **search_images** - 搜索照片、插画和矢量图
- 🎬 **search_videos** - 搜索视频和动画

### 前置要求

安装前，请确保已安装 [uv](https://github.com/astral-sh/uv)：

```bash
# macOS 和 Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 安装

#### 方法 1：从 Gitee 克隆（推荐中国用户使用）

```bash
# 克隆仓库
git clone <你的gitee仓库地址>
cd pixabay_mcp
```

然后使用下面的"从克隆仓库运行"方法配置 MCP 客户端。

#### 方法 2：使用 uv 从 PyPI 安装

```bash
uv pip install pixabay-mcp
```

#### 方法 3：使用 pip 从 PyPI 安装

```bash
pip install pixabay-mcp
```

### 配置

#### 获取 API Key

1. 在 [Pixabay](https://pixabay.com/accounts/register/) 注册免费账号
2. 访问 [API 文档页面](https://pixabay.com/api/docs/) 复制你的 API key

#### 配置 MCP 客户端

**选项 1：从克隆仓库运行**

克隆仓库后，在 MCP 设置文件（如 `mcp_settings.json`）中添加：

```json
{
  "mcpServers": {
    "pixabay": {
      "command": "uv",
      "args": [
        "run",
        "--directory", "/path/to/pixabay_mcp",
        "python", "src/pixabay_mcp/server.py"
      ],
      "env": {
        "PIXABAY_API_KEY": "你的API密钥"
      }
    }
  }
}
```

请将 `/path/to/pixabay_mcp` 替换为实际的克隆仓库路径。

**选项 2：使用 uv 的 --with 标志运行**

```json
{
  "mcparservers": {
    "pixabay": {
      "command": "uv",
      "args": [
        "run",
        "--with", "mcp[cli]",
        "--with", "httpx",
        "/path/to/pixabay_mcp/src/pixabay_mcp/server.py"
      ],
      "env": {
        "PIXABAY_API_KEY": "你的API密钥"
      }
    }
  }
}
```

**选项 3：使用 uv 运行已安装的包**

```json
{
  "mcpServers": {
    "pixabay": {
      "command": "uv",
      "args": ["run", "--with", "pixabay-mcp", "pixabay-mcp"],
      "env": {
        "PIXABAY_API_KEY": "你的API密钥"
      }
    }
  }
}
```

**选项 4：使用 pip 运行已安装的包**

```json
{
  "mcpServers": {
    "pixabay": {
      "command": "pixabay-mcp",
      "env": {
        "PIXABAY_API_KEY": "你的API密钥"
      }
    }
  }
}
```

### 快速开始

1. **获取代码：**
   ```bash
   git clone <你的gitee仓库地址>
   cd pixabay_mcp
   ```

2. **获取 API 密钥：**
   - 在 [Pixabay](https://pixabay.com/accounts/register/) 注册账号
   - 从 [API 文档页面](https://pixabay.com/api/docs/) 复制你的 API 密钥

3. **配置 MCP 客户端：**
   - 将上面"选项 1"中的配置添加到你的 MCP 设置中
   - 将 `/path/to/pixabay_mcp` 替换为你的实际路径
   - 将 `你的API密钥` 替换为你的 Pixabay API 密钥

4. **开始使用：**
   - 重启你的 AI 客户端或 MCP 服务器连接
   - 让 AI 助手帮你搜索图片或视频

### 项目结构

```
pixabay_mcp/
├── src/
│   └── pixabay_mcp/
│       ├── __init__.py
│       └── server.py          # MCP 服务器主实现
├── pyproject.toml              # 项目配置文件
├── uv.lock                     # 依赖锁定文件
├── README.md                   # 本文件
├── LICENSE                     # MIT 许可证
└── .gitignore                  # Git 忽略规则
```

### 使用示例

配置完成后，你可以这样问 AI 助手：

- "帮我搜索黄色花朵的图片"
- "找一些自然风景的视频"
- "搜索猫咪的矢量插画"

### 许可证

MIT 许可证