import os

def generate_invitations(template, attendees):
    # 1. Tip yoxlamaları (Testin tələbinə uyğun)
    if not isinstance(template, str):
        print(f"Error: Invalid input type for template. Expected str, got {type(template).__name__}")
        return
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print(f"Error: Invalid input type for attendees. Expected list of dictionaries, got {type(attendees).__name__}")
        return

    # 2. Boşluq yoxlamaları
    if not template:
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # 3. İştirakçıların emalı
    for index, person in enumerate(attendees, start=1):
        content = template
        
        # Hər bir placeholder üçün dəyişiklik
        for key in ["name", "event_title", "event_date", "event_location"]:
            # Məlumatı al, yoxdursa və ya None-dursa N/A et
            value = person.get(key)
            if value is None or value == "":
                value = "N/A"
            
            placeholder = "{{" + key + "}}"
            content = content.replace(placeholder, str(value))
        
        # 4. Fayla yazma
        filename = f"output_{index}.txt"
        with open(filename, "w") as f:
            f.write(content)
