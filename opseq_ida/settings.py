import os

# IDA 경로
IDA_PATH = os.path.normpath('C:/Program Files/IDA 7.0/idat64.exe')

# ZIP FILE PATH
ZIP_FILE_PATH = os.path.normpath(os.path.abspath('./zipfile'))

# idb(i64) 저장 경로
IDB_PATH = os.path.normpath(os.path.abspath('./idb'))

# ops 저장 경로
OPS_PATH = os.path.normpath(os.path.abspath('./ops'))

# fh 저장 경로
FH_PATH = os.path.normpath(os.path.abspath('./fh'))

# ida python script 저장 경로
IDA_PYTHON_SCRIPT_PATH = os.path.normpath(os.path.abspath('./ida_script'))

# CPU COUNT
CPU_COUNT = 6

# Feature Hashing 관련 상수 정의
# 최대 리스트 크기
MAX_LIST_SIZE = 4096

#최대 증가(감소) 크기
BOUNDARY_SIZE = 512

# n-gram 시작
N_GRAM_START = 3

# n-gram 끝
N_GRAM_END = 5