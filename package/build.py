#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build script for Awesome Prompts - creates EXE file
Works on Windows, can be run directly with Python
"""

import os
import sys
import shutil
import subprocess
from pathlib import Path

def main():
    print("=" * 50)
    print("  Awesome Prompts - Build EXE")
    print("=" * 50)
    print()

    # Change to script directory
    script_dir = Path(__file__).parent
    os.chdir(script_dir)

    # Step 1: Check Python
    print("[1/5] Checking Python...")
    print(f"  Python version: {sys.version}")
    print("  OK: Python found")
    print()

    # Step 2: Install dependencies
    print("[2/5] Installing dependencies...")
    try:
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", "prompt_tool/requirements.txt", "-i", "https://pypi.tuna.tsinghua.edu.cn/simple"], check=True)
    except:
        print("  Note: Some dependencies may have issues, continuing...")

    try:
        subprocess.run([sys.executable, "-m", "pip", "install", "pyinstaller", "-i", "https://pypi.tuna.tsinghua.edu.cn/simple"], check=True)
    except:
        pass
    print()

    # Step 3: Prepare prompt files
    print("[3/5] Preparing prompt files...")
    prompt_tool_dir = script_dir / "prompt_tool"
    prompts_dir = prompt_tool_dir / "prompts"

    if prompts_dir.exists():
        shutil.rmtree(prompts_dir)
    prompts_dir.mkdir(exist_ok=True)

    count = 0
    for item in script_dir.iterdir():
        if item.is_dir() and not item.name.startswith('.') and item.name not in ["prompt_tool", "package"]:
            dest_dir = prompts_dir / item.name
            shutil.copytree(item, dest_dir)
            count += 1
            print(f"  Copied: {item.name}")

    print(f"  Total: {count} modules")
    print()

    # Step 4: Build EXE
    print("[4/5] Building EXE...")
    print("  This may take a few minutes, please wait...")
    os.chdir(prompt_tool_dir)

    success = False
    try:
        # Try direct command line first
        cmd = [
            sys.executable, "-m", "PyInstaller",
            "--clean",
            "--onefile",
            "--windowed",
            "--add-data", "prompts;prompts",
            "main.py"
        ]
        subprocess.run(cmd, check=True)
        success = True
    except Exception as e:
        print(f"  First method failed: {e}")
        print("  Trying backup method...")

        try:
            subprocess.run([sys.executable, "-m", "PyInstaller", "--clean", "simple.spec"], check=True)
            success = True
        except Exception as e2:
            print(f"  Backup method also failed: {e2}")

    print()

    # Check result
    exe_file = prompt_tool_dir / "dist" / "AwesomePrompts.exe"
    if exe_file.exists():
        print("=" * 50)
        print("  SUCCESS!")
        print("=" * 50)
        print()
        print(f"EXE location: {exe_file}")
        print()
        print("You can run it now!")

        # Open the dist folder
        if sys.platform == "win32":
            os.startfile(str(prompt_tool_dir / "dist"))
    else:
        print("=" * 50)
        print("  ERROR: EXE not found!")
        print("=" * 50)
        print()
        print("Please check the error messages above.")

    print()
    input("Press Enter to exit...")

if __name__ == "__main__":
    main()
