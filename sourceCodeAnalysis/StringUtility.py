def sanitize(str):
    str=str.replace("Fxn:","")
    if ("(" in str):
        arg = str.split("(")[1]
        str = str.split("(")[0]
    str=str.replace("self.","")

    return str