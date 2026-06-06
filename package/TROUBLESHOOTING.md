# 故障排除指南

## 问题：NameError: name '__file__' is not defined

**原因**：旧版 spec 文件在 PyInstaller 运行时不能使用 `__file__` 变量

**解决**：已修复！请使用最新版文件

---

## 如果仍有问题：简单方案

### 方案 1：手动准备 + 打包（推荐）

1. **准备 prompts 目录**
   - 在 `prompt_tool` 文件夹内创建 `prompts` 文件夹
   - 把所有提示词模块（27个目录）复制进去

2. **运行打包**
   ```cmd
   cd prompt_tool
   pyinstaller --clean AwesomePrompts.spec
   ```

### 方案 2：使用最简单的 spec 文件

创建一个简单的 `simple.spec`：

```python
# -*- mode: python ; coding: utf-8 -*-
block_cipher = None

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[('prompts', 'prompts')],  # 直接这样写
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='AwesomePrompts',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
)
```

然后运行：`pyinstaller simple.spec`

### 方案 3：直接用命令行打包（最简单）

```cmd
cd prompt_tool
pyinstaller --onefile --windowed --add-data "prompts;prompts" main.py
```

---

## 检查清单

打包前请确认：

- [ ] Python 3.7+ 已安装
- [ ] `pip install -r requirements.txt` 已执行
- [ ] `pip install pyinstaller` 已执行
- [ ] `prompt_tool/prompts/` 目录存在，里面有 27 个模块文件夹
- [ ] 从 `prompt_tool` 目录内运行命令

---

## 常见错误

### 错误：找不到模块
确保你从正确的目录运行！

**正确**：
```cmd
cd path\to\package\prompt_tool
python build.py
```

**错误**：
```cmd
cd path\to\package
python prompt_tool/build.py  # ❌ 这样会找不到文件！
```

### 错误：权限被拒绝
- 关闭杀毒软件临时监控
- 或右键以管理员身份运行 CMD

### 错误：模块导入失败
尝试运行 `python main.py` 直接测试程序是否工作正常
