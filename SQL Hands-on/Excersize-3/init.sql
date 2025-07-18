-- Active: 1751469617468@@127.0.0.1@5432@corona_data
-- Active: 1751469617468@@127.0.0.1@5432@corona_data
CREATE TABLE
    hhs (
        "Provider Name" varchar(150),
        Address1 VARCHAR(200),
        Address2 varchar(200),
        City varchar(80),
        County varchar(80),
        "State Code" varchar(80),
        Zip varchar(80),
        "National Drug Code" varchar(80),
        "Order Label" VARCHAR(80),
        "Courses Available" VARCHAR(80),
        "Geocoded Address" VARCHAR(80),
        NPI VARCHAR(80),
        "Last Report Date" TIMESTAMP,
        "Provider Status" VARCHAR(80),
        "Provider Note" VARCHAR(80)
    );