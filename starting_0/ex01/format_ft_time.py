
def main():
    from time import time
    from datetime import datetime
    ''' #ref:
    - https://www.daleseo.com/python-time/
    - https://peps.python.org/pep-0378/
    - string type
    - https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
    '''

    ''' 출력문 예시
    Seconds since January 1, 1970: 1,666,355,857.3622 or 1.67e+09 in scientific notation$
    Oct 21 2022$
    '''
    cur_utime = time()
    '''
    print(f"{cur_utime:,.4f}")
    formatted_utime = format(cur_utime, ",.4f")
    print(f"{formatted_utime=}")
    print(f"Seconds since January 1, 1970: {formatted_utime} or {cur_utime:.2e} in scientific notation")
    '''
    print(f"Seconds since January 1, 1970: {cur_utime:,.4f} or {cur_utime:.2e} in scientific notation")

    # cur_datetime = datetime.time()
    # print(f"Seconds since January 1, 1970: #{cur_utime} or 1.67e+09 in scientific notation")
    cur_datetime = datetime.fromtimestamp(cur_utime) # https://docs.python.org/3/library/datetime.html#datetime.datetime
    '''
    datetime.strptime('31/01/22 23:59:59.999999',
                  '%d/%m/%y %H:%M:%S.%f')
    datetime.datetime(2022, 1, 31, 23, 59, 59, 999999)
    _.strftime('%a %d %b %Y, %I:%M%p')
    'Mon 31 Jan 2022, 11:59PM'

    %b: Month as locale’s abbreviated name.

    TOBE: Oct 21 2022$
    '''
    print(cur_datetime.strftime('%b %d %Y'))


if __name__ == "__main__":
    main()