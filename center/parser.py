from pycparser import c_parser, c_ast, parse_file

class FunctionVisitor(c_ast.NodeVisitor):
    def __init__(self):
        self.call_graph = {}
        self.current_func = None
    
    def visit_FuncDef(self, node):
        """捕获函数定义"""
        self.current_func = node.decl.name
        self.call_graph[self.current_func] = []
        self.generic_visit(node)  # 继续遍历子节点
        self.current_func = None
    
    def visit_FuncCall(self, node):
        """捕获函数调用"""
        if self.current_func:
            called_func = node.name.name
            # 处理函数指针等情况
            if isinstance(node.name, c_ast.ID):
                self.call_graph[self.current_func].append(called_func)
        self.generic_visit(node)

def analyze_c_file(file_path):
    """分析单个C文件"""
    ast = parse_file(file_path, use_cpp=True, cpp_args=r'-Iutils/fake_libc_include')
    visitor = FunctionVisitor()
    visitor.visit(ast)
    return visitor.call_graph