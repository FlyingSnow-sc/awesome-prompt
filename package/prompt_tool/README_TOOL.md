# Awesome Prompts - Windows 工具使用说明

## 工具功能

这是一个 Windows 后台工具，方便您快速查找和复制 AI 提示词。

### 主要功能

- 🎨 系统托盘运行：后台运行，不占用任务栏空间
- 🔍 快速搜索：支持按名称或关键词搜索提示词
- 📂 分类浏览：按功能分类浏览提示词
- 📋 一键复制：点击即可复制提示词到剪贴板
- ⌨️ 快捷键唤醒：Alt+Space 快速打开/关闭窗口

## 安装与运行

### 方法一：直接运行 Python 脚本

1. 安装依赖：
```bash
cd prompt_tool
pip install -r requirements.txt
```

2. 运行程序：
```bash
python main.py
```

### 方法二：打包成 EXE

1. 安装 PyInstaller：
```bash
pip install pyinstaller
```

2. 运行构建脚本：
```bash
python build.py
```

3. 生成的 EXE 文件位于 `dist/AwesomePrompts.exe`

## 使用说明

### 启动程序

双击运行 `AwesomePrompts.exe` 或 `python main.py`，程序将在系统托盘显示图标。

### 打开窗口

- 右键点击系统托盘图标，选择「打开主窗口」
- 或使用快捷键 Alt+Space 快速唤醒

### 浏览提示词

1. 在左侧选择分类
2. 点击具体的提示词项查看详细内容
3. 点击「复制」按钮将提示词复制到剪贴板

### 搜索提示词

在搜索框中输入关键词，实时筛选提示词。

### 退出程序

右键点击系统托盘图标，选择「退出」

## 目录结构

```
prompt_tool/
├── main.py              # 主程序入口
├── prompt_manager.py    # 提示词管理模块
├── ui_main.py           # 主界面
├── ui_tray.py           # 系统托盘
├── requirements.txt     # 依赖列表
├── build.py            # 构建脚本
└── README_TOOL.md      # 本文档
```
