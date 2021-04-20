CREATE TABLE `JournalEntries` (
	`id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`date`	TEXT NOT NULL,
	`concept`	TEXT NOT NULL,
	`entry`	TEXT NOT NULL,
	`moodId`	TEXT NOT NULL,
    FOREIGN KEY(`moodId`) REFERENCES `Moods`(`id`)
);

CREATE TABLE `Moods` (
    `id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `label`    TEXT NOT NULL
);

SELECT * FROM JournalEntries

INSERT INTO `Moods` VALUES(null, "Happy");
INSERT INTO `Moods` VALUES(null, "Sad");
INSERT INTO `Moods` VALUES(null, "Mad");
INSERT INTO `Moods` VALUES(null, "Confused");

INSERT INTO `JournalEntries` VALUES(null, "02-10-2010", "concept", "this is a great day", 1);
INSERT INTO `JournalEntries` VALUES(null, "02-10-2010", "concept", "this is a bad day", 2);
INSERT INTO `JournalEntries` VALUES(null, "02-10-2010", "concept", "this is a long day", 3);

DELETE FROM 'JournalEntries' WHERE id=1;

ALTER TABLE JournalEntries
RENAME COLUMN mood TO moodId

SELECT *
FROM Moods

SELECT
    j.id,
    j.concept,
    j.entry,
	j.date,
    j.moodId,
    m.label mood_label,
FROM JournalEntries j
JOIN Moods m
    ON m.id = j.moodId
