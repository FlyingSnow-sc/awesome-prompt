# -*- coding: utf-8 -*-
"""
主界面模块
"""
from PyQt5.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
    QSplitter, QListWidget, QListWidgetItem, QTextEdit,
    QPushButton, QLineEdit, QLabel, QMessageBox, QComboBox
)
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QFont
import pyperclip
from prompt_manager import PromptManager, PromptItem


class MainWindow(QMainWindow):
    """主窗口"""
    
    closed = pyqtSignal()
    
    def __init__(self, prompt_manager: PromptManager):
        super().__init__()
        self.prompt_manager = prompt_manager
        self.current_prompt: PromptItem | None = None
        self.init_ui()
        self.load_categories()
    
    def init_ui(self):
        """初始化界面"""
        self.setWindowTitle("Awesome Prompts - 提示词工具箱")
        self.setMinimumSize(900, 600)
        
        # 中央部件
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # 主布局
        main_layout = QVBoxLayout(central_widget)
        
        # 顶部搜索栏
        top_layout = QHBoxLayout()
        
        # 分类选择
        self.category_combo = QComboBox()
        self.category_combo.setMinimumWidth(200)
        self.category_combo.currentTextChanged.connect(self.on_category_changed)
        top_layout.addWidget(QLabel("分类:"))
        top_layout.addWidget(self.category_combo)
        
        top_layout.addStretch()
        
        # 搜索框
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("搜索提示词...")
        self.search_input.setMinimumWidth(300)
        self.search_input.textChanged.connect(self.on_search)
        top_layout.addWidget(QLabel("搜索:"))
        top_layout.addWidget(self.search_input)
        
        main_layout.addLayout(top_layout)
        
        # 分割器
        splitter = QSplitter(Qt.Horizontal)
        
        # 左侧列表
        self.list_widget = QListWidget()
        self.list_widget.itemClicked.connect(self.on_item_clicked)
        splitter.addWidget(self.list_widget)
        
        # 右侧内容区
        right_widget = QWidget()
        right_layout = QVBoxLayout(right_widget)
        
        # 标题和来源
        info_layout = QHBoxLayout()
        self.title_label = QLabel("选择一个提示词")
        self.title_label.setFont(QFont("Arial", 14, QFont.Bold))
        info_layout.addWidget(self.title_label)
        
        self.source_label = QLabel("")
        self.source_label.setStyleSheet("color: gray;")
        info_layout.addWidget(self.source_label)
        info_layout.addStretch()
        
        right_layout.addLayout(info_layout)
        
        # 内容显示
        self.content_text = QTextEdit()
        self.content_text.setReadOnly(True)
        self.content_text.setFont(QFont("Consolas", 10))
        right_layout.addWidget(self.content_text)
        
        # 按钮区
        button_layout = QHBoxLayout()
        button_layout.addStretch()
        
        self.copy_button = QPushButton("📋 复制到剪贴板")
        self.copy_button.setMinimumWidth(150)
        self.copy_button.clicked.connect(self.copy_to_clipboard)
        button_layout.addWidget(self.copy_button)
        
        right_layout.addLayout(button_layout)
        
        splitter.addWidget(right_widget)
        
        # 设置分割比例
        splitter.setSizes([300, 600])
        
        main_layout.addWidget(splitter)
    
    def load_categories(self):
        """加载分类"""
        categories = self.prompt_manager.get_all_categories()
        self.category_combo.addItem("📂 全部")
        self.category_combo.addItems(categories)
    
    def on_category_changed(self, category: str):
        """分类改变"""
        self.search_input.clear()
        if category == "📂 全部":
            prompts = self.prompt_manager.prompts
        else:
            prompts = self.prompt_manager.get_prompts_by_category(category)
        self.update_list(prompts)
    
    def on_search(self, keyword: str):
        """搜索"""
        if keyword:
            prompts = self.prompt_manager.search_prompts(keyword)
        else:
            category = self.category_combo.currentText()
            if category == "📂 全部":
                prompts = self.prompt_manager.prompts
            else:
                prompts = self.prompt_manager.get_prompts_by_category(category)
        self.update_list(prompts)
    
    def update_list(self, prompts: list[PromptItem]):
        """更新列表"""
        self.list_widget.clear()
        for prompt in prompts:
            item = QListWidgetItem(prompt.name)
            item.setData(Qt.UserRole, prompt.id)
            self.list_widget.addItem(item)
    
    def on_item_clicked(self, item: QListWidgetItem):
        """点击列表项"""
        prompt_id = item.data(Qt.UserRole)
        prompt = self.prompt_manager.get_prompt_by_id(prompt_id)
        if prompt:
            self.current_prompt = prompt
            self.title_label.setText(prompt.name)
            self.source_label.setText(prompt.source)
            self.content_text.setPlainText(prompt.content)
    
    def copy_to_clipboard(self):
        """复制到剪贴板"""
        if self.current_prompt:
            pyperclip.copy(self.current_prompt.content)
            QMessageBox.information(self, "成功", "提示词已复制到剪贴板！")
    
    def closeEvent(self, event):
        """关闭事件"""
        event.ignore()
        self.hide()
        self.closed.emit()
