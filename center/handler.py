import ast
from typing import List, Dict, Tuple
from pathlib import Path

def analyze_call_graph(file_path: Path) -> Dict[str, List[str]]:
    """使用ast模块更可靠地分析函数调用"""
    call_graph = {}
    
    with open(file_path, 'r', encoding='utf-8') as f:
        tree = ast.parse(f.read())
    
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            caller = node.name
            call_graph[caller] = []
            
            for subnode in ast.walk(node):
                if isinstance(subnode, ast.Call):
                    if isinstance(subnode.func, ast.Name):
                        call_graph[caller].append(subnode.func.id)
    
    return call_graph

def process_directory(dir_path: Path) -> Dict[str, Dict[str, List[str]]]:
    """处理目录下所有源文件"""
    result = {}
    for file in dir_path.glob('*.c'):
        result[file.name] = analyze_call_graph(file)
    return result