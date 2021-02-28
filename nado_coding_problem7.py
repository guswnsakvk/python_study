#내 코드
for i in range(50):
    with open(str(i+1) + "주차.txt", "w", encoding="utf8") as report:
        report.write(" - {0} 주차 주간보고 -".format(i+1))
        report.write(" 부서 :")
        report.write(" 이름 :")
        report.write(" 업무 요약 :")

# 나도 코딩 코드
for i in range(1, 51):
    with open(str(i) + "주차.txt", "w", encoding="utf8") as report_file:
        report_file.write(" - {0} 주차 주간보고 -".format(i))
        report_file.write("\n 부서 :")
        report_file.write("\n 이름 :")
        report_file.write("\n 업무 요약 :")