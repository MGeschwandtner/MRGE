-- import source
with fixtures as (select * from {{ ref("raw_fixtures") }})

select distinct
    split(referee, ',')[0] as referee_name,
    if(ARRAY_LENGTH(split(referee, ',')) > 1, split(referee, ',')[ORDINAL(2)], null)  as referee_origin,
    farm_fingerprint(referee) as referee_key
from fixtures
where referee is not null
