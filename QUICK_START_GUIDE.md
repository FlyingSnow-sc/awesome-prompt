# Awesome Prompts - 快速开始指南

## 🎉 最简单的方法：双击打包！

### 🚀 只需要 3 步

1. **下载并解压** `AwesomePrompts_Complete_Package.zip`
2. **双击** `一键打包.bat`
3. **等待完成**，EXE 在 `prompt_tool/dist/` 目录

就这么简单！

---

## 📦 如果上面不行，手动操作

### 前置条件
- Windows 系统
- Python 3.7+（从 python.org 下载，安装时勾选 "Add Python to PATH"）

### 步骤

1. **打开命令提示符（CMD）或 PowerShell**
2. **进入项目目录**
   ```cmd
   cd path\to\package\prompt_tool
   ```

3. **安装依赖**
   ```cmd
   pip install -r requirements.txt
   pip install pyinstaller
   ```

4. **准备提示词文件**
   - 在 `prompt_tool` 里创建 `prompts` 文件夹
   - 把外面那 27 个模块文件夹都复制进去

5. **打包**
   ```cmd
   pyinstaller --onefile --windowed --add-data "prompts;prompts" main.py
   ```

6. **完成！**
   - 找到 `dist/AwesomePrompts.exe` 直接运行

---

## 💡 工具功能

- 🎨 系统托盘后台运行
- 📂 按分类浏览提示词
- 🔍 实时搜索
- 📋 一键复制到剪贴板

---

## ❓ 遇到问题？

查看 `TROUBLESHOOTING.md` 获取更多解决方案！
