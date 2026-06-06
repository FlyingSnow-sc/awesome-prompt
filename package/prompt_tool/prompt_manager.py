# -*- coding: utf-8 -*-
"""
提示词管理模块 - 负责加载、解析和管理所有提示词
"""
import os
import sys
from pathlib import Path
from typing import List, Dict, Optional
from dataclasses import dataclass


@dataclass
class PromptItem:
    """单个提示词项"""
    id: str
    name: str
    category: str
    description: str
    content: str
    source: str = ""
    file_path: str = ""


class PromptManager:
    """提示词管理器"""
    
    # 预定义的分类映射
    CATEGORY_MAP = {
        "AI一键将长文转小红书多图": "🎨 内容创作",
        "公众号转小红书爆款图文": "🎨 内容创作",
        "微信公众号爆款标题生成器": "🎨 内容创作",
        "提取文章精华-内容总结": "🎨 内容创作",
        "文章总结并生成卡片": "🎨 内容创作",
        "杂志风知识卡片": "🎨 内容创作",
        "公众号封面图生成": "🎨 内容创作",
        "播客封面图": "🎨 内容创作",
        "插画转真实手办": "🎨 内容创作",
        "IP徽章周边": "🎨 内容创作",
        "有灵魂的AI设计师": "🎨 内容创作",
        "平面地图转 3D 实景": "🎨 内容创作",
        "高端PPT制作": "🎨 内容创作",
        "NotebookLM-提升播客质量": "🎨 内容创作",
        "商业级视频广告": "💼 商业与营销",
        "文章风格分析提取": "💼 商业与营销",
        "剖析深层问题生成卡片": "🧠 学习与分析",
        "论文深度剖析": "🧠 学习与分析",
        "阅读理解巩固": "🧠 学习与分析",
        "AI指令萃取师 (AI Instruction Extractor)": "🧠 学习与分析",
        "AI内容检测Prompt": "🧠 学习与分析",
        "Youtube访谈类视频深度剖析": "🧠 学习与分析",
        "Youtube总结": "🧠 学习与分析",
        "提升大模型回应质量-通用": "🚀 通用与增强",
        "美化UI": "🚀 通用与增强",
        "赛博李继刚": "🌟 特色系列"
    }
    
    def __init__(self, prompts_path: Optional[str] = None):
        self.prompts_path = self._get_prompts_path(prompts_path)
        self.prompts: List[PromptItem] = []
        self.categories: List[str] = []
        self._load_prompts()
    
    def _get_prompts_path(self, custom_path: Optional[str]) -> Path:
        """获取提示词目录路径"""
        if custom_path:
            return Path(custom_path)
        
        # 检查是否是打包后的应用
        if getattr(sys, 'frozen', False):
            base_path = Path(sys._MEIPASS)
            prompts_path = base_path / "prompts"
            if prompts_path.exists():
                return prompts_path
        
        # 开发环境
        current_dir = Path(__file__).parent
        prompts_path = current_dir / "prompts"
        if prompts_path.exists():
            return prompts_path
        
        # 尝试从上级目录查找
        parent_dir = current_dir.parent
        prompts_path = parent_dir
        return prompts_path
    
    def _load_prompts(self):
        """加载所有提示词"""
        if not self.prompts_path.exists():
            print(f"警告：提示词目录不存在: {self.prompts_path}")
            return
        
        self.prompts = []
        
        # 遍历所有模块文件夹
        for item in self.prompts_path.iterdir():
            if not item.is_dir() or item.name.startswith('.'):
                continue
            
            if item.name in ['prompt_tool', '.git']:
                continue
            
            self._load_module(item)
        
        # 提取分类
        self.categories = sorted(list(set(p.category for p in self.prompts)))
    
    def _load_module(self, module_dir: Path):
        """加载单个模块"""
        module_name = module_dir.name
        
        # 获取分类
        category = self.CATEGORY_MAP.get(module_name, "📦 其他")
        
        # 读取 README.md
        readme_file = module_dir / "README.md"
        description = ""
        source = ""
        
        if readme_file.exists():
            try:
                with open(readme_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                    lines = content.split('\n')
                    description = lines[0].strip() if lines else module_name
                    
                    # 尝试提取来源
                    for line in lines:
                        if line.startswith('From') or '来源' in line:
                            source = line.strip()
                            break
            except Exception as e:
                print(f"读取 {readme_file} 失败: {e}")
        
        # 查找所有 prompt 文件
        for prompt_file in module_dir.iterdir():
            if prompt_file.is_file() and prompt_file.suffix in ['.md', '.txt', '.json']:
                if prompt_file.name == 'README.md':
                    continue
                
                try:
                    with open(prompt_file, 'r', encoding='utf-8') as f:
                        prompt_content = f.read()
                    
                    # 创建提示词项
                    prompt_name = prompt_file.stem
                    if prompt_name == 'prompt':
                        prompt_name = module_name
                    
                    prompt_item = PromptItem(
                        id=f"{module_name}/{prompt_file.name}",
                        name=prompt_name,
                        category=category,
                        description=description or module_name,
                        content=prompt_content,
                        source=source,
                        file_path=str(prompt_file)
                    )
                    self.prompts.append(prompt_item)
                except Exception as e:
                    print(f"读取 {prompt_file} 失败: {e}")
        
        # 如果没有找到专门的 prompt 文件，尝试使用 README
        if not any(p.id.startswith(module_name) for p in self.prompts):
            if readme_file.exists():
                try:
                    with open(readme_file, 'r', encoding='utf-8') as f:
                        prompt_content = f.read()
                    
                    prompt_item = PromptItem(
                        id=f"{module_name}/README.md",
                        name=module_name,
                        category=category,
                        description=description or module_name,
                        content=prompt_content,
                        source=source,
                        file_path=str(readme_file)
                    )
                    self.prompts.append(prompt_item)
                except Exception as e:
                    print(f"读取 {readme_file} 失败: {e}")
    
    def get_prompts_by_category(self, category: str) -> List[PromptItem]:
        """获取指定分类的所有提示词"""
        return [p for p in self.prompts if p.category == category]
    
    def search_prompts(self, keyword: str) -> List[PromptItem]:
        """搜索提示词"""
        keyword = keyword.lower()
        return [
            p for p in self.prompts
            if keyword in p.name.lower() or 
               keyword in p.description.lower() or 
               keyword in p.content.lower()
        ]
    
    def get_all_categories(self) -> List[str]:
        """获取所有分类"""
        return self.categories
    
    def get_prompt_by_id(self, prompt_id: str) -> Optional[PromptItem]:
        """根据ID获取提示词"""
        for p in self.prompts:
            if p.id == prompt_id:
                return p
        return None
