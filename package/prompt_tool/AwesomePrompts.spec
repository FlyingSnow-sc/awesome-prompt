# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[],
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

# 添加 prompts 目录
import os
import shutil
from pathlib import Path

# 复制 prompts 到临时目录
project_root = Path(__file__).parent
temp_prompts = project_root / "prompts"
if temp_prompts.exists():
    shutil.rmtree(temp_prompts)
temp_prompts.mkdir(exist_ok=True)

for item in project_root.parent.iterdir():
    if item.is_dir() and not item.name.startswith('.') and item.name not in ['prompt_tool', '.git']:
        dest_dir = temp_prompts / item.name
        if dest_dir.exists():
            shutil.rmtree(dest_dir)
        shutil.copytree(item, dest_dir)
        print(f"Copied: {item.name}")

# 添加数据文件
datas = []
for root, dirs, files in os.walk(temp_prompts):
    for file in files:
        src_path = os.path.join(root, file)
        rel_path = os.path.relpath(src_path, project_root)
        dest_dir = os.path.dirname(rel_path)
        datas.append((src_path, dest_dir))

a.datas += datas

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
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
