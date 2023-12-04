-- define source
with teams as (select * from {{ source("football_api_data", "teams") }}),

-- get team information from source
teams_subset as (
select team.*,venue.id as venue_id from teams
)

select distinct * from teams_subset