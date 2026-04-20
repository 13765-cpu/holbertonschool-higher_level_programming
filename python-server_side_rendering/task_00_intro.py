import os

def generate_invitations(template, attendees):
    # 1. Giriş tiplərinin yoxlanılması
    if not isinstance(template, str):
        # Şərtdə "log an error message" deyilir, tipini də qeyd etmək olar
        print(f"Error: Invalid input type for template. Expected str, got {type(template).__name__}")
        return
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print(f"Error: Invalid input type for attendees. Expected list of dictionaries, got {type(attendees).__name__}")
        return

    # 2. Boşluq yoxlanılması (Şərtdəki dəqiq mesajlar)
    if not template:
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # 3. Proses
    for index, person in enumerate(attendees, start=1):
        content = template
        
        # Əvəz olunacaq açarlar
        placeholders = ["name", "event_title", "event_date", "event_location"]
        
        for key in placeholders:
            # Dəyəri götür və None olub-olmadığını yoxla
            value = person.get(key)
            if value is None:
                value = "N/A"
            
            # Placeholder-i dəyiş
            target = "{{" + key + "}}"
            content = content.replace(target, str(value))
        
        # 4. Fayla yazmaq
        filename = f"output_{index}.txt"
        try:
            with open(filename, "w") as f:
                f.write(content)
        except Exception as e:
            print(f"Error writing to {filename}: {e}")
