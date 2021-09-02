def kaggle_root():
    import kaggle
    config_values = kaggle.api.config_values
    root = config_values['path']
    return root