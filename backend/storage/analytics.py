from redis.asyncio import Redis


async def update_price_target_requests(client: Redis):
    if not await client.hget('$', 'analytics'):
        await client.hset('analytics', mapping={
            "price_target_requests": 0,
            "locations": {},
            "categories": {},
        })

    await client.hincrby(name="analytics", key="price_target_requests", amount=1)


async def update_locations_requests(client: Redis, location_id: int):
    await client.hincrby(name="analytics:locations", key=str(location_id), amount=1)


async def update_categories_requests(client: Redis, category_id: int):
    await client.hincrby(name="analytics:categories", key=str(category_id), amount=1)


storage_example = {
    "baseline": 0,
    "discounts": set(),

    "analytics": {
        "price_target_requests": 0,

        "locations": {"location_id": 0},
        "categories": {"category_id": 0},
    }
}
