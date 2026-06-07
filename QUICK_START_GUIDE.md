# Awesome Prompts - Quick Start Guide

## 🚀 Easiest Way - Use Python Build Script (Recommended!)

### Just 3 Steps

1. **Download and extract** `AwesomePrompts_Complete_Package.zip`
2. **Double-click** or **run** `build.py` with Python
3. **Wait**, EXE will be in `prompt_tool/dist/`

### How to run build.py:
   - Right-click `build.py` → Open with → Python
   - OR open command line: `python build.py`

---

## Alternative: Use Batch File (English only)

If above doesn't work, try `build_exe.bat`

---

## If Still Not Working? Do it manually:

### Step 1: Install Python
- Download Python 3.7+ from python.org/downloads
- Check "Add Python to PATH" during install

### Step 2: Open Command Prompt
```cmd
cd path\to\package\prompt_tool
```

### Step 3: Install Dependencies
```cmd
pip install -r requirements.txt
pip install pyinstaller
```

### Step 4: Prepare Files
- Create `prompts` folder inside `prompt_tool`
- Copy ALL 27+ module folders into `prompts`

### Step 5: Build EXE
```cmd
pyinstaller --onefile --windowed --add-data "prompts;prompts" main.py
```

### Step 6: Done!
- Find `dist/AwesomePrompts.exe` and run it!

---

## Features
- System tray background running
- Browse prompts by category
- Real-time search
- One-click copy to clipboard

---

## Problems?
Check `TROUBLESHOOTING.md` for help!
