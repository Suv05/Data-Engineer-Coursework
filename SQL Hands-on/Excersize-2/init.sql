-- Active: 1751469617468@@127.0.0.1@5432@corona_data
CREATE TABLE
    hhs (
        hhs_id varchar(80),
        ccn VARCHAR(80),
        facility_name varchar(200),
        address varchar(180),
        city varchar(80),
        zip varchar(80),
        fips_code varchar(80),
        state varchar(80),
        geohash  VARCHAR(150),
        geocoded_hospital_address VARCHAR(150)  
    );