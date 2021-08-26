import sys

job_count = int(sys.argv[1])
workload1 = 0
workload2 = 0
workload3 = 0
for job in range(job_count):
    print("Podaj liczbę godzin pracy dla zlecenia")
    job_hours = int(input())
    if job_hours <= 0:
        print("Błąd: Nieprawidłowa liczba godzin!")
        break
    if workload3 < workload1 and workload3 < workload2:
        workload3 += job_hours
    elif workload2 < workload1:
        workload2 += job_hours
    else:
        workload1 += job_hours
print("Najbliży mechanik będzie wolny w ciągu {} dni".format(
    int((min(workload1, workload2, workload3)+7)  / 8)
))
print("Wszyscy mechanicy będą wolni w ciągu {} dni".format(
    int((max(workload1, workload2, workload3)+7)  / 8)
))