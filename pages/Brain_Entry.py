import os
import datetime
import streamlit as st

hide_streamlit_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Create a 'brain' folder in the current directory if it doesn't exist
if not os.path.exists("brain"):
    os.makedirs("brain")

# Name of the single journal file
journal_file = "brain/brain_journal.txt"

def parse_date(date_string):
    try:
        return datetime.datetime.strptime(date_string, "%m-%d-%Y %A")
    except ValueError:
        return datetime.datetime.strptime(date_string, "%m-%d-%Y")

def get_journal_entries():
    entries = []
    if not os.path.exists(journal_file):
        return entries

    with open(journal_file, "r", encoding="utf-8") as f:
        for line in f:
            if line.startswith("Date: "):
                entry_date = parse_date(line[6:].strip())
                entries.append(entry_date)
    entries.sort(reverse=True)
    return entries

def read_entry(date):
    content = ""
    with open(journal_file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    start_reading = False
    for line in lines:
        if line.startswith("Date: ") and start_reading:
            break

        if start_reading:
            content += line

        if line.startswith("Date: ") and date == parse_date(line[6:].strip()):
            start_reading = True

    return content

def write_entry(date, content):
    new_entry = f"\nDate: {date}\n{content}\n\n"

    # If the journal file does not exist, create it with the new entry
    if not os.path.exists(journal_file):
        with open(journal_file, "w", encoding="utf-8") as f:
            f.write(new_entry)
    else:
        with open(journal_file, "r", encoding="utf-8") as f:
            lines = f.readlines()

        # Remove existing entry if present
        lines_to_remove = set()
        removing_entry = False
        for i, line in enumerate(lines):
            if line.startswith("Date: "):
                if date == line[6:].strip():
                    removing_entry = True
                    lines_to_remove.add(i)
                else:
                    removing_entry = False

            if removing_entry:
                lines_to_remove.add(i)

        lines = [line for i, line in enumerate(lines) if i not in lines_to_remove]

        # Find the correct position for the new entry based on its date
        new_entry_date = parse_date(date)
        position = None
        for i, line in enumerate(lines):
            if line.startswith("Date: "):
                entry_date = parse_date(line[6:].strip())
                if new_entry_date < entry_date:
                    position = i
                    break

        # Insert the new entry at the correct position
        if position is None:
            lines.append(new_entry)
        else:
            lines.insert(position, new_entry)

        # Write the updated journal entries to the file
        with open(journal_file, "w", encoding="utf-8") as f:
            f.writelines(lines)



st.title("Digital Brain Journal Entry ✍️")
st.write("Write a diary journal entry or edit an existing one by selecting on the date picker.")

selected_date = st.date_input("Select the date for the journal entry:", value=datetime.date.today())
formatted_date = selected_date.strftime("%m-%d-%Y %A")
st.write(f"Selected date: {formatted_date}")

entry = ""

if selected_date in get_journal_entries():
    entry = read_entry(selected_date)

new_entry = st.text_area("Write your journal entry:", entry)

if st.button("Submit"):
    write_entry(formatted_date, new_entry)
    st.success("Journal entry saved successfully!")

st.header("Previous Journal Entries")
entries = get_journal_entries()

if entries:
    selected_entry_date = st.selectbox("Select an entry to view:", entries, format_func=lambda x: x.strftime("%m-%d-%Y %A"))

    if st.button("Load Entry"):
        entry_text = read_entry(selected_entry_date)
        st.write(f"**{selected_entry_date.strftime('%m-%d-%Y %A')}**")
        st.markdown(entry_text.replace("\n", "<br>"), unsafe_allow_html=True)

else:
    st.write("No previous entries found.")

st.markdown("---")
st.markdown("")
st.markdown("<p style='text-align: center'><a href='https://github.com/Kaludii'>Github</a> | <a href='https://huggingface.co/Kaludi'>HuggingFace</a></p>", unsafe_allow_html=True)