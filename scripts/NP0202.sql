with players_first_scores as(
    select 
        player_id,
        sum(coalesce(mf.first_score, 0)) as sum_first_score
    from players p
        left  join matches mf on mf.first_player = p.player_id
    group by 1
    ),


    players_second_scores as(
    select 
        player_id,
        sum(coalesce(ms.second_score, 0)) as sum_second_score
    from players p
        left join matches ms on ms.second_player = p.player_id
    group by 1
    ),


    players_scores as(
    select 
        player_id,
        coalesce(sum_first_score + sum_second_score, 0) as sum_score
    from players_first_scores pf
        full outer join players_second_scores using(player_id)
    ),


    top_scores as(
    select
        p.player_id,
        p.group_id,
        ps.sum_score,
        row_number() over (partition by p.group_id order by ps.sum_score desc, p.player_id) as n
    from players_scores ps
        join players p using(player_id)
    )


select
    group_id,
    player_id as winner_id
from top_scores
where n = 1;