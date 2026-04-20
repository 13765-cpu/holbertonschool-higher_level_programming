import os

def generate_invitations(template, attendees):
    # 1. Giriş tiplərinin yoxlanılması (Check Input Types)
    if not isinstance(template, str):
        print(f"Error: Template must be a string. Got {type(template).__name__}")
        return
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print(f"Error: Attendees must be a list of dictionaries. Got {type(attendees).__name__}")
        return

    # 2. Boşluq yoxlanılması (Handle Empty Inputs)
    if not template:
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # 3. Hər bir iştirakçı üçün emal (Process Each Attendee)
    for index, person in enumerate(attendees, start=1):
        content = template
        
        # Şablondakı açarlar (DİQQƏT: tək mötərizə!)
        keys = ["name", "event_title", "event_date", "event_location"]
        
        for key in keys:
            # Məlumat yoxdursa və ya None-dursa "N/A" qoy
            value = person.get(key)
            if value is None:
                value = "N/A"
            
            # Placeholder-i dəyiş (Şablon {name} formatındadır)
            placeholder = "{" + key + "}"
            content = content.replace(placeholder, str(value))
        
        # 4. Fayla yazmaq (Generate Output Files)
        filename = f"output_{index}.txt"
        
        # Hints: os.path.exists və try-except istifadəsi
        try:
            if os.path.exists(filename):
                # Fayl artıq varsa, üstünə yazılacağını bildirə bilərsən (istəyə bağlı)
                pass
            
            with open(filename, "w") as f:
                f.write(content)
        except Exception as e:
            print(f"Error occurred while writing to {filename}: {e}")
