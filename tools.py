"""
AI CLI Design - AI CLI设计工具
支持CLI架构、命令设计、文档生成
"""

import json
import os
from typing import Dict, List, Any
from datetime import datetime

try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False


class AICLIDesignTools:
    """
    AI CLI设计工具
    支持：架构、命令、文档
    """

    def __init__(self, model: str = "mimo-v2.5-pro", api_key: str = None, base_url: str = None):
        self.model = model
        if OPENAI_AVAILABLE:
            self.client = OpenAI(
                api_key=api_key or os.environ.get('OPENAI_API_KEY', ''),
                base_url=base_url or os.environ.get('OPENAI_BASE_URL', 'https://api.xiaomimimo.com/v1')
            )
        else:
            self.client = None

    def design_cli_tool(self, tool_name: str, purpose: str, commands: List[str]) -> Dict:
        """设计CLI工具"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        commands_text = ", ".join(commands)

        prompt = f"""请设计{tool_name} CLI工具：

目的：{purpose}
命令：{commands_text}

请返回JSON格式：
{{
    "architecture": "架构",
    "command_structure": "命令结构",
    "global_options": ["全局选项"],
    "output_formats": ["输出格式"],
    "config": "配置方案"
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"cli": content}

    def generate_cli_code(self, tool_name: str, commands: List[Dict], framework: str = "click") -> str:
        """生成CLI代码"""
        if not self.client:
            return "LLM客户端未配置"

        commands_text = json.dumps(commands, ensure_ascii=False)

        prompt = f"""请生成{tool_name} CLI代码：

框架：{framework}
命令：{commands_text}

要求：
1. 完整可运行
2. 帮助文档
3. 错误处理
4. 彩色输出"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=4000
        )

        return response.choices[0].message.content

    def generate_man_page(self, tool_name: str, description: str, commands: List[Dict]) -> str:
        """生成man page"""
        if not self.client:
            return "LLM客户端未配置"

        commands_text = json.dumps(commands, ensure_ascii=False)

        prompt = f"""请为{tool_name}生成man page：

描述：{description}
命令：{commands_text}

请使用标准man page格式："""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )

        return response.choices[0].message.content

    def generate_completion_scripts(self, tool_name: str, shell: str) -> str:
        """生成自动补全脚本"""
        if not self.client:
            return "LLM客户端未配置"

        prompt = f"""请为{tool_name}生成{shell}自动补全脚本：

要求：
1. 命令补全
2. 选项补全
3. 参数补全"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1000
        )

        return response.choices[0].message.content

    def design_cli_config(self, tool_name: str, config_options: List[str]) -> Dict:
        """设计CLI配置"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        options_text = ", ".join(config_options)

        prompt = f"""请为{tool_name}设计配置方案：

选项：{options_text}

请返回JSON格式：
{{
    "config_file": "配置文件格式",
    "env_vars": ["环境变量"],
    "cli_flags": ["CLI标志"],
    "precedence": "优先级规则"
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"config": content}

    def generate_cli_docs(self, tool_name: str, commands: List[Dict]) -> str:
        """生成CLI文档"""
        if not self.client:
            return "LLM客户端未配置"

        commands_text = json.dumps(commands, ensure_ascii=False)

        prompt = f"""请为{tool_name}生成CLI文档：

命令：{commands_text}

要求：
1. 快速开始
2. 命令参考
3. 示例
4. 配置说明"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )

        return response.choices[0].message.content


def create_tools(**kwargs) -> AICLIDesignTools:
    """创建CLI设计工具"""
    return AICLIDesignTools(**kwargs)


if __name__ == "__main__":
    tools = create_tools()

    print("AI CLI Design Tools")
    print()

    # 测试
    cli = tools.design_cli_tool("myapp", "应用管理", ["init", "build", "deploy"])
    print(json.dumps(cli, ensure_ascii=False, indent=2))
