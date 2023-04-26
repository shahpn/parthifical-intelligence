import re

class Bulletin:
    def __init__(self) -> None:
        pass

    def _get_classes(input):
       matches = re.findall(r'(CMPSC|IST)\s?(\d{3})(w?)', input, re.IGNORECASE)

       if matches:
              course_names = [match[0].upper() + ' ' + match[1] + match[2] for match in matches]
              course_links = ['https://bulletins.psu.edu/search/?search=' + name.replace(' ', '+') + '&psusearchname=%2Fsearch%2F&caturl=%2Fundergraduate' for name in course_names]
              return(course_links)
       else:
              return("No course names found.")

    def _search_history(input):
        link = ['https://www.google.com/search?q=' + input.replace(' ', '+') + 'psu']
        return(link)

    def _search_location(input):
        link = ['https://www.abington.psu.edu/map']
        return(link)

    def _search_professor(input):
        match = re.search(r'(?i)Professor\s(\w+)', input)

        if match:
                professor_name = match.group(1)
                link = ['https://www.abington.psu.edu/directory/results?keys=' + professor_name  +'&type=All']
                return(link)
        else:
                return(f"Professor not found.")