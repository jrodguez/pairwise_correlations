def corr_row_i_row_j(row_i, row_j):
    """This function will compute the correlation between one row, i, and a second row, j"""
    return row_i.corr(row_j)

def corr_row_i_vs_all(df, index_i, row_i, corr_matrix):
    """This function, after having specified a row, i, will compute the correlation matrix between row i
    and every other row in the dataframe"""
    for index_j, row_j in df.iterrows():# pd.itterows will itterate over every row in the dataframe
        corr_matrix.loc[index_i, index_j] = corr_row_i_row_j(row_i, row_j) #computes correlation and saves to matrix
        corr_matrix.loc[index_j, index_i] = corr_matrix.loc[index_i, index_j]
    return

def pairwise_correlation(df):
    """This function will create an empty correlation matrix and itterate over every row to compute the correlation 
    against every row, and return the filled correlation matrix with the results."""
    corr_matrix = pd.DataFrame()
    for index_i, row_i in df.iterrows():
        corr_row_i_vs_all(df, index_i, row_i, corr_matrix)
    return corr_matrix
