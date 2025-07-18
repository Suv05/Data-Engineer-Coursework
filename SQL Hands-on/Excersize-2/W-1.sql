-- Active: 1751469617468@@127.0.0.1@5432@corona_data

SELECT * FROM hhs;

SELECT hhs_id,facility_name,state
FROM hhs;

-- no.of hss in every state
SELECT  count(hhs_id),state
FROM hhs
GROUP BY(state);