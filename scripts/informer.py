import pandas as pd

def apply_df_method(df, method_name, *args, **kwargs):
    """
    Apply a method of a DataFrame dynamically.

    Parameters:
        df (pd.DataFrame): The DataFrame to operate on.
        method_name (str): The name of the DataFrame method (e.g., "mean", "shape").
        *args: Positional arguments to pass to the method.
        **kwargs: Keyword arguments to pass to the method.

    Returns:
        Result of the method call.
    """
    # Get the method
    if hasattr(df, method_name):
        method = getattr(df, method_name)
        # If it's callable (like df.mean()), call it
        if callable(method):
            return method(*args, **kwargs)
        else:
            return method  # For properties like df.shape or df.columns
    else:
        raise AttributeError(f"'{type(df).__name__}' object has no method or attribute '{method_name}'")