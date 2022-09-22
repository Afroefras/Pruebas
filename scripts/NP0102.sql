select
    id,
    city,
    price
from
    (select
        id,
        city,
        price,
        row_number() over (partition by city order by price, id) as n
    from flats
    where price between 1000 and 10000000
    limit 100
    ) a
where n<=3
order by 1;