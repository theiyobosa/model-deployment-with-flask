from joblib import load
from os import getcwd

def predict(x: float):
    """
    This function loads the model from the 'modelling' directory,
    and makes a prediction with the input value 'x'.
    
    Args:
        x: [float] the input for the model

    Return:
        output: [float] the predicted value from the input
    """
    
    model_location = 'modelling\\model.joblib' #getcwd() + "\modelling\\model.joblib"
    model = load(model_location)

    # Convert 'x' to 2D list
    X = [[x]]

    output = model.predict(X)

    # Clear variables and the model from memory
    del model_location
    del model
    del X

    return output