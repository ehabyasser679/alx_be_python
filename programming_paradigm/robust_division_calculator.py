from typing import Union


def safe_divide(numerator, denominator) -> Union[float, str]:
	try:
		num = float(numerator)
		den = float(denominator)
	except (ValueError, TypeError):
		return "Error: non-numeric input"

	try:
		return f"The result of the division is {num / den}"
	except ZeroDivisionError:
		return "Error: Cannot divide by zero."


__all__ = ["safe_divide"]

