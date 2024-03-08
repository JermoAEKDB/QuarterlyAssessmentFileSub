-- database: :memory:

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

CREATE TABLE IF NOT EXISTS WilliamBradford (
    QuestionID INTEGER PRIMARY KEY,
    QuestionText TEXT NOT NULL,
    AnswerText TEXT NOT NULL,
    IsCorrect BOOLEAN NOT NULL
);

INSERT INTO WilliamBradford (QuestionText, AnswerText, IsCorrect) VALUES
    ('What is the title of William Bradford''s most famous work?', 'Of Plymouth Plantation', 1),
    ('In which year did William Bradford and the Pilgrims arrive in America?', 'Mayflower Compact', 0),
    ('Who succeeded William Bradford as the governor of Plymouth Colony?', 'Edward Winslow', 0),
    ('What role did William Bradford play in the development of the Mayflower Compact?', 'Drafting and signing the compact', 1),
    ('Where is William Bradford buried?', 'Plymouth, Massachusetts', 0);

CREATE TABLE IF NOT EXISTS JeanDeCrevecouer (
    QuestionID INTEGER PRIMARY KEY,
    QuestionText TEXT NOT NULL,
    AnswerText TEXT NOT NULL,
    IsCorrect BOOLEAN NOT NULL
);

INSERT INTO JeanDeCrevecouer (QuestionText, AnswerText, IsCorrect) VALUES
    ('What is Jean De Crevecouer''s famous work that explores the idea of the American identity?', 'Letters from an American Farmer', 1),
    ('In which century did Jean De Crevecouer write about American life?', '19th century', 0),
    ('What term did Jean De Crevecouer coin to describe the American identity?', 'Melting Pot', 1),
    ('Where was Jean De Crevecouer born?', 'France', 1),
    ('What was Jean De Crevecouer''s occupation in the American colonies?', 'Farmer', 1);

CREATE TABLE IF NOT EXISTS NathanielHawthorne (
    QuestionID INTEGER PRIMARY KEY,
    QuestionText TEXT NOT NULL,
    AnswerText TEXT NOT NULL,
    IsCorrect BOOLEAN NOT NULL
);

INSERT INTO NathanielHawthorne (QuestionText, AnswerText, IsCorrect) VALUES
    ('What is the title of Nathaniel Hawthorne''s novel featuring Hester Prynne and the scarlet letter?', 'The Scarlet Letter', 1),
    ('In which New England state is Nathaniel Hawthorne often associated with?', 'Massachusetts', 1),
    ('What is the moral theme explored in Nathaniel Hawthorne''s "The Minister''s Black Veil"?', 'Secret sins and guilt', 1),
    ('What is Nathaniel Hawthorne''s famous collection of short stories published in 1837?', 'Twice-Told Tales', 1),
    ('Who is the protagonist in Hawthorne''s "The House of the Seven Gables"?', 'Hepzibah Pyncheon', 1);

CREATE TABLE IF NOT EXISTS JonathanEdwards (
    QuestionID INTEGER PRIMARY KEY,
    QuestionText TEXT NOT NULL,
    AnswerText TEXT NOT NULL,
    IsCorrect BOOLEAN NOT NULL
);

INSERT INTO JonathanEdwards (QuestionText, AnswerText, IsCorrect) VALUES
    ('Who was Jonathan Edwards known for his sermons to?', 'Congregants in Northampton, Massachusetts', 1),
    ('In which religious movement did Jonathan Edwards play a significant role?', 'Great Awakening', 1),
    ('What is the title of Jonathan Edwards''s most famous sermon?', 'Sinners in the Hands of an Angry God', 1),
    ('Where did Jonathan Edwards serve as a minister?', 'Northampton', 1),
    ('What theological concept is central to Jonathan Edwards''s sermons?', 'Predestination', 1);

CREATE TABLE IF NOT EXISTS EdgarAllanPoe (
    QuestionID INTEGER PRIMARY KEY,
    QuestionText TEXT NOT NULL,
    AnswerText TEXT NOT NULL,
    IsCorrect BOOLEAN NOT NULL
);

INSERT INTO EdgarAllanPoe (QuestionText, AnswerText, IsCorrect) VALUES
    ('What is the title of Edgar Allan Poe''s famous poem about a lost love?', 'The Raven', 1),
    ('In which city did Edgar Allan Poe spend a significant portion of his life?', 'Baltimore', 1),
    ('What is the central theme of Poe''s "The Tell-Tale Heart"?', 'Madness and guilt', 1),
    ('Which literary genre is often associated with Edgar Allan Poe?', 'Gothic fiction', 1),
    ('What is the name of Poe''s famous detective character?', 'C. Auguste Dupin', 1);
