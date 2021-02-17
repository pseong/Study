import os

environ_dic = os.environ
# 환경변수

os.chdir('/home')
# 디렉터리 위치 변경

pwd_str = os.getcwd()
# 디렉터리 위치 리턴

s = os.system('ls -al')
# 시스템 명령어 호출

f_str = os.popen('ls -al').read()
# 시스템 결과값 받아오기

os.mkdir('')
# 폴더 생성

os.rmdir('')
# 폴더 삭제

os.unlink('')
# 파일 삭제

os.rename('a', 'b')
# 파일 이름 a에서 b로 변경