-- define source
with
    venues as (select * from {{ ref("raw_venues") }}),

    -- get team information from source
    venues_subset as (
        select
            farm_fingerprint(cast(id as string)) as venue_key,
            address,
            capacity,
            city,
            id,
            image,
            name,
            surface
        from venues
    )

select distinct *
from venues_subset
