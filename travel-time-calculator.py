# Day 37 - Travel Time Calculator (2026-11-12)
# What it does: Calculates how long a journey will take from distance and
# average speed, and what time you will arrive if you leave at a given time.
# Also works out the speed you need to arrive by a deadline.
# Useful for: anyone planning a trip, commute or bus/train journey -
# know your arrival time before you leave home.

from datetime import datetime, timedelta


def travel_time_hours(distance_km, speed_kmh):
    """Return travel time in hours for a distance at an average speed."""
    if distance_km < 0:
        raise ValueError("Distance cannot be negative.")
    if speed_kmh <= 0:
        raise ValueError("Speed must be greater than zero.")
    return distance_km / speed_kmh


def format_duration(hours):
    """Format a duration in hours as 'Xh Ym' (e.g. 2.5 -> '2h 30m')."""
    total_minutes = round(hours * 60)
    h, m = divmod(total_minutes, 60)
    if h == 0:
        return f"{m}m"
    if m == 0:
        return f"{h}h"
    return f"{h}h {m}m"


def arrival_time(departure, distance_km, speed_kmh):
    """Return the arrival time as a datetime.

    departure: a datetime, or a "HH:MM" string (assumed to be today).
    """
    if isinstance(departure, str):
        departure = datetime.combine(
            datetime.today().date(),
            datetime.strptime(departure, "%H:%M").time(),
        )
    hours = travel_time_hours(distance_km, speed_kmh)
    return departure + timedelta(hours=hours)


def required_speed(distance_km, available_hours):
    """Speed (km/h) needed to cover a distance within the given hours."""
    if distance_km < 0:
        raise ValueError("Distance cannot be negative.")
    if available_hours <= 0:
        raise ValueError("Available time must be greater than zero.")
    return distance_km / available_hours


def plan_trip(distance_km, speed_kmh, departure="08:00"):
    """Print a simple trip plan: travel time and arrival time."""
    hours = travel_time_hours(distance_km, speed_kmh)
    arrive = arrival_time(departure, distance_km, speed_kmh)
    print(f"Distance: {distance_km} km, average speed: {speed_kmh} km/h")
    print(f"Travel time: {format_duration(hours)}")
    print(f"Leave at {departure} -> arrive at {arrive.strftime('%H:%M')}")
    return arrive


if __name__ == "__main__":
    # Example 1: Dhaka to Chattogram by bus (~250 km at 50 km/h)
    plan_trip(250, 50, "08:00")
    print()

    # Example 2: Daily commute - 18 km across town at 25 km/h
    plan_trip(18, 25, "09:00")
    print()

    # Example 3: How fast must I drive to cover 120 km in 2 hours?
    print(f"Need to reach 120 km in 2 hours: "
          f"{required_speed(120, 2):.0f} km/h")
