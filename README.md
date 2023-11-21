# Transportation Problem Optimization

This Python program solves the transportation problem using three different methods: North-West corner method, Vogel's approximation method, and Russell's approximation method. The transportation problem involves finding the optimal way to transport goods from multiple suppliers to multiple consumers at the minimum cost.

## Installation

To run the Transportation Problem Optimization program, follow these steps:

1. Clone the GitHub repository:

```bash
git clone https://github.com/Amir23714/Optimization3.git
cd Optimization3
```

Install the required dependencies using pip:
```bash
pip install -r requirements.txt
```

## Input

The program takes the following inputs:

1. **Supply Vector:** The supply amounts from each supplier.
2. **Demand Vector:** The demand amounts from each consumer.
3. **Cost Table:** The cost of transporting one unit from each supplier to each consumer.

Here is an example of the input:

```plaintext
Input the supply vector for your transportation problem:
300 400 500
Input the demand vector for your transportation problem
250 350 400 200
Input the cost table for your transportation problem:
3 1 7 4
2 6 5 9
8 3 3 2
```
## Output

The program provides the solutions for the transportation problem using three different methods. The output is presented in a tabular format using the PrettyTable library.

Here is an example of the output:

```plaintext
+--------+-----+-----+-----+-----+--------+
|        |  D1 |  D2 |  D3 |  D4 | Supply |
+--------+-----+-----+-----+-----+--------+
|   S1   |  3  |  1  |  7  |  4  |  300   |
|   S2   |  2  |  6  |  5  |  9  |  400   |
|   S3   |  8  |  3  |  3  |  2  |  500   |
| Demand | 250 | 350 | 400 | 200 |        |
+--------+-----+-----+-----+-----+--------+
Answer for North-West corner method is:
+---+-----+-----+-----+-----+
| № |  1  |  2  |  3  |  4  |
| 1 | 250 |  50 |  0  |  0  |
| 2 |  0  | 300 | 100 |  0  |
| 3 |  0  |  0  | 300 | 200 |
+---+-----+-----+-----+-----+
Answer for Vogel's approximation method is:
+---+-----+-----+-----+-----+
| № |  1  |  2  |  3  |  4  |
| 1 |  0  | 300 |  0  |  0  |
| 2 | 250 |  0  | 150 |  0  |
| 3 |  0  |  50 | 250 | 200 |
+---+-----+-----+-----+-----+
Answer for Russell's approximation method is:
+---+-----+-----+-----+-----+
| № |  1  |  2  |  3  |  4  |
| 1 |  0  | 300 |  0  |  0  |
| 2 | 250 |  50 | 100 |  0  |
| 3 |  0  |  0  | 300 | 200 |
+---+-----+-----+-----+-----+
```

The numbers in the table represent the optimal amounts to be transported from each supplier to each consumer.

## Not applicable/balanced
When there is at least one negative number in the table or in the supply or demand vectors

```plaintext
The method is not applicable!
```

When the amount is in supply != amount in demand

```plaintext
The method is not applicable!
```
