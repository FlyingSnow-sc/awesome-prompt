# Awesome Prompts - 快速开始指南

## 🎉 下载完成！

您已成功下载 Awesome Prompts 完整项目包！

## 📦 包含内容

- **27+ 个 AI 提示词模块（分类整理）
- **Windows 桌面工具完整源代码
- **一键打包脚本

## 🚀 Windows 打包步骤（只需 3 步）

### 第一步：解压项目包

将 `AwesomePrompts_Complete_Package.zip` 解压到任意位置

### 第二步：安装 Python（如果没有）

1. 访问 [python.org/downloads](https://www.python.org/downloads/)
2. 下载 Python 3.7 或更高版本
3. **重要**：安装时勾选 "Add Python to PATH"

### 第三步：打包成 EXE

打开命令提示符（CMD）或 PowerShell，进入 `prompt_tool` 目录：

```cmd
cd path\to\package\prompt_tool
pip install -r requirements.txt
pip install pyinstaller
python build.py
```

完成！打包成功后，EXE 文件位于：
`prompt_tool\dist\AwesomePrompts.exe`

## 💡 直接运行方式

| 方式 | 说明 |
|-----|------|
| **开发调试** | 运行 `python main.py` |
| **打包使用** | 运行 `python build.py` 生成 EXE |

## 📖 详细文档

- [PACKAGE_README.md](package/PACKAGE_README.md) - 完整打包说明
- [CODE_WIKI.md](package/CODE_WIKI.md) - 项目整体架构
- [prompt_tool/README.md](package/prompt_tool/README.md) - 开发文档

## ✨ 工具功能

- 🎨 系统托盘后台运行
- 📂 按分类浏览提示词
- 🔍 实时搜索
- 📋 一键复制到剪贴板

祝您使用愉快！
