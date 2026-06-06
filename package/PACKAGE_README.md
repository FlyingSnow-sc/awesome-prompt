# Awesome Prompts - 完整项目包

## 📦 项目说明

这是 **Awesome Prompts** 项目的完整打包版本，包含所有提示词模块和 Windows 桌面工具的源代码。

## 📁 目录结构

```
AwesomePrompts_Package/
├── README.md                    # 本文档
├── prompt_tool/                 # Windows 工具源代码
│   ├── main.py                  # 主程序入口
│   ├── prompt_manager.py        # 提示词管理
│   ├── ui_main.py               # 主窗口界面
│   ├── ui_tray.py               # 系统托盘
│   ├── requirements.txt         # Python 依赖
│   ├── AwesomePrompts.spec      # 打包配置
│   └── build.py                 # 构建脚本
└── [所有提示词模块目录...]     # 20+ 个提示词模块
```

## 🚀 快速开始（Windows）

### 方法一：直接运行 Python 脚本（开发调试）

1. **安装 Python 3.7+**
   - 从 https://www.python.org/downloads/ 下载安装
   - 安装时勾选 "Add Python to PATH"

2. **安装依赖**
   ```cmd
   cd prompt_tool
   pip install -r requirements.txt
   ```

3. **运行程序**
   ```cmd
   python main.py
   ```

### 方法二：打包成 EXE（推荐）

1. **安装依赖和 PyInstaller**
   ```cmd
   cd prompt_tool
   pip install -r requirements.txt
   pip install pyinstaller
   ```

2. **执行构建**
   ```cmd
   python build.py
   ```

3. **获取 EXE 文件**
   - 构建完成后，EXE 文件位于：`prompt_tool/dist/AwesomePrompts.exe`
   - 双击即可运行！

## 💡 使用说明

### 工具功能

- 🎨 **系统托盘运行** - 关闭窗口最小化到托盘
- 📂 **分类浏览** - 按 5 大分类浏览提示词
- 🔍 **实时搜索** - 输入关键词搜索提示词
- 📋 **一键复制** - 点击复制到剪贴板

### 快捷键

- 双击系统托盘图标 → 显示/隐藏窗口

## 🎯 提示词分类

- 🎨 内容创作（14个模块）
- 💼 商业与营销（2个模块）
- 🧠 学习与分析（6个模块）
- 🚀 通用与增强（2个模块）
- 🌟 赛博李继刚（特色系列）

## 🛠️ 技术支持

如有问题，请参考：
- `prompt_tool/README.md` - 详细开发文档
- `../CODE_WIKI.md` - 项目整体说明

## 📝 注意事项

- 首次运行 PyInstaller 可能需要几分钟
- 杀毒软件可能对打包的 EXE 误报，添加信任即可
- 如需添加新提示词，在对应目录添加 .md/.txt 文件后重新构建
