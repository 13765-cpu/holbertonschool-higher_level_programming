#!/usr/bin/python3
def multiple_returns(sentence):
    # Cümlənin uzunluğunu hesablayırıq
    length = len(sentence)
    
    # Əgər cümlə boşdursa (uzunluq 0-dırsa), ilk xarakter None olur
    if length == 0:
        first_char = None
    else:
        # Əks halda ilk xarakteri götürürük
        first_char = sentence[0]
    
    # Nəticəni tuple şəklində qaytarırıq
    return (length, first_char)
