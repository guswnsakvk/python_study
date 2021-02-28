import pickle

# 파일 생성
with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file))

# 파일에 쓰기
with open("study.txt", "w", encoding="utf8") as study_file:
    study_file.write("파이썬을 열심히 공부하고 있어요")

# 파일 읽기
with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())