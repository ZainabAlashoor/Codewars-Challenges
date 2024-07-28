# Codewars :: Calculate average

def find_average(numbers):
    try:
        return sum(numbers) / len(numbers)
    except:
        return 0