-- define source
with venues as (select * from {{ source("football_api_data", "teams") }}),

-- get team information from source
venues_subset as (
select venue.*,team.id as team_id,repl_date from venues
)

select distinct * from venues_subset