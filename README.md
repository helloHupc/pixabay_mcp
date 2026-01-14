# Pixabay MCP Server

[English](#english) | [中文](#中文)

---

## English

A Model Context Protocol (MCP) server that enables AI assistants to search for images and videos on [Pixabay](https://pixabay.com).

### Features

- 🖼️ **search_images** - Search for photos, illustrations, and vectors
- 🎬 **search_videos** - Search for videos and animations

### Installation

#### Method 1: Quick Start with uvx (Recommended)

The easiest way to use this MCP server is with `uvx`. No manual cloning required!

1. Get your [Pixabay API Key](https://pixabay.com/api/docs/)
2. Add the following to your MCP client configuration:

```json
{
  "mcpServers": {
    "pixabay": {
      "command": "uvx",
      "args": [
        "https://gitee.com/hupengchen/pixabay_mcp.git"
      ],
      "env": {
        "PIXABAY_API_KEY": "your-api-key-here"
      }
    }
  }
}
```

3. Restart your MCP client and start using!

#### Method 2: Local Development

For development or to customize the code, clone the repository locally:

```bash
git clone https://gitee.com/hupengchen/pixabay_mcp.git
cd pixabay_mcp
```

Then configure your MCP client:

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

Make sure to replace `/path/to/pixabay_mcp` with your actual local path.

### Get Your API Key

1. Create a free account at [Pixabay](https://pixabay.com/accounts/register/)
2. Go to [API Documentation](https://pixabay.com/api/docs/) and copy your API key

### Quick Start

1. **Get your API key from Pixabay**
2. **Copy** configuration from Method 1 above
3. **Replace `your-api-key-here`** with your actual API key
4. **Add to your MCP client settings**
5. **Restart your MCP client**
6. **Start searching!**

### Usage Examples

Once configured, you can ask your AI assistant:

- "Search for photos of yellow flowers"
- "Find some nature videos"
- "Look for vector illustrations of cats"

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

### License

MIT License

---

## 中文

一个 MCP (Model Context Protocol) 服务，让 AI 助手能够在 [Pixabay](https://pixabay.com) 上搜索图片和视频。

### 功能

- 🖼️ **search_images** - 搜索照片、插画和矢量图
- 🎬 **search_videos** - 搜索视频和动画

### 安装

#### 方法 1：使用 uvx 快速开始（推荐）

最简单的使用方式，使用 `uvx` 直接从 Gitee 运行，无需手动克隆！

1. 获取你的 [Pixabay API 密钥](https://pixabay.com/api/docs/)
2. 在 MCP 客户端配置中添加以下内容：

```json
{
  "mcpServers": {
    "pixabay": {
      "command": "uvx",
      "args": [
        "https://gitee.com/hupengchen/pixabay_mcp.git"
      ],
      "env": {
        "PIXABAY_API_KEY": "你的API密钥"
      }
    }
  }
}
```

3. 重启 MCP 客户端，开始使用！

#### 方法 2：本地开发调试

用于开发或自定义代码，将仓库克隆到本地：

```bash
git clone https://gitee.com/hupengchen/pixabay_mcp.git
cd
```

然后配置 MCP 客户端：

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

请将 `/path/to/pixabay_mcp` 替换为你的实际本地路径。

### 获取 API 密钥

1. 在 [Pixabay](https://pixabay.com/accounts/register/) 注册免费账号
2. 访问 [API 文档页面](https://pixabay.com/api/docs/) 复制你的 API 密钥

### 快速开始

1. **从 Pixabay 获取你的 API 密钥**
2. **复制上面方法 1 中的配置**
3. **将 `你的API密钥`** 替换为你的实际 API 密钥
4. **添加到你的 MCP 客户端设置**
5. **重启 MCP 客户端**
6. **开始搜索！**

### 使用示例

配置完成后，你可以这样问 AI 助手：

- "帮我搜索黄色花朵的图片"
- "找一些自然风景的视频"
- "搜索猫咪的矢量插画"

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

### uv 和 uvx 的区别

**uv** - 通用 Python 项目管理工具
- 用于开发、安装包、运行脚本
- 需要手动管理虚拟环境
- 适合本地开发和调试

**uvx** - 快速执行工具
- 直接从 PyPI 或 Git 仓库运行包
- 自动管理隔离环境
- 无需手动安装，开箱即用
- 适合快速部署和分享

### 许可证

MIT 许可证