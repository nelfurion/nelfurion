def format_models(models, options):
    if type(models) is list:
        for i in range(len(models)):
            models[i] = format_model(models[i], options);
    else:
        for key, val in models.items():
            if type(val) is list:
                for i in range(len(val)):
                    val[i] = format_model(val[i], options)
            elif type(val) is str:
                models[key] = val.format(**options)

    return models

def format_model(model, options):
    print(model)
    for key, val in model.items():
        if type(val) is str:
            model[key] = val.format(**options)

    return model
