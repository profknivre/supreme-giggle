__author__ = 'zebrowsk'

quiet_hours = list(range(0, 6)) + list(range(23, 24))
weekend_quiet_hours = list(range(0, 9)) + list(range(22, 24))


def is_quiet_time(current_time):
    if current_time.tm_wday in (5, 6):  # weekend
        if current_time.tm_hour in weekend_quiet_hours:
            return True
    else:
        if current_time.tm_hour in quiet_hours:
            return True
    return False


def main():
    from time import localtime
    if not is_quiet_time(localtime()):
        import xmlrpc.client
        from time import sleep

        s = xmlrpc.client.ServerProxy('http://44.0.0.171:8000')
        for i in range(2):
            s.toggle(0)  # tick tok
            sleep(1)

        s.off(0)


if __name__ == '__main__':
    main()
