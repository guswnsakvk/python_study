print("java", "python", "c++", sep=" vs ")

scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():
    #print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep = ":")

for num in range(1, 21):
    print("대기번호 : " + str(num).zfill(3))