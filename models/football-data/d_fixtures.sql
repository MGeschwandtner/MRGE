-- import source
with
    -- only taking latest result of fixtures
    fixtures as (
        select *
        from {{ ref("raw_fixtures") }}
        where
            (id, repl_date)
            in (select (id, max(repl_date)) from {{ ref("raw_fixtures") }} group by id)
    )

-- add business logic 
select distinct
    farm_fingerprint(cast(id as string)) as fixture_key,
    id,
    f.fixture_datetime,
    f.fixture_away_winner,
    f.fixture_home_winner,
    fixture_league_round,
    fixture_league_season,
    fixture_game_status_long_string
from fixtures as f
