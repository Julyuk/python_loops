def list_to_float_converter(array):
    result=[]
    for i in array:
        if type(i) == int:
            result.append(float(i))
    print(result)
    return result
list_to_float_converter([1,2,3,4])