import os

environ_dic = os.environ
# 환경변수

environ_str = os.environ.get('PATH')
# 특정 환경변수값

os.chdir('/home')
# 디렉터리 위치 변경

pwd_str = os.getcwd()
# 디렉터리 위치 리턴

str = '/home/mytext.txt'
dirname_str = os.path.dirname(str)
# 파일 디렉터리 리턴

basename_str = os.path.basename(str)
# 경로 파일명 리턴

s = os.system('ls -al')
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
# 파일 이름 a에서 b로 변경

dir_list = os.listdir()
# 디렉터리 목록 티런

os.makedirs('dir/sub_dir')
# 하위 경로 폴더 생성

os.mkdir('dir2')
# 폴더 생성

os.removedirs('dir/sub_dir')
# 하위 경로 폴더 삭제

os.rmdir('dir2')
# 폴더 삭제

# stat_str = os.stat('readme.md')
# 파일 상태 확인