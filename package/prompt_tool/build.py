# -*- coding: utf-8 -*-
"""
构建脚本 - 用于将程序打包成Windows可执行文件
"""
import os
import sys
import shutil
from pathlib import Path


def main():
    print("=" * 60)
    print("Awesome Prompts Tool - 构建脚本")
    print("=" * 60)
    
    # 检查是否安装了 PyInstaller
    try:
        import PyInstaller
    except ImportError:
        print("\n❌ 请先安装 PyInstaller:")
        print("   pip install pyinstaller")
        return
    
    # 项目目录
    project_dir = Path(__file__).parent
    os.chdir(project_dir)
    
    # 清理旧的构建文件
    print("\n🧹 清理旧构建文件...")
    for dir_name in ['build', 'dist', 'prompts']:
        dir_path = project_dir / dir_name
        if dir_path.exists():
            shutil.rmtree(dir_path)
            print(f"   已删除: {dir_name}")
    
    # 复制提示词文件
    print("\n📦 准备提示词文件...")
    temp_prompts = project_dir / "prompts"
    temp_prompts.mkdir(exist_ok=True)
    
    prompt_count = 0
    for item in project_dir.parent.iterdir():
        if item.is_dir() and not item.name.startswith('.') and item.name not in ['prompt_tool', '.git']:
            dest_dir = temp_prompts / item.name
            shutil.copytree(item, dest_dir)
            prompt_count += 1
            print(f"   已复制: {item.name}")
    
    print(f"   共复制 {prompt_count} 个模块")
    
    # 执行构建
    print("\n🔨 开始构建...")
    
    build_cmd = [
        "pyinstaller",
        "--clean",
        "AwesomePrompts.spec"
    ]
    
    import subprocess
    result = subprocess.run(build_cmd, shell=True)
    
    if result.returncode == 0:
        print("\n" + "=" * 60)
        print("✅ 构建成功！")
        print(f"📂 可执行文件位置: {project_dir / 'dist' / 'AwesomePrompts.exe'}")
        print("=" * 60)
    else:
        print("\n" + "=" * 60)
        print("❌ 构建失败！")
        print("=" * 60)


if __name__ == "__main__":
    main()
