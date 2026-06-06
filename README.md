# 💻 AI CLI Design

AI CLI设计工具，支持CLI架构、命令设计、文档生成。

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" />
  <img src="https://img.shields.io/badge/OpenAI-API-green?logo=openai" />
  <img src="https://img.shields.io/badge/License-MIT-yellow" />
</p>

## ✨ 特性

- 🏗️ CLI工具设计
- 💻 CLI代码生成
- 📖 man page生成
- 🔧 自动补全脚本
- ⚙️ 配置方案设计
- 📚 CLI文档生成

## 🚀 快速开始

```bash
pip install openai

python tools.py
```

## 📖 使用

```python
from ai_cli_design import create_tools

tools = create_tools()

# CLI设计
cli = tools.design_cli_tool("myapp", "应用管理", ["init", "build", "deploy"])

# CLI代码
code = tools.generate_cli_code("myapp", commands, "click")

# man page
man = tools.generate_man_page("myapp", "应用管理工具", commands)

# 自动补全
completion = tools.generate_completion_scripts("myapp", "bash")

# 配置方案
config = tools.design_cli_config("myapp", ["api_key", "output_format"])

# CLI文档
docs = tools.generate_cli_docs("myapp", commands)
```

## 📁 项目结构

```
ai-cli-design/
├── tools.py       # CLI设计工具核心
└── README.md
```

## 📄 许可证

MIT License
