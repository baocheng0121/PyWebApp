DROP SCHEMA IF EXISTS framework CASCADE;

CREATE SCHEMA framework;
SET search_path to 'framework';

DROP TABLE IF EXISTS UserAccount;
CREATE TABLE UserAccount(
    user_id  INT(10) unsigned NOT NULL AUTO_INCREMENT,
    username VARCHAR(50) PRIMARY KEY,
    password VARCHAR(72) NOT NULL,
    is_admin INT(1) DEFAULT 0
);
