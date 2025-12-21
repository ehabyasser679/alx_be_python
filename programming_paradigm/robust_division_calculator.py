from typing import Union


def safe_divide(numerator, denominator) -> Union[float, str]:
	try:
		num = float(numerator)
		den = float(denominator)
	except (ValueError, TypeError):
		return "Error: non-numeric input"

	try:
		return num / den
	except ZeroDivisionError:
		return "Error: division by zero"


__all__ = ["safe_divide"]

