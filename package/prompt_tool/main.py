# -*- coding: utf-8 -*-
"""
Awesome Prompts - 主程序入口
"""
import sys
from PyQt5.QtWidgets import QApplication, QShortcut
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QKeySequence

from prompt_manager import PromptManager
from ui_main import MainWindow
from ui_tray import SystemTray


def main():
    """主函数"""
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)  # 关闭窗口不退出程序
    
    # 初始化提示词管理器
    prompt_manager = PromptManager()
    
    # 创建主窗口
    main_window = MainWindow(prompt_manager)
    
    # 创建系统托盘
    tray = SystemTray(app, main_window)
    
    # 设置全局快捷键 (Alt+Space)
    shortcut = QShortcut(QKeySequence(Qt.AltModifier | Qt.Key_Space), main_window)
    shortcut.activated.connect(lambda: toggle_window(main_window))
    
    # 显示主窗口
    main_window.show()
    
    # 运行应用
    sys.exit(app.exec_())


def toggle_window(window):
    """切换窗口显示/隐藏"""
    if window.isVisible():
        window.hide()
    else:
        window.show()
        window.activateWindow()
        window.raise_()


if __name__ == "__main__":
    main()
