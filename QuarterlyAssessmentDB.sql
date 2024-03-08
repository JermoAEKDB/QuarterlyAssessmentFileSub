-- database: :memory:
ATTACH DATABASE 'jeremyocampo@Jerms-MBP QuarterlyAssessmentFolder % ' AS QuarterlyAssessmentConnectionJO;

CREATE TABLE IF NOT EXISTS Categories (
    CategoryID INTEGER PRIMARY KEY,
    CategoryName TEXT NOT NULL
);

INSERT INTO Categories (CategoryName) VALUES
    ('William Bradford'),
    ('Jean De Crevecouer'),
    ('Nathaniel Hawthorne'),
    ('Jonathan Edwards'),
    ('Edgar Allan Poe');

CREATE TABLE IF NOT EXISTS Questions (
    QuestionID INTEGER PRIMARY KEY,
    CategoryID INTEGER,
    QuestionText TEXT NOT NULL,
    FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID)
);

INSERT INTO Questions (CategoryID, QuestionText) VALUES
    (1, 'What is the title of William Bradford''s most famous work?'),
    (1, 'In which year did William Bradford and the Pilgrims arrive in America?'),
    (1, 'Who succeeded William Bradford as the governor of Plymouth Colony?'),
    (1, 'What role did William Bradford play in the development of the Mayflower Compact?'),
    (1, 'Where is William Bradford buried?'),

    (2, 'What is Jean De Crevecouer''s famous work that explores the idea of the American identity?'),
    (2, 'In which century did Jean De Crevecouer write about American life?'),
    (2, 'What term did Jean De Crevecouer coin to describe the American identity?'),
    (2, 'Where was Jean De Crevecouer born?'),
    (2, 'What was Jean De Crevecouer''s occupation in the American colonies?'),

    (3, 'What is the title of Nathaniel Hawthorne''s novel featuring Hester Prynne and the scarlet letter?'),
    (3, 'In which New England state is Nathaniel Hawthorne often associated with?'),
    (3, 'What is the moral theme explored in Nathaniel Hawthorne''s "The Minister''s Black Veil"?'),
    (3, 'What is Nathaniel Hawthorne''s famous collection of short stories published in 1837?'),
    (3, 'Who is the protagonist in Hawthorne''s "The House of the Seven Gables"?'),

    (4, 'Who was Jonathan Edwards known for his sermons to?'),
    (4, 'In which religious movement did Jonathan Edwards play a significant role?'),
    (4, 'What is the title of Jonathan Edwards''s most famous sermon?'),
    (4, 'Where did Jonathan Edwards serve as a minister?'),
    (4, 'What theological concept is central to Jonathan Edwards''s sermons?'),

    (5, 'What is the title of Edgar Allan Poe''s famous poem about a lost love?'),
    (5, 'In which city did Edgar Allan Poe spend a significant portion of his life?'),
    (5, 'What is the central theme of Poe''s "The Tell-Tale Heart"?'),
    (5, 'Which literary genre is often associated with Edgar Allan Poe?'),
    (5, 'What is the name of Poe''s famous detective character?');

CREATE TABLE IF NOT EXISTS Answers (
    AnswerID INTEGER PRIMARY KEY,
    QuestionID INTEGER,
    AnswerText TEXT NOT NULL,
    IsCorrect BOOLEAN NOT NULL,
    FOREIGN KEY (QuestionID) REFERENCES Questions(QuestionID)
);

INSERT INTO Answers (QuestionID, AnswerText, IsCorrect) VALUES
    (1, 'Of Plymouth Plantation', 1),
    (1, 'Mayflower Compact', 0),
    (1, 'Edward Winslow', 0),
    (1, 'Drafting and signing the compact', 1),
    (1, 'Plymouth, Massachusetts', 0),

    (6, 'Letters from an American Farmer', 1),
    (6, '19th century', 0),
    (6, 'Melting Pot', 1),
    (6, 'France', 1),
    (6, 'Farmer', 1),

    (11, 'The Scarlet Letter', 1),
    (11, 'Massachusetts', 1),
    (11, 'Secret sins and guilt', 1),
    (11, 'Twice-Told Tales', 1),
    (11, 'Hepzibah Pyncheon', 1),

    (16, 'Congregants in Northampton, Massachusetts', 1),
    (16, 'Great Awakening', 1),
    (16, 'Sinners in the Hands of an Angry God', 1),
    (16, 'Northampton', 1),
    (16, 'Predestination', 1),

    (21, 'The Raven', 1),
    (21, 'Baltimore', 1),
    (21, 'Madness and guilt', 1),
    (21, 'Gothic fiction', 1),
    (21, 'C. Auguste Dupin', 1);
