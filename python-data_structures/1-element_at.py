def element_at(my_list, idx):
    """Siyahıdan müəyyən indeksdəki elementi qaytarır."""
    
    # İndeks mənfi olarsa None qaytar
    if idx < 0:
        return None
    
    # İndeks siyahının uzunluğundan böyük və ya bərabərdirsə None qaytar
    # (Siyahı indeksləri 0-dan başladığı üçün len(my_list) - 1 sonuncu indeksdir)
    if idx >= len(my_list):
        return None
    
    # Əgər yuxarıdakı şərtlər ödənmirsə, elementi qaytar
    return my_list[idx]
