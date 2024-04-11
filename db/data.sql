-- Contact Table
CREATE TABLE "contact" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "profile_image" text NULL,
    "name" varchar(100) NOT NULL,
    "email" varchar(100) NULL,
    "phone" varchar(20) NULL,
    "company" varchar(20) NULL,
    "position" varchar(20) NULL,
    "memo" text NULL,
    "address" varchar(200) NULL,
    "birthday" datetime NULL,
    "website" varchar(200) NULL
);

-- Label Table
CREATE TABLE "label" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "name" varchar(100) NOT NULL,
    "contact_id" bigint NOT NULL REFERENCES "contact" ("id") DEFERRABLE INITIALLY DEFERRED
);
