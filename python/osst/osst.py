import os

environ_dic = os.environ
# 환경변수

environ_str = os.environ.get('PATH')
# 특정 환경변수값

env_str = os.getenv('PATH', 'value')
# 해당 환경변수 리턴 없을경우 value 리턴 value 없으면 None 리턴

os.putenv('name', 'value')
# 해당 환경변수 name을 value로 설정

os.chdir('/home')
# 경로 위치 변경

pwd_str = os.getcwd()
# 경로 위치 리턴

str = '/home/mytext.txt'
dirname_str = os.path.dirname(str)
# 파일 경로 리턴

basename_str = os.path.basename(str)
# 경로 파일명 리턴

dir_base_tuple = os.path.split(str)
# 경로와 파일명 리턴

os.system('ls -al')
# 시스템 명령어 호출(결과값 print)

f_str = os.popen('ls -al').read()
# 시스템 결과값 리턴

os.mkdir('mydir')
# 폴더 생성

os.rmdir('mydir')
# 폴더 삭제

# os.unlink('mydir')
# 파일 삭제

# os.rename('a', 'b')
# 파일 이름 a에서 b로 변경 또는 이동

# os.renames('a', 'b')
# 파일 이름 a에서 b로 변경 또는 이동(경로 자동 생성)

dir_list = os.listdir('.')
# 경로 목록 티런

os.makedirs('dir/sub_dir')
# 하위 경로 폴더 생성

os.mkdir('dir2')
# 폴더 생성

os.removedirs('dir/sub_dir')
# 하위 경로 폴더 삭제

os.rmdir('dir2')
# 폴더 삭제

os.walk('.')
# 입력받은 경로부터 모든 하위경로 탐색
#   for path,dirs,files in os.walk(' '):
#       print(path, dirs, files)

os.walk('.', topdown=False)
# os.walk('.')의 반대
#   for path,dirs,files in os.walk(' ', topdown=False):
#       print(path, dirs, files)

# stat_str = os.stat('')
# 파일 상태 확인

os.access('.', os.F_OK)
# F_OK 존재여부
# R_OK 읽기 가능여부
# W_OK 쓰기 가능여부
# X_OK 실행 가능여부

os.utime('.', None)
# 경로에 해당하는 atime(에세스 시간) mtime(수정 시간) 변경
# None일경우 현재 시간으로 수정

r,w = os.pipe()
# 파이프 생성

rd = os.fdopen(r)
# 파일 디스크립터를 이용해 파일 객체 생성

oldmask = os.umask(777)
# 이후에 오픈된 파일을 (mode & ~umask)로 변경

p = popen('dir', 'r')
# 인자로 전달된 명령을 수행하며 pipe 오픈

os.name
# 운영체제 이름 

os.getpid()
# 현재 프로세스 아이디 리턴

