# Awesome Prompts - Windows 工具版

一个将 Awesome Prompts 项目打包成 Windows 桌面应用程序的工具，支持系统托盘后台运行，方便快速查找和复制 AI 提示词。

## ✨ 功能特性

- 🎨 **系统托盘运行** - 最小化到系统托盘，不占用任务栏空间
- 📂 **分类浏览** - 按功能分类浏览所有提示词
- 🔍 **实时搜索** - 支持按名称、描述、内容搜索提示词
- 📋 **一键复制** - 点击即可复制提示词到剪贴板
- 🎯 **美观界面** - 现代化的 PyQt5 图形界面
- ⚡ **快速启动** - 轻量级应用，启动迅速

## 📁 项目结构

```
prompt_tool/
├── main.py              # 主程序入口
├── prompt_manager.py    # 提示词管理模块
├── ui_main.py           # 主窗口界面
├── ui_tray.py           # 系统托盘模块
├── requirements.txt     # Python 依赖
├── AwesomePrompts.spec  # PyInstaller 打包配置
├── build.py             # 构建脚本
└── README.md            # 本文档
```

## 🚀 快速开始

### 方法一：直接运行 Python 脚本

1. **安装依赖**
```bash
cd prompt_tool
pip install -r requirements.txt
```

2. **运行程序**
```bash
python main.py
```

### 方法二：打包成 EXE 可执行文件

1. **安装依赖**
```bash
cd prompt_tool
pip install -r requirements.txt
pip install pyinstaller
```

2. **执行构建**
```bash
python build.py
```

3. **使用生成的 EXE**
   
   构建完成后，可执行文件位于：`dist/AwesomePrompts.exe`

## 📖 使用说明

### 基本操作

1. **启动程序** - 双击运行 AwesomePrompts.exe
2. **浏览提示词** - 在左侧选择分类，点击列表项查看内容
3. **搜索提示词** - 在搜索框输入关键词进行筛选
4. **复制提示词** - 点击「复制到剪贴板」按钮
5. **最小化窗口** - 点击关闭按钮，程序会最小化到系统托盘
6. **恢复窗口** - 双击系统托盘图标或右键选择「打开主窗口」
7. **退出程序** - 右键点击系统托盘图标，选择「退出」

### 界面说明

- **顶部栏** - 分类选择器 + 搜索框
- **左侧列表** - 提示词列表
- **右侧区域** - 提示词详情 + 复制按钮

## 🛠️ 技术栈

- **GUI 框架**: PyQt5
- **打包工具**: PyInstaller
- **剪贴板操作**: pyperclip
- **Python 版本**: 3.7+

## 📝 开发说明

### 依赖安装

```bash
pip install PyQt5 pyperclip pyinstaller
```

### 代码模块说明

#### 1. prompt_manager.py
负责提示词的加载、解析和管理：
- `PromptItem` - 提示词数据类
- `PromptManager` - 管理器类，负责加载、搜索、分类

#### 2. ui_main.py
主窗口界面：
- `MainWindow` - 主窗口类
- 分类选择、搜索、列表展示、内容查看、复制功能

#### 3. ui_tray.py
系统托盘功能：
- `SystemTray` - 系统托盘管理类
- 托盘图标、右键菜单、窗口控制

#### 4. main.py
程序入口：
- 初始化应用、管理器、窗口、托盘
- 事件循环

## 🎨 添加新提示词

只需在项目根目录的对应分类文件夹中添加新的 `.md` 或 `.txt` 文件，重新构建即可。

## ⚙️ 打包配置

可以通过修改 `AwesomePrompts.spec` 来自定义打包行为：
- 修改 `console=False/True` 来显示/隐藏控制台窗口
- 添加更多 `hiddenimports` 来包含缺失的模块
- 修改 `datas` 来添加额外的数据文件

## 🐛 常见问题

**Q: 程序无法加载提示词？**

A: 确保提示词文件夹位于正确位置，重新运行构建脚本。

**Q: 杀毒软件报毒？**

A: PyInstaller 打包的程序有时会被误报，添加信任即可。

**Q: 如何开机自启动？**

A: 将 AwesomePrompts.exe 的快捷方式放到 `C:\Users\<用户名>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup`

## 📄 许可证

本项目遵循原项目的许可证。

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！
