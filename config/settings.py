import os
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent

# 数据库配置
MYSQL_HOST = os.getenv('MYSQL_HOST', 'localhost')
MYSQL_USER = os.getenv('MYSQL_USER', 'root')
MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD', 'password')
MYSQL_DB = os.getenv('MYSQL_DB', 'command_db')

NEO4J_URI = os.getenv('NEO4J_URI', 'bolt://localhost:7474')
NEO4J_USER = os.getenv('NEO4J_USER', 'neo4j')
NEO4J_PASSWORD = os.getenv('NEO4J_PASSWORD', 'password')

# 路径配置
DATA_DIR = BASE_DIR / 'data'
EXTRACTION_DIR = DATA_DIR / 'extraction'
CLASSIFY_DIR = DATA_DIR / 'classify'