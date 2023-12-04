-- define source
with
    teams as (select * from {{ ref("raw_teams") }}),

    -- get team information from source
    teams_subset as (
        select farm_fingerprint(name) as teams_key, teams.* except (venue_id) from teams
    )

select distinct *
from teams_subset
