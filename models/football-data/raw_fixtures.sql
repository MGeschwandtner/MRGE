-- import source
with fixtures as (select * from {{ source("football_api_data", "fixtures") }}),

-- add business logic 
fixtures_subset as (
select
    fixture.date as fixture_datetime,
    fixture.id fixture_id,
    fixture.referee as referee,
    fixture.status.elapsed as fixture_elapsed_minutes,
    fixture.status.long as fixture_game_status_long_string,
    fixture.venue.id as venue_id,
    league.round as fixture_league_round,
    league.season as fixture_league_season,
    teams.away.id as fixture_away_team_id,
    teams.home.id as fixture_home_team_id,
    teams.away.winner as fixture_away_winner,
    teams.home.winner as fixture_home_winner,
    goals.home as fixture_home_team_goals,
    goals.away as fixture_away_team_goals,
    score.halftime.away as fixture_away_team_goals_halftime,
    score.halftime.home as fixture_home_team_goals_halftime,
    repl_date
from fixtures
order by fixture.date
)

-- final read
select distinct * from fixtures_subset
