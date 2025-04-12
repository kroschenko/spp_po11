from collections import Counter
from datetime import datetime

from matplotlib import pyplot as plt


def show_plot(commit_dates):
    monthly_activity = analyze_commit_activity(commit_dates)
    plot_activity(monthly_activity)


def analyze_commit_activity(commit_dates):
    monthly_activity = Counter()
    for date in commit_dates:
        month = datetime.strptime(date, "%Y-%m-%dT%H:%M:%SZ").strftime("%Y-%m")
        monthly_activity[month] += 1
    return monthly_activity


def plot_activity(monthly_activity):
    sorted_activity = sorted(monthly_activity.items())
    months, counts = zip(*sorted_activity)

    plt.figure(figsize=(10, 6))
    plt.bar(months, counts, color="skyblue")
    plt.xlabel("Month")
    plt.ylabel("Number of commits")
    plt.title("User activity by month")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
