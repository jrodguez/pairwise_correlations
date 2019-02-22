import pandas as pd
import numpy as np
import df_utils

def test_corr_row_i_row_j():
    """This is a test function for corr_row_i_row_j"""
    #introducing the dataframe 
    df = pd.DataFrame([[-1, 0, 1], [1, 0, -1], [.5, 0, .5]], index = ['A', 'B', 'C'], columns = ['v1', 'v2', 'v3'])
    #assert statements
    assert int(df_utils.corr_row_i_row_j(df.loc['A'], df.loc['A'])) == 1 #value of correlation for row A to A should be 1
    assert int(df_utils.corr_row_i_row_j(df.loc['A'], df.loc['B'])) == -1 #value of correlation for row A to B should be -1
    assert int(df_utils.corr_row_i_row_j(df.loc['A'], df.loc['C'])) == 0 #value of correltion for row A to B should be 0
    return

def test_corr_row_i_vs_all():
    """This is a test function for corr_row_i_vs_all"""
    #introducing the dataframe 
    df = pd.DataFrame([[-1, 0, 1], [1, 0, -1], [.5, 0, .5]], index = ['A', 'B', 'C'], columns = ['v1', 'v2', 'v3'])
    
    #introducing empty correlation matrix
    corr_matrix = pd.DataFrame()
    
    #Checking that dataframe has more than one row for pd.iterrows to function properly
    assert len(df.index) > int(1), "pd.iterrows cannot iterate because dataframe only has one row" 
    
    #Checking that all rows in correlation matrix get filled, without any NaN's.
    df_utils.corr_row_i_vs_all(df, 'A', df.loc['A'], corr_matrix)
    df_utils.corr_row_i_vs_all(df, 'B', df.loc['B'], corr_matrix)
    df_utils.corr_row_i_vs_all(df, 'C', df.loc['C'], corr_matrix)
    
    assert df.isnull().values.any() == False,  "null (NaN) values are present, not iterating correctly"
    
   #Checking that the function is outputting the correct matrix symmetry
    assert corr_matrix.at['A', 'B'] == corr_matrix.at['B', 'A'], "The function is not outputting the correct symmetry"
    assert corr_matrix.at['B', 'C'] == corr_matrix.at['C', 'B'], "The function is not outputting the correct symmetry"
    
    return

def test_pairwise_correlation():
    """This is a test function for pairwise_correlation"""

    #introducing the dataframe 
    df = pd.DataFrame([[-1, 0, 1], [1, 0, -1], [.5, 0, .5]], index = ['A', 'B', 'C'], columns = ['v1', 'v2', 'v3'])
    
    #introducing empty correlation matrix
    corr_matrix = pd.DataFrame()
    
    #Checking that the dataframe and correaltion matrix passed are indeed dataframes, and not an integer, string, etc. 
    assert isinstance(df, pd.DataFrame), "Data is not part of a dataframe" 
    assert isinstance(corr_matrix, pd.DataFrame), "correlation matrix is not part of a dataframe"
    
    #Checking that the datarame passed is not empty, for example, if one mixed up labeling of the dataframe and corr_matrix
    assert df.empty == False, "Dataframe is empty" 
    
    #Checking that the correlation matrix is empty, so the correlations computed by the fucntion can be saved in the matrix.
    assert corr_matrix.empty == True, "Correlation matrix needs to be empty to correctly save the computations"
    
    #Checking that dataframe has more than one row for pd.iterrows to function properly
    assert len(df.index) > int(1), "pd.iterrows cannot iterate because dataframe only has one row" 
    
    return
