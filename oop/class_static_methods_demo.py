class Calculator:
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Static method to add two numbers.
        
        Static methods don't require access to class or instance data.
        They can be called on the class without creating an instance.
        
        Args:
            a (float): First number
            b (float): Second number
            
        Returns:
            float: Sum of a and b
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Class method to multiply two numbers.
        
        Class methods have access to class attributes through the cls parameter.
        They can be called on the class without creating an instance.
        
        Args:
            cls: Reference to the Calculator class
            a (float): First number
            b (float): Second number
            
        Returns:
            float: Product of a and b
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b

