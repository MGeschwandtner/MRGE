with
    game_results as (
        select
            away_teams_key as team_key,
            case
                when fixture_away_winner
                then 3
                when fixture_away_winner is null
                then 1
                else 0
            end as points,
            ff.fixture_away_team_goals as scored_goals,
            ff.fixture_home_team_goals as conceded_goals
        from {{ ref("f_fixtures") }} ff
        inner join {{ ref("d_fixtures") }} as df on df.fixture_key = ff.fixture_key
        where fixture_game_status_long_string = 'Match Finished'
        union all
        select
            home_team_key as team_key,
            case
                when fixture_home_winner
                then 3
                when fixture_home_winner is null
                then 1
                else 0
            end as points,
            ff.fixture_home_team_goals as scored_goals,
            ff.fixture_away_team_goals as conceded_goals
        from {{ ref("f_fixtures") }} ff
        inner join {{ ref("d_fixtures") }} as df on df.fixture_key = ff.fixture_key
        where fixture_game_status_long_string = 'Match Finished'
    )
select
    dt.name as teamname,
    sum(points) as points,
    sum(scored_goals) as scored_goals,
    sum(conceded_goals) as conceded_goals,
    sum(scored_goals) - sum(conceded_goals) as goal_diff
from game_results
left join {{ ref("d_teams") }} as dt on dt.teams_key = game_results.team_key
group by 1
order by points desc, goal_diff desc
