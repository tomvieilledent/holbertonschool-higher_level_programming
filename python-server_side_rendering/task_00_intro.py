#!/usr/bin/python3

def generate_invitations(template_content, attendees):

    if not isinstance(template_content, str):
        raise TypeError("template must be a string")
    if template_content == "":
        raise ValueError("template  must not be empty")

    if not isinstance(attendees, list):
        raise TypeError("attendees must be a list")
    if not attendees:
        raise ValueError("attendees list must not be empty")

    for i, participant in enumerate(attendees, start=1):
        if not isinstance(participant, dict):
            raise TypeError(
                "Item {} in attendees must be a dictionary".format(i))

        data = {
            "name": participant.get("name") or "N/A",
            "event_title": participant.get("event_title") or "N/A",
            "event_date": participant.get("event_date") or "N/A",
            "event_location": participant.get("event_location") or "N/A"
        }

        mail = template_content.format(**data)
        file_name = "output_{}.txt".format(i)
        with open(file_name, "w", encoding="utf-8") as f:
            f.write(mail)
