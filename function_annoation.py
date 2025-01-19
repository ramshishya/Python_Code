def funcation_annoation(ham:str,eggs:str='eggs')->str:
    print("Annonation",funcation_annoation.__annotations__)
    print("Arguments:",ham,eggs)
    return ham+'and'+eggs
funcation_annoation('spam')