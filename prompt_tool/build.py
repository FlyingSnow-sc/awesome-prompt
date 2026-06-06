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
    
    # 检查从哪里复制提示词
    parent_dir = project_dir.parent
    prompt_count = 0
    
    # 检查是否是在项目包内部
    if (parent_dir / "AI一键将长文转小红书多图").exists():
        # 在完整项目包中，从上级目录复制
        source_dir = parent_dir
    elif (project_dir / "../AI一键将长文转小红书多图").exists():
        # 开发环境
        source_dir = project_dir.parent
    else:
        print("⚠️  未找到提示词目录，跳过复制")
        source_dir = None
    
    if source_dir:
        for item in source_dir.iterdir():
            if item.is_dir() and not item.name.startswith('.') and item.name not in ['prompt_tool', '.git', 'package']:
                dest_dir = temp_prompts / item.name
                if dest_dir.exists():
                    shutil.rmtree(dest_dir)
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
