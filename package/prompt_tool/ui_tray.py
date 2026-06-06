# -*- coding: utf-8 -*-
"""
系统托盘模块
"""
from PyQt5.QtWidgets import QSystemTrayIcon, QMenu, QAction
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon, QPainter, QColor, QFont


def create_tray_icon() -> QIcon:
    """创建系统托盘图标"""
    pixmap = QIcon.fromTheme("applications-system").pixmap(64, 64)
    if not pixmap.isNull():
        return QIcon(pixmap)
    
    # 如果没有系统图标，创建一个简单的图标
    from PyQt5.QtGui import QPixmap
    pixmap = QPixmap(64, 64)
    pixmap.fill(QColor(66, 133, 244))  # 蓝色背景
    
    painter = QPainter(pixmap)
    painter.setRenderHint(QPainter.Antialiasing)
    
    # 绘制文字
    painter.setPen(QColor(255, 255, 255))
    font = QFont("Arial", 32, QFont.Bold)
    painter.setFont(font)
    painter.drawText(pixmap.rect(), Qt.AlignCenter, "AI")
    
    painter.end()
    return QIcon(pixmap)


class SystemTray:
    """系统托盘管理"""
    
    def __init__(self, app, main_window):
        self.app = app
        self.main_window = main_window
        self.tray_icon = QSystemTrayIcon()
        
        self.init_tray()
    
    def init_tray(self):
        """初始化系统托盘"""
        # 设置图标
        icon = create_tray_icon()
        self.tray_icon.setIcon(icon)
        self.tray_icon.setToolTip("Awesome Prompts - 提示词工具箱")
        
        # 创建菜单
        tray_menu = QMenu()
        
        # 打开主窗口
        open_action = QAction("📂 打开主窗口", tray_menu)
        open_action.triggered.connect(self.show_main_window)
        tray_menu.addAction(open_action)
        
        tray_menu.addSeparator()
        
        # 退出
        quit_action = QAction("❌ 退出", tray_menu)
        quit_action.triggered.connect(self.quit_app)
        tray_menu.addAction(quit_action)
        
        self.tray_icon.setContextMenu(tray_menu)
        
        # 双击托盘图标显示窗口
        self.tray_icon.activated.connect(self.on_tray_activated)
        
        # 显示托盘图标
        self.tray_icon.show()
    
    def on_tray_activated(self, reason):
        """托盘图标激活事件"""
        if reason == QSystemTrayIcon.DoubleClick:
            self.show_main_window()
    
    def show_main_window(self):
        """显示主窗口"""
        self.main_window.show()
        self.main_window.activateWindow()
        self.main_window.raise_()
    
    def quit_app(self):
        """退出应用"""
        self.tray_icon.hide()
        self.app.quit()
