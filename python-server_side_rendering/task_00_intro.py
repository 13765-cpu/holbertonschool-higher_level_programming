import os

def generate_invitations(template, attendees):
    # 1. Giriş tiplərinin yoxlanılması (Input Types Check)
    if not isinstance(template, str):
        print("Error: template must be a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: attendees must be a list of dictionaries.")
        return

    # 2. Boşluq yoxlanılması (Handle Empty Inputs)
    if not template.strip():
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # 3. Hər bir iştirakçı üçün emal (Process Each Attendee)
    for index, person in enumerate(attendees, start=1):
        content = template
        
        for key in ["name", "event_title", "event_date", "event_location"]:
            # Sənin yazdığın məntiq bura daxil olur:
            value = person.get(key)
            if value is None:
                value = "N/A"
            
            placeholder = f"{{{{{key}}}}}" # Bu {{key}} deməkdir
            content = content.replace(placeholder, str(value))
        
        # 4. Fayla yazmaq (Generate Output Files)
        filename = f"output_{index}.txt"
        try:
            with open(filename, "w") as f:
                f.write(content)
        except Exception as e:
            print(f"Error writing to {filename}: {e}")
