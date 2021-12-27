import hst

# printing-the-extracted-raw-data
print('\nBoth Stocks Closing Data over past 4 years\n')
print(hst.sdf)
print('\nBoth Stock Returns over past 4 years\n')
print(hst.returns)

# data-printing
print('\nMonthly Stats')
print('\nMonthly Standard Deviation')
print(hst.monstd)
print('\nMonthly Average Return')
print(hst.monavgmean)
print('\nMonthly Geometric Return')
print(hst.mongeomean)
print('\nAnnual Stats')
print('\nAnnual Standard Deviation')
print(hst.annstd)
print('\nAnnual Average Return')
print(hst.annavgmean)
print('\nAnnual Geometric Return')
print(hst.anngeomean)
print('\nCorrelation of the Stocks')
print(hst.corr)
print('\nCovariance of the Stocks')
print(hst.covar)
print('\nVariance of the Stocks')
print(hst.var)
