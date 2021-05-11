# Import data
%time data = pd.read_csv('data-1.csv')

# Check the shape of the dataset
data.shape

# Understanding each variables
data.info()

# Checking the first 5 raws and column
pd.set_option('max_columns', 100)
data.head()

# Statistical summary of variables with numerical value
pd.set_option('max_columns', 100)
data.iloc[:,2:].describe()

# Check the descriptive statistics for the categorical column
data.iloc[:, 13:].describe(include= 'object')
