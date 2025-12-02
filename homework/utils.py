import requests
import json

def get_max(numbers):
    if not numbers:
        raise ValueError("Список не должен быть пустым")
    return max(numbers)


def get_min(numbers):
    if not numbers:
        raise ValueError("Список не должен быть пустым")
    return min(numbers)


def get_average(numbers):
    if not numbers:
        raise ValueError("Список не должен быть пустым")
    return sum(numbers) / len(numbers)
