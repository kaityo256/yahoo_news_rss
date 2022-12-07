import datetime


def hours_from_standard_time(filename, reference_date):
    """
    ファイル名を受け取り、基準となる時刻からの経過時間(hour)を返す関数
    """
    datestr = filename[:13]  # 最初の13文字を切り出す
    current_date = datetime.datetime.strptime(datestr, '%Y-%m-%d-%H')
    dt = current_date - reference_date
    hours = int(dt.total_seconds() / 3600)
    return hours


def days_from_standard_time(filename, reference_date):
    """
    ファイル名を受け取り、基準となる時刻からの経過日数(days)を返す関数
    """
    datestr = filename[:13]  # 最初の13文字を切り出す
    current_date = datetime.datetime.strptime(datestr, '%Y-%m-%d-%H')
    dt = current_date - reference_date
    return dt.days


def main():
    # 基準時間(いつでも良いが、たとえば2022年9月1日)
    reference_date = datetime.datetime.strptime('2022-09-01', '%Y-%m-%d')

    # XMLのファイル名
    filename = "2022-09-03-11-top-pics.xml"
    hours = hours_from_standard_time(filename, reference_date)
    print(f"{hours} hours")  # 2日と11時間なので59 hoursになる。
    days = days_from_standard_time(filename, reference_date)
    print(f"{days} days")  # 2日と11時間なので2 daysとなる。


if __name__ == '__main__':
    main()
