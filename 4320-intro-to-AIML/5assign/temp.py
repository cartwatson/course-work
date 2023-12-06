# all information around usage is numerical in nature, it will undergo standard scaling to normalize the data
numerical_transformer = StandardScaler()
numerical = ["customer service calls", "total day minutes", "total day charge", "total eve minutes", "total eve charge", "total night minutes", "total night charge", "total intl minutes", "total intl charge", "number customer service calls"]

# all information that is categorical will be one hot encoded to allow for the model to understand the data in an appropriate way
categorical_transformer = OneHotEncoder(handle_unknown="ignore")
categorical = ["state", "area code"]

# all information that is boolean will be one hot encoded and translated from yes/no to boolean values
boolean_transformer = OneHotEncoder(handle_unknown="ignore")
boolean = ["international plan", "voice mail plan"]
for category in boolean:
    X_train[category] = X_train[category].replace({'Yes': 1, 'No': 0})

# phone number shouldn't have an effect on churn, so it will be dropped
drop = ["phone number"]

ColumnTransformer = make_column_transformer(
    (numerical_transformer, numerical),
    (categorical_transformer, categorical),
    (boolean_transformer, boolean),
    ("drop", drop),
)