# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import itertools
import math


def total_completion(schedule):
    prev = 0
    metric = 0
    for job in schedule:
        metric += job.processing+prev
        prev += job.processing
    return metric


def total_weighted_completion(schedule):
    prev = 0
    metric = 0
    for job in schedule:
        prev += job.processing
        metric += (prev * job.weight)
    return metric

def total_discounted_weighted_completion(schedule, r):
    prev = 0
    metric = 0
    for job in schedule:
        prev += job.processing
        value = (1 - math.exp(-r * prev))
        metric += (value * job.weight)
    return metric


def max_lateness(schedule):
    prev = 0
    metric = 0
    for job in schedule:
        prev += job.processing
        metric = metric if (metric > prev - job.due_date) else prev - job.due_date
    return metric

def total_tardiness(schedule):
    prev = 0
    metric = 0
    for job in schedule:
        prev += job.processing
        metric += max(0, prev - job.due_date)
    return metric

def total_lateness(schedule):
    prev = 0
    metric = 0
    for job in schedule:
        prev += job.processing
        metric += prev - job.due_date
    return metric

def number_tardy_jobs(schedule):
    prev = 0
    metric = 0
    for job in schedule:
        prev += job.processing
        metric += 1 if (prev - job.due_date > 0) else 0
    return metric

class Job:

    def __init__(self, processing, weight=0, release=0, due_date=0):
        self.weight = weight
        self.processing = processing
        self.release = release
        self.due_date = due_date


if __name__ == '__main__':

    jobs = [
        Job(6, due_date=8),  # 3
        Job(5, due_date=10),  # 4
        Job(6, due_date=11),  # 5
        Job(2, due_date=12),  # 1
    ]

    # print(max_lateness(jobs))
    # print(total_tardiness(jobs))

    min_so_far = math.inf
    best_schedule = []
    best_indices = []

    for indexes in itertools.permutations([i for i in range(len(jobs))]):
        schedule = [jobs[i] for i in indexes]
        result = number_tardy_jobs(schedule)
        # print(result)
        min_so_far = min_so_far if min_so_far < result else result
        best_schedule = best_schedule if min_so_far < result else schedule
        best_indices = best_indices if min_so_far < result else indexes

    print(" ")
    print(min_so_far)
    print("Processing Times: ", [i.processing for i in best_schedule])
    print("Jobs: ", [i + 1 for i in best_indices])





