-- import source
with
    -- only taking latest result of fixtures
    fixtures as (
        select *
        from {{ ref("raw_fixtures") }}
        where
            (id, repl_date)
            in (select (id, max(repl_date)) from {{ ref("raw_fixtures") }} group by id)
    ),
    referee as (select * from {{ ref("d_referee") }}),
    venues as (select * from {{ ref("d_venues") }}),
    teams as (select * from {{ ref("d_teams") }}),
    d_fixtures as (select * from {{ ref("d_fixtures") }})

-- add business logic 
select
    f.id as fixture_id,
    r.referee_key,
    venue_key,
    df.fixture_key,
    away_t.teams_key as away_teams_key,
    home_t.teams_key as home_team_key,
    f.fixture_away_team_goals,
    f.fixture_away_team_goals_halftime,
    f.fixture_home_team_goals,
    f.fixture_home_team_goals_halftime
from fixtures as f
left join referee as r on r.referee_name = split(f.referee, ',')[0]
left join venues as v on v.id = f.venue_id
left join teams as away_t on away_t.id = f.fixture_away_team_id
left join teams as home_t on home_t.id = f.fixture_home_team_id
left join d_fixtures as df on df.id = f.id
