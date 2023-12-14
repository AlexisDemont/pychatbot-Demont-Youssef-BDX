def transpose_this( matrice ):
    """
      Function that transpose a matrix

      Parameters:
          matrix

      Returns:
          transposed matrix
      """
    rows = len(matrice)
    columns = len(matrice[0])
    transposedMatrice = [[0]*rows for k in range (columns)]
    for i in range (columns):
        for j in range (rows):
            transposedMatrice[i][j] = matrice[j][i]

    return transposedMatrice


