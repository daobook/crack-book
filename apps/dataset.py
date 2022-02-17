def kaggle_root():
    import kaggle
    config_values = kaggle.api.config_values
    return config_values['path']