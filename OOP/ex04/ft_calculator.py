class calculator:
    """A simple calculator class for vector operations."""

    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """
        Calculate and print the dot product of two vectors.

        Parameters:
        V1 (list[float]): First vector.
        V2 (list[float]): Second vector.
        """
        result = sum([V1[i] * V2[i] for i in range(len(V2))])
        print(f"Dot product is: {result}")

    def add_vec(V1: list[float], V2: list[float]) -> None:
        """
        Add two vectors element-wise and print the result.

        Parameters:
        V1 (list[float]): First vector.
        V2 (list[float]): Second vector.
        """
        result = [float(V1[i] + V2[i]) for i in range(len(V2))]
        print(f"Add Vector is: {result}")

    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """
        Subtract the second vector from the first vector
        element-wise and print the result.

        Parameters:
        V1 (list[float]): First vector.
        V2 (list[float]): Second vector.
        """
        result = [float(V1[i] - V2[i]) for i in range(len(V2))]
        print(f"Sous Vector is: {result}")
