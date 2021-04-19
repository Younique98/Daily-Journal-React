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