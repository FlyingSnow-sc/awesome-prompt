# -*- coding: utf-8 -*-
"""
System Tray Module
"""
from PyQt5.QtWidgets import QSystemTrayIcon, QMenu, QAction
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QIcon, QPainter, QColor, QFont, QPixmap


def create_tray_icon() -> QIcon:
    """Create system tray icon"""
    try:
        # Try to get a system icon first
        icon = QIcon.fromTheme("applications-system")
        if not icon.isNull():
            return icon
    except:
        pass
    
    # Create a simple colored icon
    pixmap = QPixmap(64, 64)
    pixmap.fill(QColor(66, 133, 244))  # Blue background
    
    painter = QPainter(pixmap)
    painter.setRenderHint(QPainter.Antialiasing)
    
    # Draw simple text
    painter.setPen(QColor(255, 255, 255))
    font = QFont("Arial", 24, QFont.Bold)
    painter.setFont(font)
    painter.drawText(pixmap.rect(), Qt.AlignCenter, "AI")
    
    painter.end()
    return QIcon(pixmap)


class SystemTray:
    """System Tray Manager"""
    
    def __init__(self, app, main_window):
        self.app = app
        self.main_window = main_window
        self.tray_icon = QSystemTrayIcon()
        
        self.init_tray()
    
    def init_tray(self):
        """Initialize system tray"""
        # Set icon
        icon = create_tray_icon()
        self.tray_icon.setIcon(icon)
        self.tray_icon.setToolTip("Awesome Prompts")
        
        # Create menu
        tray_menu = QMenu()
        
        # Open main window
        open_action = QAction("Open", tray_menu)
        open_action.triggered.connect(self.show_main_window)
        tray_menu.addAction(open_action)
        
        tray_menu.addSeparator()
        
        # Quit
        quit_action = QAction("Quit", tray_menu)
        quit_action.triggered.connect(self.quit_app)
        tray_menu.addAction(quit_action)
        
        self.tray_icon.setContextMenu(tray_menu)
        
        # Double click to show window
        self.tray_icon.activated.connect(self.on_tray_activated)
        
        # Show tray icon
        self.tray_icon.show()
    
    def on_tray_activated(self, reason):
        """Tray icon activated event"""
        if reason == QSystemTrayIcon.DoubleClick:
            self.show_main_window()
    
    def show_main_window(self):
        """Show main window"""
        self.main_window.show()
        self.main_window.activateWindow()
        self.main_window.raise_()
    
    def quit_app(self):
        """Quit application"""
        self.tray_icon.hide()
        self.app.quit()
