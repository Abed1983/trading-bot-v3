def moving_average(data, window_size):
    return data['close'].rolling(window=window_size).mean()
