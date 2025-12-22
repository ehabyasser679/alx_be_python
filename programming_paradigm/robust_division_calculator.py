from typing import Union


def safe_divide(numerator, denominator) -> Union[float, str]:
	try:
		num = float(numerator)
		den = float(denominator)
	except (ValueError, TypeError):
		return "Error: Please enter numeric values only."

	try:
		return num / den
	except ZeroDivisionError:
		return "Error: Cannot divide by zero."


__all__ = ["safe_divide"]



