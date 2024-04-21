import re
import os



def search_markdown_document(search_words):
    file_path = os.path.abspath(os.path.join(os.getcwd(), "README.md"))

    result = {}
    current_section = ""
    current_subsection = ""
    in_target_section = False
    in_target_subsection = False

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # Check for section headers
            if line.startswith('#'):
                current_section = line.strip('# ').strip()
                in_target_section = any(word.lower() in current_section.lower() for word in search_words)
                current_subsection = ""  # Reset subsection when a new section is encountered

            # Check for subsection headers
            elif line.startswith('##'):
                current_subsection = line.strip('## ').strip()
                in_target_subsection = any(word.lower() in current_subsection.lower() for word in search_words)

            # Check for search words within the section or subsection
            if in_target_section or in_target_subsection:
                for word in search_words:
                    if re.search(fr'\b{re.escape(word)}\b', line, re.IGNORECASE):
                        section_dict = result.setdefault(current_section, {})
                        subsection_dict = section_dict.setdefault(current_subsection, [])
                        subsection_dict.append(line.strip())

    return result

# Example usage:
search_words = ["Numberlists"]

result = search_markdown_document(search_words)

if result:
    for section, content in result.items():
        print(f"Section: {section}")
        print("\n".join(content))
        print("-" * 30)
else:
    print("No matching sections found.")
