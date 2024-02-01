import datetime as dt
import pytz

def get_local_time_for_remote_time_alpha2(local_country_2alpha: str, remote_country_2alpha: str, time_to_run_remote_time: str) -> dt.datetime:
    """
    Local = the time of the server
    Remote = the time in the country
    Execute time = is the time to execute on the remote time but without a timezone yet
    :param country_2alpha:
    :type country_2alpha:
    :param time_to_run_remote_time: Should be hour:minute like 12:00
    :type time_to_run_remote_time: str
    :return: The time in amsterdam
    :rtype:
    """
    # Convert the local time to Amsterdam time
    execute_time = dt.datetime.strptime(time_to_run_remote_time, "%H:%M")  # Time to execute the task in the local time, this time does not have a timezone yet
    # Get the local time into the desired timezone
    remote_timezone_name = pytz.country_timezones[remote_country_2alpha][0]
    remote_timezone = pytz.timezone(remote_timezone_name)
    remote_time = dt.datetime.now(remote_timezone)
    remote_time = remote_time.replace(hour=execute_time.hour, minute=execute_time.minute)
    # Convert the local time to Amsterdam time
    local_timezone_name = pytz.country_timezones[local_country_2alpha][0]
    local_timezone = pytz.timezone(local_timezone_name)
    local_time = remote_time.astimezone(local_timezone)
    # Get the Amsterdam hour
    # local_hour = local_time.strftime("%H:%M")
    return local_time


def get_local_time_for_remote_time(local_timezone_name: str, remote_timezone_name: str, time_to_run_remote_time: str) -> dt.datetime:
    """
    Local = local country the server is located
    Remote = remote country where the job has to be timed for
    Execute time = is the time to execute on the remote time but without a timezone yet
    :param local_timezone_name: Example: "Europe/Amsterdam"
    :type remote_timezone_name: Example: "Europe/Berlin"
    :param time_to_run_remote_time: Should be hour:minute like 12:00
    :type time_to_run_remote_time: str
    :return: The time in amsterdam
    :rtype:
    """
    # Convert the local time to Amsterdam time
    execute_time = dt.datetime.strptime(time_to_run_remote_time, "%H:%M")  # Time to execute the task in the local time, this time does not have a timezone yet
    # Get the local time into the desired timezone
    remote_timezone = pytz.timezone(remote_timezone_name)
    remote_time = dt.datetime.now(remote_timezone)
    remote_time = remote_time.replace(hour=execute_time.hour, minute=execute_time.minute)
    # Convert the local time to Amsterdam time
    local_timezone = pytz.timezone(local_timezone_name)
    local_time = remote_time.astimezone(local_timezone)
    # Get the Amsterdam hour
    # local_hour = local_time.strftime("%H:%M")
    return local_time


if __name__ == "__main__":
    # Example usage:
    # country_code_input = input("Enter 2-letter country code: ")
    # amsterdam_time = get_local_time_for_remote_time_alpha2("NL", country_code_input, "12:00")
    a = get_local_time_for_remote_time("Europe/Amsterdam","Brazil/West", "12:00")
    a = get_local_time_for_remote_time_alpha2("NL","US", "12:00")
    print(a.strftime("%H:%M"))

    # print(f"The time in Amsterdam when it will be around 13:00 in {country_code_input.upper()} ({pytz.country_names[country_code_input]}) is: {amsterdam_time} Amsterdam time.")
