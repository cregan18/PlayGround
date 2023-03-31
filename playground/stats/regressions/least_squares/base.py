import numpy as _np
import pandas as _pd
from functools import reduce as _reduce


def _compute_least_squares_betas(x, y, omega=None):
    """
    Finds the least squares solution with x, y, and an optional covariance matrix omega,
    which can be used to implement WLS or GLS.
    :param x:
    :param y:
    :param omega:
    :return:
    """

    assert x.shape[0] == y.shape[0], "X and Y matrices/vectors are not aligned."

    if not omega:
        omega = _np.eye(y.shape[0])

    betas = _reduce(_np.dot, [_np.linalg.inv(_reduce(_np.dot, [x.T, omega, x])), x.T, omega, y])

    return betas


def _compute_ols_betas(x, y, add_constant=True):
    """

    :param x:
    :param y:
    :param add_constant: Default is True
    :return:
    """

    assert type(x) == _pd.DataFrame
    assert type(y) in [_pd.Series, _pd.DataFrame]
    
    if add_constant:
        x["Intercept"] = 1.0
        x = x.loc[:, ["Intercept"] + x.columns.tolist()]

    betas = _compute_least_squares_betas(x=x.values, y=y.values)

    if type(y) == _pd.Series:
        betas = _pd.Series(betas, index=x.columns)
    else:
        betas = _pd.DataFrame(betas, index=x.columns, columns=y.columns)

    return betas
