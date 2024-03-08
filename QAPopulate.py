import sqlite3

authors = ["Crevecouer", "Bradford", "Edwards", "Hawthorne", "Poe"]

questions_and_answers = {
    "Crevecouer": [
        ("Known for?", "Farmer."),
        ("When did Crevecouer live?", "18th-century."),
        ("Where born?", "France."),
        ("Another famous work?", "Sketches."),
        ("Naturalized citizen of which country?", "US."),
        ("Influences on writings?", "Experiences."),
        ("Central theme in Crevecouer's Letters?", "Identity."),
        ("Focus on which social class?", "Middle."),
        ("Primary language of writing?", "English."),
        ("Where did Crevecouer spend most of his life?", "US."),
    ],
    "Bradford": [
        ("Who was William Bradford?", "Leader."),
        ("When was the Mayflower Compact signed?", "1620."),
        ("Purpose of the Mayflower Compact?", "Self-governing."),
        ("Where did the Pilgrims arrive in 1620?", "Plymouth."),
        ("First governor of Plymouth Colony?", "Carver."),
        ("Challenges faced by Pilgrims in the New World?", "Weather."),
        ("How long did the Mayflower voyage take?", "66 days."),
        ("Religious group William Bradford belonged to?", "Separatist."),
        ("When did William Bradford pass away?", "1657."),
        ("Bradford's most famous work?", "Plantation."),
    ],
    "Edwards": [
        ("Who was Jonathan Edwards?", "Preacher."),
        ("Birth date and place of Jonathan Edwards?", "1703, Connecticut."),
        ("Famous for?", "Sermon."),
        ("Belonged to which theological movement?", "Awakening."),
        ("Where did Jonathan Edwards serve as a minister?", "Northampton."),
        ("Most significant philosophical work?", "Will."),
        ("Date of Jonathan Edwards' death?", "1758."),
        ("Title of Edwards' famous sermon on predestination?", "God."),
        ("Contribution to American literature?", "Impact."),
        ("Role in the Great Awakening?", "Crucial."),
    ],
    "Hawthorne": [
        ("Who was Nathaniel Hawthorne?", "Novelist."),
        ("Birth date of Nathaniel Hawthorne?", "1804, Massachusetts."),
        ("Famous novel published in 1850?", "Letter."),
        ("Setting of 'The Scarlet Letter'?", "Massachusetts."),
        ("Protagonist of 'The Scarlet Letter'?", "Prynne."),
        ("Symbolic item worn by Hester Prynne?", "Adultery."),
        ("Where did Hawthorne work as a customs surveyor?", "House."),
        ("What is the Hawthorne effect?", "Observation."),
        ("Date of Nathaniel Hawthorne's death?", "1864."),
        ("Genre often associated with Hawthorne's works?", "Romanticism."),
    ],
    "Poe": [
        ("Who was Edgar Allan Poe?", "Writer."),
        ("Birth date and place of Edgar Allan Poe?", "1809, Massachusetts."),
        ("Poem that made Poe famous?", "Raven."),
        ("Famous detective character created by Poe?", "Dupin."),
        ("Genre of Poe's writing often associated with mystery and macabre?", "Gothic."),
        ("Famous poem exploring themes of lost love and death?", "Lee."),
        ("Location of Poe's last years of life?", "Maryland."),
        ("Poe's most famous poem about a lost lover?", "Raven."),
        ("Date of Edgar Allan Poe's death?", "1849."),
        ("Famous short story about a man who walls up his friend in a cellar?", "Amontillado."),
    ],
}

def populate_tables():
    conn = sqlite3.connect("QuarterlyAssessmentDB.sql")
    cursor = conn.cursor()

    for author in authors:
        for question, answer in questions_and_answers[author]:
            cursor.execute(f"INSERT INTO {author} (question, answer) VALUES (?, ?)", (question, answer))

    conn.commit()
    conn.close()

if __name__ == "__main__":
    populate_tables()
