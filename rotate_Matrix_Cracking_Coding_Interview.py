def rotate(matrix):
    results = []
    for col in range(len(matrix)):
        inner = []

        for row in range(len(matrix)):
            item = matrix[row][col]
            inner.insert(0,item);
        results.append(inner);
  
    return results
