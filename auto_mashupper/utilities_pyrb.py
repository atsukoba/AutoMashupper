from pyrubberband import pyrb


def change_tempo(y, sr, X, Y, rbargs=None):
    """Multiply the frequencies inside an audio time series.
    The equivalent of the --tempo <X>:<Y> option.

    NOTE: This function is originally implemented in pyrubberband repo pull request created by @migperfer
    https://github.com/bmcfee/pyrubberband/pull/19, which is not yet merged.

    FIXME: This function should be removed once the pull request is merged.

    Parameters
    ----------
    y : np.ndarray [shape=(n,) or (n, c)]
        Audio time series, either single or multichannel

    sr : int > 0
        Sampling rate of `y`

    X : float
        Base tempo

    Y : float
        Final tempo

    rbargs
        Additional keyword parameters for rubberband

        See `rubberband -h` for details.

    Returns
    -------
    y_shift : np.ndarray
        tempo-shifted audio
    """

    if X == 0:
        return y

    if rbargs is None:
        rbargs = dict()

    rbargs.setdefault("--tempo", "%s:%s" % (X, Y))

    return pyrb.__rubberband(y, sr, **rbargs)


def frequency_multiply(y, sr, X, rbargs=None):
    """Multiply the frequencies inside an audio time series.
    The equivalent of the -f option.

    NOTE: This function is originally implemented in pyrubberband repo pull request created by @migperfer
    https://github.com/bmcfee/pyrubberband/pull/19, which is not yet merged.

    FIXME: This function should be removed once the pull request is merged.

    Parameters
    ----------
    y : np.ndarray [shape=(n,) or (n, c)]
        Audio time series, either single or multichannel

    sr : int > 0
        Sampling rate of `y`

    X : float
        Shift magnitudes in spectrum by X

    rbargs
        Additional keyword parameters for rubberband

        See `rubberband -h` for details.

    Returns
    -------
    y_shift : np.ndarray
        frequency-multiplied audio
    """

    if X == 0:
        return y

    if rbargs is None:
        rbargs = dict()

    rbargs.setdefault("--frequency", X)

    return pyrb.__rubberband(y, sr, **rbargs)
